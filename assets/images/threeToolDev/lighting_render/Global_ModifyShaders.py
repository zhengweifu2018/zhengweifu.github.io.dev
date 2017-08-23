import maya.cmds as cm 
import random
def globalModify_reference_ui():
	if cm.window('gmr_win',ex=True):
		cm.deleteUI('gmr_win')
	gmr_window=cm.window('gmr_win',t='GlobalModify v1.0',wh=(200,300))
	gmr_maincol=cm.columnLayout('g_main_col',cat=["both",3],adj=True)
	gmr_aw_f=cm.frameLayout('g_aw_frame',label='AO / WorldNormal',cll=True,borderStyle='etchedOut',\
		ec=lambda *args:resizeWindowH('gmr_win','g_zd_frame','g_id_frame',688,571,505,388),\
		cc=lambda *args:resizeWindowH('gmr_win','g_zd_frame','g_id_frame',362,245,179,62))
	gmr_faw_col=cm.columnLayout('g_faw_col',cat=["both",3],adj=True)
	gmr_samples=cm.intFieldGrp('g_samp', l='Samples', value1=45,cl2=['right','left'],cw2=[80,70])
	gmr_brig=cm.colorSliderGrp('g_brig',label='Bright', rgb=(1, 1, 1) ,cl3=['right','left','left'],cw3=[80,70,120])
	gmr_dark=cm.colorSliderGrp('g_dark',label='Dark', rgb=(0, 0, 0) ,cl3=['right','left','left'],cw3=[80,70,120])
	gmr_spread=cm.floatFieldGrp('g_spre', l='Spread', value1=0.8,cl2=['right','left'],cw2=[80,70])
	gmr_maxD=cm.floatFieldGrp('g_maxD', l='Max Distance', value1=25,cl2=['right','left'],cw2=[80,70])
	gmr_re_col=cm.columnLayout('g_re_col',cat=["both",83],adj=True)
	gmr_reflective=cm.checkBox('g_reflective',l='Reflective')
	cm.setParent('g_faw_col')
	gmr_outputM=cm.intSliderGrp('g_outputM',field=True, label='Output Mode', minValue=0, maxValue=3, fieldMinValue=0, fieldMaxValue=100, value=0 ,cl3=['right','left','left'],cw3=[80,70,120])
	gmr_oIA_col=cm.columnLayout('g_oIA_col',cat=["left",83],adj=True)
	gmr_OIA=cm.checkBox('g_OIA',l='Occlusion In Alpha')
	cm.setParent('g_faw_col')
	gmr_fallo=cm.floatFieldGrp('g_fallo', l='Falloff', value1=0.5,cl2=['right','left'],cw2=[80,70])
	gmr_idIncl=cm.intFieldGrp('g_idIncl', l='Id Inclexcl', value1=-1,cl2=['right','left'],cw2=[80,70])
	gmr_idNonself=cm.intFieldGrp('g_idNonself', l='Id Nonself', value1=1,cl2=['right','left'],cw2=[80,70])
	cm.separator('g_separ_up', height=10, style='in' )
	gmr_AO_col=cm.columnLayout('g_AO_col',cat=["left",83],adj=True)
	gmr_AO=cm.checkBox('g_AO',l='AO',v=True,onc=lambda *args:openCheckBox('g_WN',45,0.8,25,0,0.5,-1,1,1,0))
	gmr_WN=cm.checkBox('g_WN',l='World Normal',onc=lambda *args:openCheckBox('g_AO',0,0,0,3,1,1,1,1,0))
	cm.setParent('g_faw_col')
	cm.separator('g_separ_down', height=10, style='in' )
	gmr_mAWn=cm.button('g_mAWn',l='Modify AO /worldNormal...',h=30,bgc=[0.3,0.5,0.8],c=lambda *args:getAoAndWnM())
	cm.separator('g_separ_xiadown', height=10, style='in' )

	cm.setParent('g_main_col')
	gmr_zd_f=cm.frameLayout('g_zd_frame',label='Zdepth',cll=True,borderStyle='etchedOut',\
		ec=lambda *args:resizeWindowH('gmr_win','g_aw_frame','g_id_frame',688,362,505,179),\
		cc=lambda *args:resizeWindowH('gmr_win','g_aw_frame','g_id_frame',571,245,388,62))
	gmr_fzd_col=cm.columnLayout('g_fzd_col',cat=["both",3],adj=True)
	gmr_NCP=cm.floatFieldGrp('g_NCP', l='Near Clip Plane', value1=1,cl2=['right','left'],cw2=[120,70])
	gmr_FCP=cm.floatFieldGrp('g_FCP', l='Far Clip Plane', value1=20,cl2=['right','left'],cw2=[120,70])
	gmr_in_col=cm.columnLayout('g_in_col',cat=["left",123],adj=True)
	#gmr_invert=cm.checkBox('g_invert',l='Invert Result',v=True)
	cm.setParent('g_fzd_col')
	cm.separator('g_separ_zd_down', height=25, style='in' )
	gmr_zdepth=cm.button('g_zdepth',l='Modify Zdepth...',h=30,bgc=[0.3,0.5,0.8],c=lambda *args:getZdepthAndM())
	cm.separator('g_separ_zd_xiadown', height=10, style='in' )
	
	cm.setParent('g_main_col')
	gmr_id_f=cm.frameLayout('g_id_frame',label='ID',cll=True,borderStyle='etchedOut',\
		ec=lambda *args:resizeWindowH('gmr_win','g_aw_frame','g_zd_frame',688,360,571,245),\
		cc=lambda *args:resizeWindowH('gmr_win','g_aw_frame','g_zd_frame',505,179,388,62))
	gmr_fid_col=cm.columnLayout('g_fid_col',cat=["both",3],adj=True)
	gmr_asset=cm.colorSliderGrp('g_asset',label='Asset Object ID', rgb=(0, 0, 0) ,cl3=['right','left','left'],cw3=[80,70,120])
	gmr_mat=cm.colorSliderGrp('g_mat',label='Material ID', rgb=(0, 0, 0) ,cl3=['right','left','left'],cw3=[80,70,120])
	gmr_asset_col=cm.columnLayout('g_asset_col',cat=["left",123],adj=True)
	gmr_asset_c=cm.checkBox('g_asset_c',l='AssetID',v=1)
	gmr_mat_c=cm.checkBox('g_mat_c',l='MatID',v=1)
	cm.setParent('g_fid_col')
	cm.separator('g_separ_id_down', height=10, style='in' )
	gmr_id=cm.button('g_id',l='Modify ID...',h=30,bgc=[0.3,0.5,0.8],c=lambda *args:modifyID())
	cm.separator('g_g_separ_id_xiadown', height=10, style='in' )
	gmr_g_asset_col=cm.columnLayout('g_g_asset_col',cat=["left",10],adj=True)
	gmr_g_asset_c=cm.checkBox('g_g_asset_c',l='Reference Level (on: top && off: down)',v=1)
	cm.setParent('g_fid_col')
	gmr_r_id=cm.button('g_r_id',l='Random ID...',h=30,bgc=[0.3,0.5,0.8],c=lambda *args:modifyRandomID())
	cm.separator('g_separ_id_xiadown', height=10, style='in' )
	cm.window('gmr_win',e=True,wh=(320,688))
	cm.showWindow('gmr_win')
