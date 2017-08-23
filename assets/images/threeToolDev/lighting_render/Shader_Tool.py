# -*- Coding: Utf-8 -*- 

#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

#工具名字 ："Shader Tool"
#书写时间 ：2012 . 7 - 2012 . 8
#作      者 ：郑卫福
#版      本 ：V1.0
#电子邮件 ：651999307@qq.com
#maya版本 ：V2012-x64

#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

#使用方法：
#       1. 拷贝"Shader_Tool.py"到"...\Documents\maya\2012-x64\scripts"(或者python可以调用的路径下面)。
#       2. 打开maya2012。
#       3. 进入script Editor,python模块(编写 from Shader_Tool import * ;shader_ui())。

#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

import maya.cmds as cmds 
import maya.mel as mel
import AddOtherAttrForShade as aas

def shader_ui():
    mr=cmds.pluginInfo("Mayatomr", q=True, l=True)
    if not mr:
        cmds.loadPlugin("Mayatomr")
        cmds.confirmDialog( title='load mr_V2', message='++++++"Mayatomr" was loaded,please Try again.++++++',b='colse')
        return 
    if cmds.window('shader_ui',ex=True):
        cmds.deleteUI('shader_ui')
    window=cmds.window('shader_ui',t='Shader Tool V1.0',wh=(230,215))
    m_c=cmds.columnLayout('smain_col',cat=["both",3],adj=True)
    m_f=cmds.frameLayout('smain_frame',label='Shader Switch',borderStyle='etchedOut')
    m_rf=cmds.rowLayout('sm_r',nc=2, cw2=(120,50), adjustableColumn=2, columnAlign=(1, 'both'), columnAttach=[(1, 'both', 0), (2, 'both', 0)] )
    shader_itsl=cmds.textScrollList('ssitsl',allowMultiSelection=False,append=['Blinn','mi_blinn'],h=65)
    cmds.columnLayout('Lsmain_col',rs=5,adj=True)
    tg_b=cmds.button('stomi_blinn',l='>>>mi_blinn',h=30, bgc=[0.4, 0.6, 0.6],c=lambda *args:SwitchShader())
    Ltg_b=cmds.button('stoLambert',l='>>>lambert(FG)',h=30, bgc=[0.4, 0.6, 0.6],c=lambda *args:mi_blinnToLambert())
    cmds.setParent('smain_col')
    cmds.separator('ssss_f', height=10, style='in' )
    cg_bs=cmds.button('cmi_blinn',l='Create "mi_blinn"...', h=30, bgc=[0.4, 0.46, 0.8], c=lambda *args:ass_mi_blinnTOsel())
    cmds.separator(height=10, style='in' )
    cg_mtb=cmds.button('cmi_Toblinn',l='"mi_blinn">>>"blinn"', h=30, bgc=[0.4, 0.46, 0.8], c=mi_blinnToBlinn)
    cmds.separator(height=10, style='in' )
    cg_ba=cmds.button('cmi_AddAttr',l='Add Attribute (for selected shade)"...', h=30, bgc=[0.4, 0.46, 0.8],c='import AddOtherAttrForShade as aoafs;aoafs.AddAttrforselectshades()')
    cmds.separator('ssss_s', height=10, style='in' )
    cg_ba=cmds.button('cmi_blinnAsss',l='Create and connect"mi_sss" to "mi_blinn"...', h=30, bgc=[0.85, 0.6, 0.5],c=lambda *args:create_mi_sssTo_mi_blinn())
    cmds.window('shader_ui',e=True, wh=(230,255))
    cmds.showWindow('shader_ui')

def createdefault_mi_blinn():
    shadername=mel.eval('mrCreateCustomNode -asShader "" mi_blinn')
    shadername_G=cmds.listConnections(shadername,s=0)[0]
    cmds.disconnectAttr('%s.message'%shadername, '%s.miMaterialShader'%shadername_G)
    #shadername_G=cmds.sets(renderable=True, noSurfaceShader=True, empty=True, name='%sSG'%shadername)
    cmds.connectAttr('%s.outColor'%shadername,'%s.surfaceShader'%shadername_G, f=True)
    bumpshader=cmds.shadingNode('bump2d',asUtility=True)
    cmds.connectAttr('%s.outNormal'%bumpshader, '%s.normalCamera'%shadername, f=True)
    shadowshader=mel.eval('mrCreateCustomNode -asUtility "" mayaShadow')
    cmds.connectAttr('%s.transparency'%shadername, '%s.transparency'%shadowshader, f=True)
    cmds.connectAttr('%s.shadowAttenuation'%shadername, '%s.shadowAttenuation'%shadowshader, f=True)
    cmds.connectAttr('%s.translucenceDepth'%shadername, '%s.translucenceDepth'%shadowshader, f=True)
    cmds.connectAttr ('%s.outValue'%shadowshader, '%s.miShadowShader'%shadername_G, f=True)
    return shadername