def openCheckBox(aoOrWn,samp,spre,maxD,outputM,fallo,idIncl,idNonself,on,off):
	cm.intFieldGrp('g_samp', e=1,value1=samp)
	cm.colorSliderGrp('g_brig',e=1,rgb=[on,on,on])
	cm.colorSliderGrp('g_dark',e=1,rgb=[off,off,off])
	cm.floatFieldGrp('g_spre',e=1,value1=spre)
	cm.floatFieldGrp('g_maxD',e=1,value1=maxD)
	cm.checkBox('g_reflective',e=1,v=off)
	cm.intSliderGrp('g_outputM',e=1,v=outputM)
	cm.checkBox('g_OIA',e=1,v=off)
	cm.floatFieldGrp('g_fallo',e=1,value1=fallo)
	cm.intFieldGrp('g_idIncl',e=1,value1=idIncl)
	cm.intFieldGrp('g_idNonself',e=1,value1=idNonself)
	cm.checkBox(aoOrWn,e=1,v=0)
def getAoAndWnM():
	allaos=cm.ls(type='mib_amb_occlusion')
	if not len(allaos):
		if cm.checkBox('g_AO',q=1,v=1):
			cm.warning('no Ao shaders in your scene!')
		if cm.checkBox('g_WN',q=1,v=1):
			cm.warning('no worldNormal shaders in your scene!')
	else:
		aolist=[]
		wnlist=[]
		for single in allaos:
			outp=cm.listConnections('%s.outValue'%single,s=0,p=1)
			if outp!=None:
				outp=outp[0].split('.')[-1]