def ass_mi_blinnTOsel():
    sel=cmds.ls(sl=True)
    mb=createdefault_mi_blinn()
    if len(sel):
        mb_G=cmds.listConnections(mb,s=False,type='shadingEngine')[0]
        cmds.sets(sel, e=True, forceElement=mb_G)

def ssgetAllShaders(ShaderType=''):
    shaders=cmds.ls(type=ShaderType)
    return shaders

def getShaderChannel(shaderName,channelname,generalname,newchannelname):
    if cmds.objExists('%s.%s'%(shaderName,channelname)) and cmds.objExists('%s.%s'%(generalname,newchannelname)):
        e_all=cmds.objExists('%s.%s'%(shaderName,channelname))
        e_r=cmds.objExists('%s.%sR'%(shaderName,channelname))
        e_g=cmds.objExists('%s.%sG'%(shaderName,channelname))
        e_b=cmds.objExists('%s.%sB'%(shaderName,channelname))
        ci_all=cmds.connectionInfo('%s.%s'%(shaderName,channelname), isDestination=True)
        if e_all:
            if ci_all:
                all=cmds.listConnections('%s.%s'%(shaderName,channelname),d=False,p=True)[0]
                cmds.connectAttr (all, '%s.%s'%(generalname,newchannelname),f=True)
            else:
                if e_r:
                    ci_r=cmds.connectionInfo('%s.%sR'%(shaderName,channelname), isDestination=True)
                    if ci_r:
                        r=cmds.listConnections('%s.%sR'%(shaderName,channelname),d=False,p=True)[0]
                        cmds.connectAttr (r, '%s.%sR'%(generalname,newchannelname),f=True)
                if e_g:
                    ci_g=cmds.connectionInfo('%s.%sG'%(shaderName,channelname), isDestination=True)
                    if ci_g:
                        g=cmds.listConnections('%s.%sG'%(shaderName,channelname),d=False,p=True)[0]
                        cmds.connectAttr (g, '%s.%sG'%(generalname,newchannelname),f=True)
                if e_b:
                    ci_b=cmds.connectionInfo('%s.%sB'%(shaderName,channelname), isDestination=True)
                    if ci_b:
                        b=cmds.listConnections('%s.%sB'%(shaderName,channelname),d=False,p=True)[0]
                        cmds.connectAttr (b, '%s.%sB'%(generalname,newchannelname),f=True)
        if e_all==1 and e_r==1 and e_g==1 and e_b==1:
            if ci_all!=1 and ci_r!=1 and ci_g!=1 and ci_b!=1:
                number_r=cmds.getAttr('%s.%sR'%(shaderName,channelname))
                number_g=cmds.getAttr('%s.%sG'%(shaderName,channelname))
                number_b=cmds.getAttr('%s.%sB'%(shaderName,channelname))
                cmds.setAttr('%s.%s'%(generalname,newchannelname), number_r, number_g, number_b,type='double3')
        if e_all==1 and e_r!=1 and e_g!=1 and e_b!=1:
            if ci_all!=1 :
                number=cmds.getAttr('%s.%s'%(shaderName,channelname))
                if channelname=='miReflectionBlur' or channelname=='miRefractionBlur':
                    number*=0.01
                cmds.setAttr('%s.%s'%(generalname,newchannelname), number)

def SwitchShader():
    sel_shaderType=cmds.textScrollList('ssitsl',q=True,si=True)
    if sel_shaderType==None:
        cmds.warning('no selected in textScrollList.')
    else:
        if sel_shaderType[0]=='Blinn':
            shaders=cmds.ls(sl=True,type='blinn')
            if not len(shaders):
                return cmds.warning('no type: "blinn" were select,please select some "blinn" shaders!')
            else:
                for each in shaders:
                    aas.AddOtherAttr(each,'sss')
                    aas.AddOtherAttr(each,'addSpecular')
                    aas.AddOtherAttr(each,'addReflection')
                    aas.AddOtherAttr(each,'ambientOcclusion')
                    aas.AddOtherAttr(each,'worldNormal')
                    aas.AddOtherAttr(each,'zdepth')
                    aas.AddOtherAttr(each,'facingRatio')
                    aas.AddOtherAttr(each,'mv')
                    aas.AddOtherAttr(each,'assetObjectID')
                    aas.AddOtherAttr(each,'materialID')
                    eachG=cmds.listConnections(each,s=False,type='shadingEngine')
                    if eachG==None:
                        mel.eval('print "+++++++++ %s was unused node! ++++++++++"'%each)
                        continue
                    myshader=createdefault_mi_blinn()
                    myshader=cmds.rename(myshader,each)
                    myshaderG=cmds.listConnections(myshader,s=False,type='shadingEngine')[0]
                    myshaderS=cmds.listConnections(myshader,s=False,type='mayaShadow')[0]
                    cmds.delete(myshaderG)
                    for single in eachG:
                        cmds.connectAttr('%s.outColor'%myshader, '%s.surfaceShader'%single, f=True)
                        cmds.connectAttr('%s.outValue'%myshaderS, '%s.miShadowShader'%single, f=True)
                    CreateConnectionsForShader(each,myshader)
            mel.eval('hyperShadePanelMenuCommand("hyperShadePanel1", "deleteUnusedNodes")')
        else:
            cmds.warning('Please select "Blinn" in the list')

def mi_blinnToBlinn(*args):
    mi_blinns=cmds.ls(type='mi_blinn')
    if mi_blinns:
        for mi_blinn in mi_blinns:
            blinn=cmds.shadingNode("blinn",asShader=True,name=mi_blinn) 
            aas.AddOtherAttr(blinn,'sss')
            aas.AddOtherAttr(blinn,'addSpecular')
            aas.AddOtherAttr(blinn,'addReflection')
            aas.AddOtherAttr(blinn,'ambientOcclusion')
            aas.AddOtherAttr(blinn,'worldNormal')
            aas.AddOtherAttr(blinn,'zdepth')
            aas.AddOtherAttr(blinn,'facingRatio')
            aas.AddOtherAttr(blinn,'mv')
            aas.AddOtherAttr(blinn,'assetObjectID')
            aas.AddOtherAttr(blinn,'materialID')
            mi_blinnSG=cmds.listConnections(mi_blinn,s=False,type='shadingEngine')
            if mi_blinnSG:
                try:
                    cmds.connectAttr('%s.outColor'%blinn, '%s.surfaceShader'%mi_blinnSG[0], f=True)
                except: pass
            CreateConnectionsForShader(mi_blinn,blinn)
            isBumpDown(blinn)
        mel.eval('hyperShadePanelMenuCommand("hyperShadePanel1", "deleteUnusedNodes")')
        others=cmds.ls(type=['misss_fast_lmap_maya','mayaShadow'])
        if others:
            try:cmds.delete(others)
            except:pass
    else:
        cmds.warning('No "mi_blinn" in the scene!')

def isBumpDown(shader):
    bumpl=[]
    attr=['normalCamera','normalCameraX','normalCameraY','normalCameraZ']
    for i in attr:
        b=cmds.listConnections('%s.%s'%(shader,i),d=False)
        if b:
            if b[0] not in bumpl:
                bumpl.append(b[0])
    if bumpl:
        bbl=[]
        for x in bumpl:
            bb=cmds.listConnections('%s.bumpValue'%x,d=False)
            if bb:
                if bb[0] not in bbl:
                    bbl.append(bb[0])
        if not bbl:
            try:
                cmds.delete(bumpl)
            except:
                aa=`bumpl`
                print '%s can not be deleted!'%aa
                print aa