#				print outp
				if outp=='ambientOcclusion':
					aolist.append(single)
				if outp=='worldNormal':
					wnlist.append(single)
		if cm.checkBox('g_AO',q=1,v=1) :
			if len(aolist):
				for eachao in aolist:
					print eachao
					modifyAoAndWn(eachao)
				print ' ^_^ all ao shaders modify succeeful.'
			else:
				cm.warning('no Ao shaders in your scene!')
		if cm.checkBox('g_WN',q=1,v=1):
			if len(wnlist):
				for eachwn in wnlist:
					modifyAoAndWn(eachwn)
				print ' ^_^ all worldNormal shaders modify succeeful'
			else:
				cm.warning('no worldNormal shaders in your scene!')
		if cm.checkBox('g_AO',q=1,v=1)==0 and cm.checkBox('g_WN',q=1,v=1)==0:
			cm.warning('please select (AO or World Normal) in this script!')
def modifyAoAndWn(awshader):
	sa=cm.intFieldGrp('g_samp', q=1,value1=1)
	br=cm.colorSliderGrp('g_brig',q=1,rgb=1)
	da=cm.colorSliderGrp('g_dark',q=1,rgb=1)
	sp=cm.floatFieldGrp('g_spre',q=1,value1=1)
	ma=cm.floatFieldGrp('g_maxD',q=1,value1=1)
	re=cm.checkBox('g_reflective',q=1,v=1)
	ou=cm.intSliderGrp('g_outputM',q=1,v=1)
	oi=cm.checkBox('g_OIA',q=1,v=1)
	fa=cm.floatFieldGrp('g_fallo',q=1,value1=1)
	idi=cm.intFieldGrp('g_idIncl',q=1,value1=1)
	idn=cm.intFieldGrp('g_idNonself',q=1,value1=1)
	cm.setAttr('%s.samples'%awshader, sa)
	cm.setAttr('%s.bright'%awshader, br[0],br[1],br[2], type='double3')
	cm.setAttr('%s.dark'%awshader, da[0],da[1],da[2], type='double3')
	cm.setAttr('%s.spread'%awshader, sp)
	cm.setAttr('%s.max_distance'%awshader, ma)
	cm.setAttr('%s.reflective'%awshader, re)
	cm.setAttr('%s.output_mode'%awshader, ou)
	cm.setAttr('%s.occlusion_in_alpha'%awshader, oi)
	cm.setAttr('%s.falloff'%awshader, fa)
	cm.setAttr('%s.id_inclexcl'%awshader, idi)
	cm.setAttr('%s.id_nonself'%awshader, idn)
def getZdepthAndM():
	allZdepths=cm.ls(type='zdepth')
	if not len(allZdepths):
		cm.warning('no zdepth shaders in your scene!')
	else:
		zdlist=[]
		for each in allZdepths:
			ou=cm.listConnections('%s.output'%each,s=0,p=1)
			if ou!=None:
				ou=ou[0].split('.')[-1]
				if ou=='zdepth':
					zdlist.append(each)
		if len(zdlist):
			for singlezd in zdlist:
				modifyZdepth(singlezd)
			print ' ^_^ all zdepth shaders modify succeeful'
		else:
			cm.warning('no zdepth shaders in your scene!')
def modifyZdepth(zdshader):
	ncp=cm.floatFieldGrp('g_NCP',q=1,value1=1)
	fcp=cm.floatFieldGrp('g_FCP',q=1,value1=1)
	#inv=cm.checkBox('g_invert',q=1,v=1)
	cm.setAttr('%s.min_dis'%zdshader,ncp)
	cm.setAttr('%s.max_dis'%zdshader,fcp)
	#cm.setAttr('%s.invert'%zdshader,inv)
def modifyID():
	#sel_mi_blinns=cm.ls(sl=1,type='mi_blinn')
	sel_mi_blinns=cm.ls(sl=1,mat=1)
	if not len(sel_mi_blinns):
		#cm.warning ('no (type:"mi_blinn") were selected!')
		cm.warning ('no shades were selected!')
	else:
		ai=cm.checkBox('g_asset_c',q=1,v=1)
		mi=cm.checkBox('g_mat_c',q=1,v=1)
		ass=cm.colorSliderGrp('g_asset',q=1,rgb=1)
		mat=cm.colorSliderGrp('g_mat',q=1,rgb=1)
		pai=[]
		pmi=[]
		for single in sel_mi_blinns:
			if ai==1:
				if cm.objExists('%s.assetObjectID'%single):
					cm.setAttr('%s.assetObjectID'%single,ass[0],ass[1],ass[2],type='double3')
				pai.append(single)
			if mi==1:
				if cm.objExists('%s.materialID'%single):
					cm.setAttr('%s.materialID'%single,mat[0],mat[1],mat[2],type='double3')
				pmi.append(single)
			if ai==0 and mi==0:
				cm.warning('Please select AssetID or MatID in this script!')
		if len(pai):
			print ' ^_^ Asset Object ID were modify succeeful in you select (type:"mi_blinn")'
		if len(pmi):
			print ' ^_^ Material ID were modify succeeful in you select (type:"mi_blinn")'
#//8.16
def modifyRandomID():
	ai=cm.checkBox('g_asset_c',q=1,v=1)
	mi=cm.checkBox('g_mat_c',q=1,v=1)
	rl=cm.checkBox('g_g_asset_c',q=1,v=1)
	if ai==1:
		if rl==1:
			modifyMi_blinnsAssetObjectID_T()
		else:
			modifyMi_blinnsAssetObjectID_D()
	if mi==1:
		modifyMi_blinnsMaterialID()
	if ai==0 and mi==0:
		cm.warning('Please select AssetID or MatID in this script!')


def deleteDInList(listName=[]):
	midList=[]
	for eachName in listName:
		if not eachName in midList:
			midList.append(eachName)
	return midList
def getAllToreference():
	ToRList=[]
	all_refereces=cm.ls(type='reference')
	if len(all_refereces):
		for x in all_refereces:
			try:
				toReferences=cm.referenceQuery(x,referenceNode=True,topReference=True)
				ToRList.append(toReferences)
			except:
				pass
	if ToRList:
		ToRList=deleteDInList(ToRList)
	return ToRList
def getObjectesFromToreference(Toreference=''):
	allObjectes=cm.referenceQuery(Toreference,nodes=True,dp=True)
	renderObjectes=cm.ls(allObjectes,type=['mesh','subdiv','nurbsSurface'])
	return renderObjectes
def getMi_blinnsFromObjectList(objList=[]):
	all_shader_G=cm.listConnections(objList,s=False,type='shadingEngine')
#	print all_shader_G
	if all_shader_G!=None:
		all_shader_G=deleteDInList(all_shader_G)
		all_mi_blinns=cm.listConnections(all_shader_G,d=False,type='mi_blinn')
		if all_mi_blinns!=None:
			all_mi_blinns=deleteDInList(all_mi_blinns)
	return all_mi_blinns