def CreateConnectionsForShader(each,myshader):
#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    #++++++++++++++++++++++++++++++++++++connect color++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    getShaderChannel(each,'color',myshader,'color')
    #++++++++++++++++++++++++++++++++++++connect transparency++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    getShaderChannel(each,'transparency',myshader,'transparency')
    #++++++++++++++++++++++++++++++++++++connect ambientColor++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    getShaderChannel(each,'ambientColor',myshader,'ambientColor')
    '''
    ambientColorlist=['%s.ambientColor'%each,'%s.ambientColorR'%each,'%s.ambientColorG'%each,'%s.ambientColorB'%each]
    alls=cmds.listConnections(ambientColorlist,d=False)
    if alls!=None:
        if cmds.nodeType(alls[0])=='mi_sss':
            ass=cmds.listConnections('%s.ambientColor'%each,d=False,p=True)[0]
            cmds.connectAttr (ass, '%s.sss'%myshader,f=True)
        else:
            getShaderChannel(each,'ambientColor',myshader,'ambientColor')
    else:
        number_r=cmds.getAttr('%s.ambientColorR'%each)
        number_g=cmds.getAttr('%s.ambientColorG'%each)
        number_b=cmds.getAttr('%s.ambientColorB'%each)
        cmds.setAttr('%s.ambientColor'%myshader, number_r, number_g, number_b ,type='double3')
    '''
    #++++++++++++++++++++++++++++++++++++connect sss++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    getShaderChannel(each,'sss',myshader,'sss')
    #++++++++++++++++++++++++++++++++++++connect addSpecular++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    getShaderChannel(each,'addSpecular',myshader,'addSpecular')
    #++++++++++++++++++++++++++++++++++++connect addReflection++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    getShaderChannel(each,'addReflection',myshader,'addReflection')
    #++++++++++++++++++++++++++++++++++++connect ambientOcclusion++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    getShaderChannel(each,'ambientOcclusion',myshader,'ambientOcclusion')
    #++++++++++++++++++++++++++++++++++++connect worldNormal++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    getShaderChannel(each,'worldNormal',myshader,'worldNormal')
    #++++++++++++++++++++++++++++++++++++connect zdepth++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    getShaderChannel(each,'zdepth',myshader,'zdepth')
    #++++++++++++++++++++++++++++++++++++connect facingRatio++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    getShaderChannel(each,'facingRatio',myshader,'facingRatio')
    #++++++++++++++++++++++++++++++++++++connect mv++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    getShaderChannel(each,'mv',myshader,'mv')
    #++++++++++++++++++++++++++++++++++++connect assetObjectID++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    getShaderChannel(each,'assetObjectID',myshader,'assetObjectID')
    #++++++++++++++++++++++++++++++++++++connect materialID++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    getShaderChannel(each,'materialID',myshader,'materialID')

    #++++++++++++++++++++++++++++++++++++connect incandescence++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    getShaderChannel(each,'incandescence',myshader,'incandescence')
    #++++++++++++++++++++++++++++++++++++connect normalCamera++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    nc_all=cmds.connectionInfo('%s.normalCamera'%each, isDestination=True)
    if nc_all:
        d_all=cmds.listConnections('%s.normalCamera'%each,d=False,p=True)[0]
        cmds.connectAttr (d_all, '%s.normalCamera'%myshader,f=True)
    else:
        nc_x=cmds.connectionInfo('%s.normalCameraX'%each, isDestination=True)
        nc_y=cmds.connectionInfo('%s.normalCameraY'%each, isDestination=True)
        nc_z=cmds.connectionInfo('%s.normalCameraZ'%each, isDestination=True)
        if nc_x:
            d_x=cmds.listConnections('%s.normalCameraX'%each,d=False,p=True)[0]
            cmds.connectAttr (d_x, '%s.normalCameraX'%myshader,f=True)
        if nc_y:
            d_y=cmds.listConnections('%s.normalCameraY'%each,d=False,p=True)[0]
            cmds.connectAttr (d_y, '%s.normalCameraY'%myshader,f=True)
        if nc_z:
            d_z=cmds.listConnections('%s.normalCameraZ'%each,d=False,p=True)[0]
            cmds.connectAttr (d_z, '%s.normalCameraZ'%myshader,f=True)
    #++++++++++++++++++++++++++++++++++++connect diffuse++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    getShaderChannel(each,'diffuse',myshader,'diffuse')
    #++++++++++++++++++++++++++++++++++++connect translucence+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    getShaderChannel(each,'translucence',myshader,'translucence')
    #++++++++++++++++++++++++++++++++++++connect translucenceDepth+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    getShaderChannel(each,'translucenceDepth',myshader,'translucenceDepth')
    #++++++++++++++++++++++++++++++++++++connect translucenceFocus++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    getShaderChannel(each,'translucenceFocus',myshader,'translucenceFocus')
#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    #++++++++++++++++++++++++++++++++++++connect eccentricity++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    getShaderChannel(each,'eccentricity',myshader,'eccentricity')
    #++++++++++++++++++++++++++++++++++++connect specularRollOff++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    getShaderChannel(each,'specularRollOff',myshader,'specularRollOff')
    #++++++++++++++++++++++++++++++++++++connect specularColor++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    getShaderChannel(each,'specularColor',myshader,'specularColor')
    #++++++++++++++++++++++++++++++++++++connect reflectivity++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    getShaderChannel(each,'reflectivity',myshader,'reflectivity')
    #++++++++++++++++++++++++++++++++++++connect reflectedColor++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    getShaderChannel(each,'reflectedColor',myshader,'reflectedColor')
    #++++++++++++++++++++++++++++++++++++connect reflectionRolloff++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    getShaderChannel(each,'reflectionRolloff',myshader,'reflectionRolloff')
#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    #++++++++++++++++++++++++++++++++++++connect hideSource++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    getShaderChannel(each,'hideSource',myshader,'hideSource')
    #++++++++++++++++++++++++++++++++++++connect glowIntensity+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    getShaderChannel(each,'glowIntensity',myshader,'glowIntensity')
#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    #++++++++++++++++++++++++++++++++++++connect matteOpacityMode++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    getShaderChannel(each,'matteOpacityMode',myshader,'matteOpacityMode')
    #++++++++++++++++++++++++++++++++++++connect matteOpacity+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    getShaderChannel(each,'matteOpacity',myshader,'matteOpacity')
#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    #++++++++++++++++++++++++++++++++++++connect refractions+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    getShaderChannel(each,'refractions',myshader,'refractions')
    #++++++++++++++++++++++++++++++++++++connect refractiveIndex+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    getShaderChannel(each,'refractiveIndex',myshader,'refractiveIndex')
    #++++++++++++++++++++++++++++++++++++connect refractionLimit++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    getShaderChannel(each,'refractionLimit',myshader,'refractionLimit')
    #++++++++++++++++++++++++++++++++++++connect lightAbsorbance++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    getShaderChannel(each,'lightAbsorbance',myshader,'lightAbsorbance')
    #++++++++++++++++++++++++++++++++++++connect surfaceThickness+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    getShaderChannel(each,'surfaceThickness',myshader,'surfaceThickness')
    #++++++++++++++++++++++++++++++++++++connect shadowAttenuation++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    getShaderChannel(each,'shadowAttenuation',myshader,'shadowAttenuation')
    #++++++++++++++++++++++++++++++++++++connect chromaticAberration++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    getShaderChannel(each,'chromaticAberration',myshader,'chromaticAberration')
    #++++++++++++++++++++++++++++++++++++connect reflectionLimit+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    getShaderChannel(each,'reflectionLimit',myshader,'reflectionLimit')
    #++++++++++++++++++++++++++++++++++++connect reflectionSpecularity+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    getShaderChannel(each,'reflectionSpecularity',myshader,'reflectionSpecularity')