def modifyMi_blinnsAssetObjectID_T():
	allToreferences=getAllToreference()
	if len(allToreferences):
		for single in allToreferences:
			all_mi_blinns_torefe=[]
			downrefeFtorefe=getDownReferenceForToreference(single)
			for each in downrefeFtorefe:
				try:
					obj=cm.referenceQuery(each,nodes=True,dp=True)
					#some_mi_bl=cm.ls(obj,type='mi_blinn')
					some_mi_bl=cm.ls(obj,mat=True)
					if len(some_mi_bl):
						[all_mi_blinns_torefe.append(s) for s in some_mi_bl]
				except: pass
			if len(all_mi_blinns_torefe):
				randr=random.random()
				randg=random.random()
				randb=random.random()
				for each_mb in all_mi_blinns_torefe:
					if cm.objExists('%s.assetObjectID'%each_mb):
						cm.setAttr('%s.assetObjectID'%each_mb,randr,randg,randb,type='double3')
	else:
		cm.warning('No reference files in the scene!')
def modifyMi_blinnsAssetObjectID_D():
	drf=downReferenceFile()
	if len(drf):
		for each in drf:
			obj=cm.referenceQuery(each,nodes=True,dp=True)
			#mi_blinns=cm.ls(obj,type='mi_blinn')
			mi_blinns=cm.ls(obj,mat=True)
			if len(mi_blinns):
				randr=random.random()
				randg=random.random()
				randb=random.random()
				for single in mi_blinns:
					if cm.objExists('%s.assetObjectID'%single):
						cm.setAttr('%s.assetObjectID'%single,randr,randg,randb,type='double3')
	else:
		cm.warning('No reference files in the scene!')
def modifyMi_blinnsMaterialID():
	all_mi_blinns=cm.ls(mat=1)
	if len(all_mi_blinns):
		for each in all_mi_blinns:
			if cm.objExists('%s.materialID'%each):
				cm.setAttr('%s.materialID'%each,random.random(),random.random(),random.random(),type='double3')
	else:
		cm.warning('No shades in the scene!')
#//8.17
def downReferenceFile():
	downReferencefiles=[]
	all_referencefiles=cm.ls(type='reference')
	if len(all_referencefiles):
		for single in all_referencefiles:
			try:
				i=0
				all_members=cm.referenceQuery(single, nodes=True,dp=True)
				for s_member in all_members:
					if cm.nodeType(s_member)=='reference':
						i+=1
						break
				if i==0:
					downReferencefiles.append(single)
			except:pass
	return downReferencefiles
#//8.18
def getDownReferenceForToreference(toreference=''):
	m=[]
	nextrefer=getnextReferencefile(toreference)
	if not len(nextrefer):
		m.append(toreference)
	else:
		j=1
		while j:
			for single in nextrefer:
				if not len(getnextReferencefile(single)):
					m.append(single)
			nextrefer=getAllnextReferencefile(nextrefer)
			if not len(nextrefer):
				break
	return m
def getAllnextReferencefile(alluprefer=[]):
	mlist=[]
	for single in alluprefer:
		sup=getnextReferencefile(single)
		if len(sup):
			[mlist.append(s) for s in sup]
	return mlist
def getnextReferencefile(upreference):
	m=[]
	try:
		all=cm.referenceQuery(upreference,nodes=True,dp=True)
		[m.append(s) for s in all if cm.nodeType(s)=='reference']
	except: pass
	return m

def resizeWindowH(windowName,fNameO,fNameT,hSizeO,hSizeT,hSizeS,hSizeTh):
	Fo_cll=not cm.frameLayout(fNameO,q=1,cl=1)
	Ft_cll=not cm.frameLayout(fNameT,q=1,cl=1)
	print Fo_cll,Ft_cll
	if Fo_cll==1 and Ft_cll==1:
		cm.window(windowName,e=1,h=hSizeO)
	if Fo_cll==0 and Ft_cll==1:
		cm.window(windowName,e=1,h=hSizeT)
	if Fo_cll==1 and Ft_cll==0:
		cm.window(windowName,e=1,h=hSizeS)
	if Fo_cll==0 and Ft_cll==0:
		cm.window(windowName,e=1,h=hSizeTh)
if __name__=='__main__':
	globalModify_reference_ui()