#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    #++++++++++++++++++++++++++++++++++++connect miIrradiance++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    getShaderChannel(each,'miIrradiance',myshader,'irradiance')
    #++++++++++++++++++++++++++++++++++++connect miIrradianceColor+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    getShaderChannel(each,'miIrradianceColor',myshader,'irradianceColor')
    #++++++++++++++++++++++++++++++++++++connect miReflectionBlur++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    getShaderChannel(each,'miReflectionBlur',myshader,'reflectionBlur')
    #++++++++++++++++++++++++++++++++++++connect miReflectionRays++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    try:
        getShaderChannel(each,'miReflectionRays',myshader,'reflectionRays')
        #++++++++++++++++++++++++++++++++++++connect miRefractionBlur++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        getShaderChannel(each,'miRefractionBlur',myshader,'refractionBlur')
        #++++++++++++++++++++++++++++++++++++connect miRefractionRays++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        getShaderChannel(each,'miRefractionRays',myshader,'refractionRays')
        #++++++++++++++++++++++++++++++++++++connect miScatterRadius+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        getShaderChannel(each,'miScatterRadius',myshader,'scatterRadius')
        #++++++++++++++++++++++++++++++++++++connect miScatterColor++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        getShaderChannel(each,'miScatterColor',myshader,'scatterColor')
        #++++++++++++++++++++++++++++++++++++connect miScatterAccuracy+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        getShaderChannel(each,'miScatterAccuracy',myshader,'scatterAccuracy')
        #++++++++++++++++++++++++++++++++++++connect miScatterFalloff+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        getShaderChannel(each,'miScatterFalloff',myshader,'scatterFalloff')
        #++++++++++++++++++++++++++++++++++++connect miScatterLimit++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        getShaderChannel(each,'miScatterLimit',myshader,'scatterLimit')
        #++++++++++++++++++++++++++++++++++++connect miScatterCache++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        getShaderChannel(each,'miScatterCache',myshader,'scatterCache')
        #++++++++++++++++++++++++++++++++++++connect miReflectionBlurLimit++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        getShaderChannel(each,'miReflectionBlurLimit',myshader,'reflectionBlurLimit')
        #++++++++++++++++++++++++++++++++++++connect miRefractionBlurLimit++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        getShaderChannel(each,'miRefractionBlurLimit',myshader,'refractionBlurLimit')
    except: pass
#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    #++++++++++++++++++++++++++++++++++++connect miFrameBufferWriteOperation++++++++++++++++++++++++++++++++++++++++++++++++++++
    getShaderChannel(each,'miFrameBufferWriteOperation',myshader,'FrameBufferWriteOperation')
    #++++++++++++++++++++++++++++++++++++connect miFrameBufferWriteFactor+++++++++++++++++++++++++++++++++++++++++++++++++++++++
    getShaderChannel(each,'miFrameBufferWriteFactor',myshader,'FrameBufferWriteFactor')
    #++++++++++++++++++++++++++++++++++++connect miFrameBufferWriteFlags+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    getShaderChannel(each,'miFrameBufferWriteFlags',myshader,'FrameBufferWriteFlags')
    cmds.delete(each)

def getSelectedMi_blinn():
    sel_mi_blinn=cmds.ls(sl=True,type='mi_blinn')
    return sel_mi_blinn

def create_mi_sssTo_mi_blinn():
    mb=getSelectedMi_blinn()
    if mb==[]:
        cmds.warning('no shaders {type : "mi_blinn"} were selected.')
    else:
        for single in mb:
            if cmds.listConnections('%s.sss'%single,d=False,type='mi_sss')!=None:
                return
            mbg=cmds.listConnections(single,s=False,type='shadingEngine')
            if mbg==None:
                return
            misss=mel.eval('mrCreateCustomNode -asTexture "" mi_sss')
            sss_lmap=mel.eval('mrCreateCustomNode -asUtility "" misss_fast_lmap_maya')
            sss_texture=mel.eval('mrCreateCustomNode -asTexture "" mentalrayTexture')
            cmds.connectAttr('%s.message'%sss_texture,'%s.lightmap'%misss,f=True)
            cmds.connectAttr('%s.message'%sss_texture, '%s.lightmap'%sss_lmap,f=True)
            cmds.connectAttr('%s.message'%sss_lmap, '%s.miLightMapShader'%mbg[0],f=True)
            cmds.connectAttr('%s.outValue'%misss, '%s.sss'%single,f=True)
            nc_all=cmds.connectionInfo('%s.normalCamera'%single, isDestination=True)
            if nc_all:
                d_all=cmds.listConnections('%s.normalCamera'%single,d=False,p=True)[0]
                #print d_all
                if cmds.listConnections(d_all.split('.')[0],d=False)!=None:
                    cmds.connectAttr (d_all, '%s.normalCamera'%misss,f=True)
            else:
                nc_x=cmds.connectionInfo('%s.normalCameraX'%single, isDestination=True)
                nc_y=cmds.connectionInfo('%s.normalCameraY'%single, isDestination=True)
                nc_z=cmds.connectionInfo('%s.normalCameraZ'%single, isDestination=True)
                if nc_x:
                    d_x=cmds.listConnections('%s.normalCameraX'%single,d=False,p=True)[0]
                    cmds.connectAttr (d_x, '%s.normalCameraX'%misss,f=True)
                if nc_y:
                    d_y=cmds.listConnections('%s.normalCameraY'%single,d=False,p=True)[0]
                    cmds.connectAttr (d_y, '%s.normalCameraY'%misss,f=True)
                if nc_z:
                    d_z=cmds.listConnections('%s.normalCameraZ'%single,d=False,p=True)[0]
                    cmds.connectAttr (d_z, '%s.normalCameraZ'%misss,f=True)
            cmds.setAttr("%s.miWritable"%sss_texture,1)
            cmds.setAttr ("%s.miDepth"%sss_texture, 4)
            #mel.eval('expression -e -s "%s.miWidth  = defaultResolution.width * 2"  -o "" -ae 1 -uc all  expression1'%sss_texture)
            #mel.eval('expression -e -s "%s.miHeight = defaultResolution.height"  -o "" -ae 1 -uc all  expression2'%sss_texture)
            cmds.expression(s="%s.miWidth=defaultResolution.width * 2"%sss_texture,o=sss_texture)
            cmds.expression(s="%s.miHeight = defaultResolution.height"%sss_texture,o=sss_texture)

def mi_blinnToLambert():
    sel_shaderType=cmds.textScrollList('ssitsl',q=True,si=True)
    if sel_shaderType==None:
        cmds.warning('no selected in textScrollList.')
    else:
        if sel_shaderType[0]!='mi_blinn':
            return cmds.warning('Please select "mi_blinn" in the list.')
    mats=cmds.ls(type='mi_blinn')
    if len(mats):
        for single in mats:
            sg=cmds.listConnections('%s.outColor'%single,s=False,type='shadingEngine')
            if sg!=None:
                lambertName=cmds.shadingNode('lambert',name=single,asShader=True)
                cmds.setAttr("%s.color"%lambertName, 1, 1, 1, type='double3')
                cmds.connectAttr('%s.outColor'%lambertName,'%s.surfaceShader'%sg[0],f=True)
                getShaderChannel(single,'diffuse',lambertName,'diffuse')
                getShaderChannel(single,'transparency',lambertName,'transparency')

                nc_all=cmds.connectionInfo('%s.normalCamera'%single, isDestination=True)
                if nc_all:
                    d_all=cmds.listConnections('%s.normalCamera'%single,d=False,p=True)[0]
                    ba=cmds.listConnections('%s.normalCamera'%single,d=False)[0]
                    if cmds.listConnections('%s.bumpValue'%ba)!=None:
                        cmds.connectAttr (d_all, '%s.normalCamera'%lambertName,f=True)
                else:
                    nc_x=cmds.connectionInfo('%s.normalCameraX'%single, isDestination=True)
                    nc_y=cmds.connectionInfo('%s.normalCameraY'%single, isDestination=True)
                    nc_z=cmds.connectionInfo('%s.normalCameraZ'%single, isDestination=True)
                    if nc_x:
                        d_x=cmds.listConnections('%s.normalCameraX'%single,d=False,p=True)[0]
                        bx=cmds.listConnections('%s.normalCameraX'%single,d=False)[0]
                        if cmds.listConnections('%s.bumpValue'%bx)!=None:
                            cmds.connectAttr (d_x, '%s.normalCameraX'%lambertName,f=True)
                    if nc_y:
                        d_y=cmds.listConnections('%s.normalCameraY'%single,d=False,p=True)[0]
                        by=cmds.listConnections('%s.normalCameraY'%single,d=False)[0]
                        if cmds.listConnections('%s.bumpValue'%by)!=None:
                            cmds.connectAttr (d_y, '%s.normalCameraY'%lambertName,f=True)
                    if nc_z:
                        d_z=cmds.listConnections('%s.normalCameraZ'%single,d=False,p=True)[0]
                        bz=cmds.listConnections('%s.normalCameraZ'%single,d=False)[0]
                        if cmds.listConnections('%s.bumpValue'%bz)!=None:
                            cmds.connectAttr (d_z, '%s.normalCameraZ'%lambertName,f=True)
                for ss in ['miShadowShader','miLightMapShader']:
                    down=cmds.listConnections('%s.%s'%(sg[0],ss),d=False)
                    if down!=None:
                        cmds.delete(down)
    else:
        print 'No (type : "mi_blinn") shaders in the scene!'
if __name__=="__main__":
    shader_ui()