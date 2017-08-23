# -*- Coding: Utf-8 -*- 
# coding=gbk

#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

#工具名字 ："Output Pass Tool"
#书写时间 ：2011 . 7 - 2012 . 9
#作      者 ：郑卫福
#版      本 ：V1.0
#电子邮件 ：651999307@qq.com
#maya版本 ：V2012-x64

#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

#使用方法：
#		1. 拷贝"Output_Pass_Tool_new.py"到"...\Documents\maya\2012-x64\scripts"(或者python可以调用的路径下面)。
#		2. 场景使用的材质是mi_blinn。
#		3. 打开maya2012。
#		4. 进入script Editor,python模块(编写 from Output_Pass_Tool_new import * ;call_OutputRenderPasses())。

#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
from __future__ import division
import maya.cmds as cmds 
import maya.mel as mel
import os
class CreateOutputRenderPasses:
	def __init__(self):
		fileInfoDate=cmds.fileInfo('zwfOutputRenderpassFileInfoDatas',q=True)
		if len(fileInfoDate):
			self.zwfOutputRenderpassControlDatas=eval(fileInfoDate[0])
		else:
			self.zwfOutputRenderpassControlDatas={}
	def saveOutputRenderpassControlDatas(self,*args):
		cmds.fileInfo('zwfOutputRenderpassFileInfoDatas',str(self.zwfOutputRenderpassControlDatas))
	def create_opt_ui(self):
		mr=cmds.pluginInfo("Mayatomr", q=True, l=True)
		if not mr:
			cmds.loadPlugin("Mayatomr")
			cmds.confirmDialog( title='load mr_V2', message='++++++"Mayatomr" was loaded,please Try again.++++++',b='colse')
			return 
		if cmds.window('output_pass_ui_V2',ex=True):
			cmds.deleteUI('output_pass_ui_V2')
		c_window=cmds.window('output_pass_ui_V2',t='Output Pass Tool V2.0',wh=(640,95))
		#main_col=cmds.columnLayout(adj=True)
		mainform=cmds.formLayout(nd=100)
		mainscrollLayout=cmds.scrollLayout(cr=True)
		tabs= cmds.tabLayout('main_tabs_V2',innerMarginWidth=5, innerMarginHeight=5,h=922)
		main_mainscrollLayout=cmds.scrollLayout(cr=True)
		m_c=cmds.columnLayout('main_col_V2',cat=["both",3],adj=True)
		rp_f=cmds.frameLayout('rp_frame_V2',label='RenderLayer & AddLightPass',cll=True,borderStyle='etchedOut')
		m_rf=cmds.rowLayout('m_r_V2',nc=3, cw3=(280,15,280), adjustableColumn=3, columnAlign=(1, 'both'), columnAttach=[(1, 'both', 0), (2, 'both', 0), (3, 'both', 0)] )
		m_f=cmds.frameLayout('main_frame_V2',label='RenderLayer',borderStyle='etchedOut')
		f_c=cmds.columnLayout('frame_col_V2',cat=["both",5],adj=True)
		render_layer=cmds.textFieldGrp('renderln_V2',l='renderLayerName:',text='',cl2=['left','left'],cw2=[90,150])
		render_itsl=cmds.textScrollList('ritsl_V2',allowMultiSelection=True,append=self.getAllRenderLayers(),sc=self.selectrenderLayer_C,h=100)
		c_rl=cmds.rowLayout('c_r_V2',nc=3, cw3=(90,90,90), adjustableColumn=3, columnAlign=(3, 'both'), columnAttach=[(1, 'both', 0), (2, 'both', 0), (3, 'both', 0)] )
		b1=cmds.button('c_b_V2',l='create',c=self.createRenderLayers)
		#b2=cmds.button('d_b',l='duplicate')
		b3=cmds.button('de_b_V2',l='delete',c=self.del_Renderlayer)
		b4=cmds.button('re_b_V2',l='rename',c=self.renameRenderLayer)
		
		cmds.setParent('m_r_V2')
		tt=cmds.text('t_name_V2',l='=>')
		s_f=cmds.frameLayout('sec_frame_V2',label='AddLightPass', borderStyle='etchedOut')
		sf_c=cmds.columnLayout('sec_frame_col_V2',cat=["both",5],adj=True)
		passcontributioncap=cmds.textFieldGrp('pass_cm_V2',l='        LightpassName:',text='',cl2=['left','left'],cw2=[105,146],en=False)
		pass_itsl=cmds.textScrollList('pitsl_V2',allowMultiSelection=True,sc=self.selectAddlightPass_C,h=100)
		c_rl_pcm=cmds.rowLayout('c_rpcm_V2',nc=3, cw3=(90,90,90), adjustableColumn=3, columnAlign=(3, 'both'), columnAttach=[(1, 'both', 0), (2, 'both', 0), (3, 'both', 0)] )
		b11=cmds.button('c_bbb_V2',l='create', c=self.createAddLightPass,en=False)
		b33=cmds.button('de_bbb_V2',l='delete',c=self.del_addlightPass,en=False)
		b44=cmds.button('re_bbb_V2',l='rename',c=self.renameLightPass,en=False)
		#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
		
		cmds.setParent('main_col_V2')
		cmds.separator('s_o_V2', height=10, style='in' )
		men_f=cmds.frameLayout('men_frame_V2',label='Members ( renderLayer & AddLightPass )',cll=True,borderStyle='etchedOut')
		men_rf=cmds.rowLayout('men_r_V2',nc=3, cw3=(290,30,270), adjustableColumn=2, columnAlign=(1, 'both'), columnAttach=[(1, 'both', 0), (2, 'both', 0), (3, 'both', 0)] )
		menmber_f=cmds.frameLayout('menmber_frame_V2',label='members ( renderLayer )',borderStyle='etchedOut',)
		f_men_c=cmds.columnLayout('frame_men_col_V2',cat=["both",5],adj=True)
		m_render_itsl=cmds.textScrollList('m_ritsl_V2',allowMultiSelection=True,sc=lambda *args:self.selectMembers_C("m_ritsl_V2"),h=200)
		m_rr=cmds.rowLayout('men_rr_V2',nc=2, cw=(120,10), adjustableColumn=2, columnAlign=(1, 'both'), columnAttach=[(1, 'both', 0), (2, 'both', 0)])
		b6=cmds.button('ar_b_V2',l='Add selectes [RL]',c=self.addSelectToRenderLayer,w=130)
		b7=cmds.button('rr_b_V2',l='Remove [RL]',c=self.removeSelectToRenderLayer)
		cmds.setParent('frame_men_col_V2')
		cmds.button('checkSameinDifLayer_b_V2',l=u'检查("mesh","subdiv","nurbsSurface")是否在其它层',c=self.checkSameobjInDiffRenderLayer)
		
		cmds.setParent('men_r_V2')
		menp_f=cmds.frameLayout('menp_frame_V2',label='lights ( AddLightPass )', borderStyle='etchedOut')
		menp_c=cmds.columnLayout('menp_frame_col_V2',cat=["both",5],adj=True)
		menp_itsl=cmds.textScrollList('menp_itsl_V2',allowMultiSelection=True,sc=lambda *args:self.selectMembers_C("menp_itsl_V2"),h=223)
		m_pr=cmds.rowLayout('men_rr_V2',nc=2, cw=(120,10), adjustableColumn=2, columnAlign=(1, 'both'), columnAttach=[(1, 'both', 0), (2, 'both', 0)])
		b8=cmds.button('ap_b_V2',l='Add lights ',c=self.addSelectToAddLightPass,w=130)
		b9=cmds.button('rp_b_V2',l='Remove ',c=self.removeSelectToAddLightPass)
		#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
		
		cmds.setParent('main_col_V2')
		cmds.separator('s_T_V2', height=10, style='in' )
		rb_f=cmds.frameLayout('rb_frame_V2',label='Render & Buffer',cll=True,borderStyle='etchedOut')
		cmds.columnLayout('rb_column_V2',adj=True)
		rbnn=cmds.rowLayout('rbnn_r_V2',nc=5, cw5=(80,50,120,230,80), adjustableColumn=4, columnAlign=(1, 'both'), columnAttach=[(1, 'both', 5), (2, 'both',-6), (3, 'both',5),(4, 'both',5),(5, 'both',5)] )
		cmds.text('buffername_t_V2',l='Buffer Name:', en=False)
		Qz=cmds.textField('qz_V2',tx='',en=False)
		b_n=cmds.textField('buffername_V2',text='', cc=self.renameRenderPassName,en=False)
		D_T=cmds.optionMenu('datetype_V2', label='Date Type',cc=self.dataType_C,en=False)
		cmds.menuItem('mi_o_V2', label='8-bit Integer (unsigned)')
		cmds.menuItem('mi_t_V2', label='16-bit Integer (unsigned)')
		cmds.menuItem( 'mi_th_V2', label='16-bit Float' )
		cmds.menuItem( 'mi_f_V2', label='32-bit Float' )
		pre=cmds.button('presets_V2',l='Presets')
		prepop=cmds.popupMenu('pre_popupI_V2',pmc=self.updatepopupMenu,button=1)
		self.addpopupMenu()

		cmds.setParent('rb_column_V2')
		cmds.separator('s_F_V2', height=10, style='in' )
		rb_rf=cmds.rowLayout('rb_r_V2',nc=3, cw3=(140,30,400), adjustableColumn=3, columnAlign=(1, 'both'), columnAttach=[(1, 'both', 0), (2, 'both', 0), (3, 'both', 0)] )
		rbb_f=cmds.frameLayout('rbb_frame_V2',label='Presets',borderStyle='etchedOut')
		rb_men_c=cmds.columnLayout('rb_men_col_V2',cat=["both",5],adj=True)
		rb_itsl=cmds.textScrollList('rb_ritsl_V2',allowMultiSelection=True,\
		append=['Color','DiffuseColor','Light','Indirect','Specular','AmbientColor','Incandescence','SSS','Reflection','Refraction',
		'GlowSource','VolumeLight','VolumeObject','VolumeScene',
		'AddSpecular','AddReflection','AO','WorldNormal','Zdepth','FacingRatio','MV','AssetObjectID','MaterialID'],h=180)
		
		cmds.setParent('rb_r_V2')
		cmds.columnLayout('>>><<<<_V2',adj=True)
		bb1=cmds.button('gb_V2',l='>>>',c=self.addRenderpass,h=80)
		cmds.separator('s_Th_V2', height=10, style='in' )
		bb2=cmds.button('ib_V2',l='<<<', c=self.deleteRenderpass,h=85)
		
		cmds.setParent('rb_r_V2')
		rrbb_f=cmds.frameLayout('rrbb_frame_V2',label='Render', borderStyle='etchedOut')
		rrbb_c=cmds.columnLayout('rrbb_frame_col_V2',cat=["both",5],adj=True)
		rrbb_itsl=cmds.textScrollList('rrbb_itsl_V2',allowMultiSelection=True,sc=self.renderTextScrollList_C, h=180)
		#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
		
		cmds.setParent('main_col_V2')
		cmds.separator('s_link_V2', height=10, style='in' )
		link_f=cmds.frameLayout('link_frame_V2',label='RenderLayer Links',cll=True,borderStyle='etchedOut')
		link_rf=cmds.rowLayout('link_r_V2',nc=2, cw2=(100,350), adjustableColumn=2, columnAlign=(1, 'both'), columnAttach=[(1, 'both', 0), (2, 'both', 5)] )
		linkL_f=cmds.frameLayout('linkL_frame_V2',label='Link Type',borderStyle='etchedOut')
		linkL_c=cmds.columnLayout('linkL_col_V2',cat=["both",5],adj=True)
		linkL_itsl=cmds.textScrollList('linkL_ritsl_V2',allowMultiSelection=False, append = [ 'Reflection','Refraction','Shadow','Matte'],sc=self.seleceLinkType_C, h=70)
		
		cmds.setParent('link_r_V2')
		linkR_f=cmds.frameLayout('linkR_frame_V2',label='RenderLayer(not selected)', borderStyle='etchedOut')
		linkR_c=cmds.columnLayout('linkR_frame_col_V2',cat=["both",5],adj=True)
		linkRR_itsl=cmds.textScrollList('linkR_itsl_V2',allowMultiSelection=True,sc=self.setUpAndBreakLinks,h=70)
		allRL=self.getAllRenderLayers_exc()
		if len(allRL):
			cmds.textScrollList('linkR_itsl_V2',e=True,append=allRL)
		#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
		cmds.setParent('main_col_V2')
		cmds.separator('s_mask_V2', height=10, style='in' )
		cmds.frameLayout('mask_frame_V2',label='Mask Matte',cll=True,cl=True,borderStyle='etchedOut')
		check_col=cmds.columnLayout('c_col_V2',cat=["both",3],adj=True)
		cmds.text('note_o_V2',l='  ! Note: 1. 请执行下面的操作前先保存你的场景。', align='left',bgc=[1,0.3,0.2],h=20)
		cmds.text('note_T_V2',l='              2. 请保证需要创建 "matteMask" 的渲染层中没有相同物体("mesh","subdiv","nurbsSurface")。', align='left',bgc=[1,0.3,0.2],h=20)
		cmds.setParent('mask_frame_V2')
#		cmds.separator('s_note', height=10, style='in' )
		mask_rowl=cmds.rowLayout('m_rowl_V2',nc=2, cw2=(350,180), adjustableColumn=2, columnAlign=(1, 'both'), columnAttach=[(1, 'both', 0), (2, 'both', 0)] )
		mask_tfg=cmds.textFieldGrp('matteMask_V2',l='MatteMask_SceneName:',text='matteMask',cl2=['left','left'],cw2=[120,220])
		create_m=cmds.button('create_mask_V2',l='CreateMaskPass...',c=self.createMatteMask)
		#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#		cmds.setParent('main_col_V2')
#		cmds.separator('s_end', height=5, style='in' )
		cmds.setParent(tabs)
		Modify_mainscrollLayout=cmds.scrollLayout(cr=True)
		Modify_col=cmds.columnLayout(adj=True,cat=['both',2],rs=5)
		Modify_other_b=cmds.button(l=u'打开其他全局修改面板...',c='import Global_ModifyShaders as GMS; GMS.globalModify_reference_ui()',h=30)
		Modify_usedLambert_b=cmds.button(l=u'检查使用lambert1或者没有材质的物体（符合条件的物体将高亮显示）...',c=self.getobjsAssLambertOrNoshader,h=30)
		Modify_renderPass_f=cmds.frameLayout(label='RenderPassModify',cll=True,borderStyle='etchedOut')
		Modify_renderPass_col=cmds.columnLayout(adj=True,cat=['both',2],rs=5)
		Modify_renderPass_on_b=cmds.button(l='All RenderPasses On ...',c=lambda *args : self.renderPassesOnOrOff(1))
		Modify_renderPass_on_b=cmds.button(l='All RenderPasses Off ...',c=lambda *args : self.renderPassesOnOrOff(0))
		Modify_renderPass_connection_b=cmds.button(l='Connection Relationship (Id and transparent)...',c=self.IDAndTransparentConnectionRelationship)
		Modify_renderPass_break_b=cmds.button(l='Break Relationship (Id and transparent)...',c=self.IDAndTransparentBreakRelationship)
		Modify_renderPass_check_b=cmds.button(l=u'Delete Unused RenderPasses (使用前必须单击“Create...”)...',c=self.deleteUnusedrenderPasses)
		cmds.setParent(Modify_col)
		Modify_picoutput_f=cmds.frameLayout(label='Picture Output Folder',cll=True,borderStyle='etchedOut')
		Modify_picoutput_col=cmds.columnLayout(adj=True,cat=['both',2],rs=5)
		self.Modify_picoutput_text_ts=cmds.text(l='renderOutput : ',al='left',h=30,fn="obliqueLabelFont")
		self.Modify_picoutput_cb=cmds.checkBox(l='Renderpass',v=True)
		self.Modify_picoutput_outputkey=cmds.textFieldButtonGrp( label='Output key:', text='<RenderLayer>', buttonLabel='   set...   ',cl3=['left','left','left'],cw3=[60,250,60],bc=self.pic_outPut)
		cmds.setParent(tabs)
		Help_mainscrollLayout=cmds.scrollLayout(cr=True)
		Help_col=cmds.columnLayout('help_c_V2',adj=True,cat=['both',2],rs=5)
		includHelp='''
工作描述：\n                                                          
    1.分层插件，根据添加的渲染层输出各种renderPasses("Color";"DiffuseColor"; "Light";"Indirect";"Specular";"AmbienColor";"Incandescence";"SSS";"Reflection";"Refration ";"AddSpecular";"AddReflection";"AO";"WorldNormal";"Zdepth";"FacingRatio";"MV";"AssetObjectID";"MaterialID")，方便后期合成。\n
    2.本套插件是先操作后用create...按钮执行。\n\n
................................................................................\n\n
使用方法：\n
    1. 创建渲染层，在场景选择您需要添加的物体和灯光，在“renderLayerName：”中填入该渲染层的名字并且单击相应的create 按钮创建。\n
    2. 删除渲染层，在RenderLayer列表中选中您需要删除的渲染层(除“defaultRenderLayer”)并且单击相应的delete按钮删除。\n
    3. 渲染层重命名，在RenderLayer列表中选中您需要重命名的渲染层(除“defaultRenderLayer”)并且单击相应的rename按钮重命名。\n
    4. 添加lightpasses for renderLayer，在RenderLayer列表中选中您需要操作的渲染层(除“defaultRenderLayer”)并在该渲染层选中您需要输出的灯光，在LightpassName：中填入该pass的名字单击相应的create按钮添加。\n
    5. 删除lightpasses，在AddLightPass列表中选中您需要删除的lightpass并且单击相应的delete按钮删除。\n
    6. 渲染层重命名，在AddLightPass列表中选中您需要重命名的lightpass并且单击相应的rename按钮重命名。\n
    7. 在渲染层中添加物体，在RendLayer列表中选中渲染层(除“defaultRenderLayer”)，在场景选择您需要添加的物体单击Add selectes [RL]按钮添加。\n
    8. 在渲染层中删除物体，在RendLayer列表中选中渲染层(除“defaultRenderLayer”)，在场景或者在members（renderlayer）列表中选中您需要删除的物体，单击Remove[RL]按钮删除。\n
    9. 检查(“mesh”，“subdiv”，“nurbsSurface”)是否在其他渲染层，在RendLayer列表中选中一个渲染层(除“defaultRenderLayer”)，单击检查(“mesh”，“subdiv”，“nurbsSurface”)是否在其它层 按钮检测，如果按钮成红色说明在其它层中存在相同的物体并且在members(renderLayer)中以“！”为首作为标记，如果按钮成绿色说明在其它层中不存在相同的物体。(如果RendLayer列表中除“defaultRenderLayer”)外只有一个渲染层不需要执行此操作。\n
    10.在AddLightPass中选择lightpass，在场景中选择灯光并且单击Add lights按钮添加。\n
    11.在AddLightPass中选择lightpass，在lights（AddLightPassr）列表中选中灯光并且单击delete按钮删除。\n
    12.添加renderPasses，在RenderLayer列表中选择渲染层（除“defaultRenderLayer”）并在Presets列表中选择您需要的renderPasses并单击>>>按钮添加（在Render列表中列出相应的renderpass）。\n
    13.删除renderPasses，在RenderLayer列表中选择渲染层（除“defaultRenderLayer”）并在Render列表中选择您需要删除的renderPass单击<<<按钮删除（在Render列表中减掉相应的renderpass）。\n
    14.重命名renderPass，在RenderLayer列表中选择渲染层（除“defaultRenderLayer”）并在Render列表中选择您需要重命名的-个renderPass，在Buffer Name：中新的名字并按回车键执行（在Render列表的renderpass会改变）。\n
    15.修改DateType，在RenderLayer列表中选择渲染层（除“defaultRenderLayer”）并在Render列表中选择您需要修改renderPasses，在Data Type中选择相应的dataType修改（在Render列表的renderpass会改变）。\n
    16.保存renderpasses预设，在Presets列表中选择您需要的renderPasses，单击preset按钮，在弹出的菜单中单击Save RenderPass Preset...。弹出一个窗口，在Preset name：中填入名字并单击Save RenderPass Preset按钮保存。\n
    17.删除renderpasses预设，单击preset按钮，在弹出的菜单中单击Edit Presets...。弹出一个窗口，在列表中选择预设并单击Delete按钮删除。\n
    18.将renderpasses预设执行，在RenderLayer列表中选择渲染层（除“defaultRenderLayer”），单击preset按钮，在弹出的菜单中单击之前保存预设执行。\n
    19.渲染层之间添加和打断Link（Reflection,Refraction,Shadow），在RenderLayer列表中选择一个渲染层（除“defaultRenderLayer”），在Link Type列表中选择link方式同时在RenderLayer(not selected)列表中选择需要与之前选择的渲染层产生关系的渲染层(选择多个按住shift键，打断按住ctrl键)。\n
    20.执行以上所有的操作之后都需要单击Create...按钮生效。\n
    21.当修改了上面操作，没有单击Create...按钮，可以单击Save Setings按钮保存以上的数据（当重新打开Output Pass Tool工具时上面的数据会保存，不然显示不正确）。\n
    22.当上面操作显示不正确，单击Reset Setings按钮清除以上的操作回到原始。\n
    23.创建遮罩关系层（可选），当渲染层个数大于1并且它们之间存在遮挡关系时需要创建该层。创建相应Matte关系，在MatteMask_SceneName:中填写保存文件的名字并单击CreateMaskPass...按钮执行。\n
    24.使用“打开其他全局修改面板”可以打开一个全局修改的面板。\n
    25.使用“检查使用lambert1或者没有材质的物体”，可以将符合物体高亮显示。\n
    26.使用“All RenderPasses On”和“All RenderPasses Off”按钮能打开和关闭场景中所有的renderPasses渲染功能。\n
    27.使用“Connection Relationship (Id and transparent)”和“Break Relationship (Id and transparent)”按钮能连接和打断Id与半透明的关系（半透明指材质“transparent”属性后面没有连接贴图）。\n
    28.使用“Delete Unused Renderpasses”按钮可以删除场景没有使用的renderPasses。\n
    29.设置渲染输出贴片所在的文件夹，如果场景中有渲染层和renderpass，使用预设参数直接单击set按钮执行；如果场景中有渲染层没有renderpass，去的“Renderpass”上的勾，单击set按钮执行；如果如果场景中没有渲染层也没有renderpass，去的“Renderpass”上的勾，在Out key：中填入您所需的名字，单击set按钮执行。\n\n
................................................................................\n\n
注意事项：\n
    1.如果场景中的物体(“mesh”，“subdiv”，“nurbsSurface”，“light”)重命名了，所有的操作需要重新制作。\n
    2.同个物体(“mesh”，“subdiv”，“nurbsSurface”)不能在不同的渲染层中出现。（单击检查(“mesh”，“subdiv”，“nurbsSurface”)是否在其它层 按钮检测）。\n 
    3.场景中所有的物体的材质不能是“lambert1”（用 “检查使用lambert1或者没有材质的物体”按钮检查 ）。\n
    4.使用“Delete Unused Renderpasses”前必须先使用“Create...”按钮创建。\n
    5.对所有渲染层的操作（“delete”,“rename”,“addObjs”,“removeObjs”等等）只能用该脚本提供的工具。\n
'''
		Help_scroll_descr=cmds.scrollField(ww=True,editable=False,text=includHelp,h=750)
		
		cmds.setParent(Help_col)
		Help_frame_about=cmds.frameLayout(label=u'关于“Output Pass Tool” ',borderStyle='in')
		cmds.text(l=u'   工具名字 :                              Output Pass Tool',align='left')
		cmds.text(l=u'   更新时间 :                              2011 年 12 月',align='left')
		cmds.text(l=u'   作者 :                                     郑卫福',align='left')
		cmds.text(l=u'   版本 :                                     v2.0',align='left')
		cmds.text(l=u'   电子邮箱 :                              651999307@qq.com',align='left')
		cmds.text(l=u'   maya版本 :                             maya2011以上',align='left')
		cmds.tabLayout('main_tabs_V2',e=True,tl=((main_mainscrollLayout,'Main Function'),(Modify_mainscrollLayout,'Modify Function'),(Help_mainscrollLayout,'Help')),psc=self.setButton)

#		cmds.setParent(mainscrollLayout)

		cmds.setParent(mainform)
#		cmds.rowLayout('create_rowl_V2',nc=4, cw4=(150,150,150,150), adjustableColumn=4, columnAlign=(1, 'both'), columnAttach=[(1, 'both', 0), (2, 'both', 0),(3, 'both', 0), (4, 'both', 0)] )
		self.cBox=cmds.checkBox(l='Calculation of the bump( or normal ) effect for " facingRatio " , " worldNormal " , " AO " .',v=True)
		create_pass=cmds.button('create_pass_b_V2',l='Create...',c=self.createSetings,h=30)
		save_presets=cmds.button('save_presets_b_V2',l='Save Setings',c=self.saveOutputRenderpassControlDatas,h=30)
		reset_presets=cmds.button('reset_presets_b_V2',l='Reset Setings',c=self.resetSetings,h=30)
		close_b=cmds.button(l='Close',c=self.delete_winUI,h=30)

		cmds.formLayout(mainform,e=True,af=[(mainscrollLayout,'top',5),(mainscrollLayout,'left',5),(mainscrollLayout,'right',5),(mainscrollLayout,'bottom',60),
									(self.cBox,'left',5),(self.cBox,'bottom',40),
									('create_pass_b_V2','left',5),('create_pass_b_V2','bottom',5),
									(close_b,'right',5),(close_b,'bottom',5),
									('save_presets_b_V2','bottom',5),('reset_presets_b_V2','bottom',5)],
								ac=[('save_presets_b_V2','left',5,'create_pass_b_V2'),('save_presets_b_V2','right',5,'reset_presets_b_V2'),('reset_presets_b_V2','right',5,close_b)],
								ap=[('create_pass_b_V2','right',0,25),('reset_presets_b_V2','left',0,50),(close_b,'left',0,75)])

		cmds.window('output_pass_ui_V2',e=True, wh=(640,995))
		cmds.showWindow('output_pass_ui_V2')
		mel.eval('unifiedRenderGlobalsWindow')
		mel.eval('setCurrentRenderer("mentalRay")')
	def delete_winUI(self,*args):
		cmds.deleteUI('output_pass_ui_V2')
	def setButton(self,*args):
		num=cmds.tabLayout('main_tabs_V2',q=True, sti=True)
		if num==1:
			cmds.button('create_pass_b_V2',e=True,en=True)
			cmds.button('save_presets_b_V2',e=True,en=True)
			cmds.checkBox(self.cBox,e=True,en=True)
			cmds.button('reset_presets_b_V2',e=True,en=True)
		if num==2 or num==3:
			cmds.button('create_pass_b_V2',e=True,en=False)
			cmds.button('save_presets_b_V2',e=True,en=False)
			cmds.button('reset_presets_b_V2',e=True,en=False)
			cmds.checkBox(self.cBox,e=True,en=False)
	def resetSetings(self,*args):
		self.BeforeCreateSetingsdeleteAll()
		self.deleteIntermediateObjects()
		cmds.fileInfo(rm='zwfOutputRenderpassFileInfoDatas')
		self.zwfOutputRenderpassControlDatas={}
		self.create_opt_ui()
	def getsceneName(self):
		sceneName=cmds.file(q=True,sn=True)
		return sceneName
	def selectObj(self):
		seletcted=cmds.ls(sl=True,type='transform')
		return seletcted
	def getAllRenderLayers_exc(self):
		allrenderLayers_exc=self.zwfOutputRenderpassControlDatas.keys()
		return allrenderLayers_exc
	def getAllRenderLayers(self):
		allrenderLayers=self.getAllRenderLayers_exc()
		allrenderLayers.append('defaultRenderLayer')
		return allrenderLayers
	def switchToChannelbox(self):
		aeb=mel.eval('iconTextCheckBox  -q -value $gAttributeEditorButton')
		tsb=mel.eval('iconTextCheckBox  -q -value $gToolSettingsButton')
		cclb=mel.eval('iconTextCheckBox  -q -value $gChannelsOrChannelsLayersButton')
		if aeb:
			mel.eval('ToggleAttributeEditor')
		if tsb:
			mel.eval('ToggleToolSettings')
		if not cclb:
			mel.eval('ToggleChannelsLayers')
	def getType(self,obj):
		obj_allc=cmds.listRelatives(obj,ad=True,pa=True)
		if obj_allc!=None:
			obj_allL=cmds.listRelatives(obj,ad=True,type='light',pa=True)
			if obj_allL==None:
				outType='Object'
			else:
				obj_allo=cmds.listRelatives(obj,ad=True,type=('mesh','subdiv','nurbsSurface'),pa=True)
				if obj_allo==None:
					outType='Light'
				else:
					outType='Object(Light)'
		else:
			outType='Null'
		return outType

	def gaiBianBuJuInMenber(self,layername,type,obj):
		newobj='%s : [%s : %s]'%(layername,type,obj)
		return newobj

	def fromMyMust(self,objectNameInScr):
		newobjectNameInScr=objectNameInScr.split(' : ')[-1][:-1]
		return newobjectNameInScr
	def selectMembers_C(self,textsc_nn=''):
		sel_member_RL=cmds.textScrollList(textsc_nn,q=True,si=True)
		cmds.select(cmds.ls(type='transform'),d=True)
		if sel_member_RL!=None:
			sel_objs=[]
			for single in sel_member_RL:
				single=self.fromMyMust(single)
				sel_objs.append(single)
			cmds.select(sel_objs)
	def removeItem(self,oldlist,reItem):
		midlist=[]
		for i in oldlist:
			if i!=reItem:
				midlist.append(i)
		return midlist 
	def getobjFromRenderLayer(self,OBJL,Type):
		listobjs=[]
		renderlayerobjs=cmds.listRelatives(cmds.listRelatives(OBJL, ad=True, type=Type, pa=True),p=True,type='transform',pa=True)
		if renderlayerobjs!=None:
			renderlayerobjs=self.deleteDInList(renderlayerobjs)
			[listobjs.append(single) for single in renderlayerobjs]
		return listobjs
	def getAnotherRenderLayer(self,renderlayer=''):
		anotherLayers=[]
		all_renderLayers=self.getAllRenderLayers_exc()
		[anotherLayers.append(single) for single in all_renderLayers if single!=renderlayer]
		return anotherLayers

	def checksameobjtolayers(self,renderlayer,obj):
		newobj=obj
		anotherLayers=self.getAnotherRenderLayer(renderlayer)
		if anotherLayers!=[]:
			all_objshapes=cmds.listRelatives(obj,ad=True,pa=True,type=('mesh','subdiv','nurbsSurface'))
			if all_objshapes:
				all_objshapes=self.getNewObjshapesList(all_objshapes)
			if all_objshapes:
				j=0
				for single in anotherLayers:
					t_layer=self.zwfOutputRenderpassControlDatas[single]['AllObjects']
					t_layer=cmds.listRelatives(t_layer,ad=True,pa=True,type=('mesh','subdiv','nurbsSurface'))
					if t_layer:
						t_layer=self.getNewObjshapesList(t_layer)
					if t_layer:
						for i in all_objshapes:
							if i in t_layer:
								j+=1
								newobj=' ! %s'%obj
								break
						if j!=0:
							break
		return newobj
#=========================================================================================检查(“mesh”,”subdiv”,”nurbsSurface”)是否在其它层===============================================================
	def checkSameobjInDiffRenderLayer(self,*args):
		sel_renderLN=cmds.textScrollList('ritsl_V2',q=True,si=True)
		if sel_renderLN!=None:
			if len(sel_renderLN)==1:
				renderlayer=sel_renderLN[0]
				if renderlayer=='defaultRenderLayer':
					return cmds.warning('"defaultRenderLayer" can not check!!!')
				objects=self.zwfOutputRenderpassControlDatas[renderlayer]['MemberObjects']
				layersize=len(objects)
				if layersize:
					i=0
					amount=0
					cmds.progressWindow(title='create progress',progress=0,status='Sleeping: 0%',isInterruptable=True )
					for single in objects:
						if cmds.progressWindow( query=True, isCancelled=True ) :
							break
						partsingle=self.fromMyMust(single)
						objsingle=self.checksameobjtolayers(renderlayer,partsingle)
						if objsingle[:3]==' ! ':
							i+=1
							newsingle=' ! '+single
							cmds.textScrollList('m_ritsl_V2',e=True,ri=single)
							cmds.textScrollList('m_ritsl_V2',e=True,ap=[1,newsingle])
						amount+=100/layersize
						amountInt=int(amount)
						cmds.progressWindow( edit=True, progress=amount, status=('Sleeping: ' + `amountInt` + '%' ) )
					if i==0:
						cmds.button('checkSameinDifLayer_b_V2',e=True,bgc=[0,1,0])
					else:
						cmds.button('checkSameinDifLayer_b_V2',e=True,bgc=[1,0,0])
					cmds.progressWindow( edit=True, progress=100, status=('Sleeping: 100%' ) )
					cmds.progressWindow(endProgress=1)
				else:
					cmds.warning('No objects in %s.'%renderlayer)
			else:
				cmds.warning('plase select one in RenderLayer textScrollList.')
		else:
			cmds.warning('no selected in RenderLayer textScrollList.')
#=========================================================================================渲染层部分===================================================================================================
	def createRenderLayers(self,*args):
		renderLayerName=cmds.textFieldGrp('renderln_V2',q=True,tx=True)
		if not len(renderLayerName):
			cmds.warning( "No words in renderLayerName:" )
		else:
			objs=self.selectObj()
			if objs==[]:
				return cmds.warning( "No selected" )
			cmds.waitCursor( state=True )
			renderL=cmds.createRenderLayer(name=renderLayerName, number=True, empty=True)
			cmds.editRenderLayerMembers(renderL,objs,nr=True)
			pns_objs=self.getobjFromRenderLayer(objs,['mesh','subdiv','nurbsSurface'])
			light_objs=self.getobjFromRenderLayer(objs,'light')
			self.zwfOutputRenderpassControlDatas[renderL]={}
			self.zwfOutputRenderpassControlDatas[renderL]['AllObjects']=objs
			if len(pns_objs):
				self.zwfOutputRenderpassControlDatas[renderL]['PNSObjects']=pns_objs
			if len(light_objs):
				self.zwfOutputRenderpassControlDatas[renderL]['LIGHTObjects']=light_objs
			layermembers=[]
			for single in objs:
				typ=self.getType(single)
				single=self.gaiBianBuJuInMenber(renderL,typ,single)
				layermembers.append(single)
			self.zwfOutputRenderpassControlDatas[renderL]['MemberObjects']=layermembers
			cmds.textScrollList('ritsl_V2',e=True,ra=True)
			cmds.textScrollList('ritsl_V2',e=True,append=self.getAllRenderLayers())
			cmds.textFieldGrp('renderln_V2',e=True,tx='')
			mel.eval('renderLayerEditorRenderable RenderLayerTab "defaultRenderLayer" "0"')
			cmds.waitCursor( state=False )
		self.saveOutputRenderpassControlDatas()
	def selectrenderLayer_C(self,*args):
		self.switchToChannelbox()
		allRL=self.getAllRenderLayers()
		sel_renderLN=cmds.textScrollList('ritsl_V2',q=True,si=True)
		cmds.textScrollList('pitsl_V2',e=True,ra=True)
		cmds.textScrollList('m_ritsl_V2',e=True,ra=True)
		cmds.textScrollList('menp_itsl_V2',e=True,ra=True)
		cmds.textScrollList('rrbb_itsl_V2',e=True,ra=True)
		cmds.textScrollList('linkR_itsl_V2',e=True,ra=True)
		cmds.textScrollList('linkL_ritsl_V2',e=True,da=True)
#		print self.zwfOutputRenderpassControlDatas
		if sel_renderLN==None:
			cmds.textFieldGrp('pass_cm_V2',e=True,en=False)
			cmds.button('c_bbb_V2',e=True,en=False)
			cmds.button('de_bbb_V2',e=True,en=False)
			cmds.button('re_bbb_V2',e=True,en=False)
			cmds.textField('buffername_V2',e=True,tx='')
			cmds.textField('buffername_V2',e=True,en=False)
			cmds.optionMenu('datetype_V2', e=True,en=False)
#			for sRl in allRL:
#				if sRl!='defaultRenderLayer':
#					cmds.textScrollList('linkR_itsl_V2',e=True,append=sRl)
		else:
			cmds.select(allRL,d=True)
			for single in sel_renderLN:
				cmds.editRenderLayerGlobals(currentRenderLayer=single)
				cmds.select(single,add=True)
				if single!='defaultRenderLayer':
					cmds.textFieldGrp('pass_cm_V2',e=True,en=True)
					cmds.button('c_bbb_V2',e=True,en=True)
					cmds.button('de_bbb_V2',e=True,en=True)
					cmds.button('re_bbb_V2',e=True,en=True)
					if 'AllAddlightpasses' in self.zwfOutputRenderpassControlDatas[single]:
						addlightPasses=self.zwfOutputRenderpassControlDatas[single]['AllAddlightpasses']
						cmds.textScrollList('pitsl_V2',e=True,append=addlightPasses.keys())
					#--------------------------------------------menmbwe ( renderLayer)---------------------------------------
					p_snb=self.zwfOutputRenderpassControlDatas[single]['MemberObjects']
					cmds.textScrollList('m_ritsl_V2',e=True,append=p_snb)
					#--------------------------------------------------------render----------------------------------------------
					if 'Renderpasses' in self.zwfOutputRenderpassControlDatas[single]:
						passes=self.zwfOutputRenderpassControlDatas[single]['Renderpasses'].keys()
						if len(passes):
							[cmds.textScrollList('rrbb_itsl_V2',e=True,append=self.zwfOutputRenderpassControlDatas[single]['Renderpasses'][each]['NameDataType']) for each in passes]
				else:
					cmds.textFieldGrp('pass_cm_V2',e=True,en=False)
					cmds.button('c_bbb_V2',e=True,en=False)
					cmds.button('de_bbb_V2',e=True,en=False)
					cmds.button('re_bbb_V2',e=True,en=False)
			#--------------------------------------------------------link-------------------------------------------------
			allrenderLayers=self.getAllRenderLayers_exc()
			[cmds.textScrollList('linkR_itsl_V2',e=True,append=eachRL) for eachRL in allrenderLayers if eachRL not in sel_renderLN]
	def del_addlightpassFormrendelayer(self,renderlayer):
		passContributionMaps=cmds.listConnections(renderlayer,s=False,type='passContributionMap')
		if passContributionMaps!=None:
			cmds.delete(passContributionMaps)
	def del_Renderlayer(self,*args):
		sel_renderLN=cmds.textScrollList('ritsl_V2',q=True,si=True)
		if sel_renderLN==None:
			return cmds.warning('no selected in Renderlayer textScrollList.')
		else:
			for each in sel_renderLN:
				if each!='defaultRenderLayer':
					self.del_addlightpassFormrendelayer(each)
					anotherlayers=self.getAnotherRenderLayer(each)
					if len(anotherlayers):
						for eachlayer in anotherlayers:
							layer=self.zwfOutputRenderpassControlDatas[eachlayer]
							if 'Reflection' in layer:
								reflectionlayers=layer['Reflection']
							else:
								reflectionlayers=[]
							if 'Refraction' in layer:
								refractionlayers=layer['Refraction']
							else:
								refractionlayers=[]
							if 'Shadow' in layer:
								shadowayers=layer['Shadow']
							else:
								shadowayers=[]
							if 'Matte' in layer:
								mattelayers=layer['Matte']
							else:
								mattelayers=[]
							if each in reflectionlayers:
								layer['Reflection']=self.removeItem(layer['Reflection'],each)
							if each in refractionlayers:
								layer['Refraction']=self.removeItem(layer['Refraction'],each)
							if each in shadowayers:
								layer['Shadow']=self.removeItem(layer['Shadow'],each)
							if each in mattelayers:
								layer['Matte']=self.removeItem(layer['Matte'],each)
					cmds.editRenderLayerGlobals(currentRenderLayer='defaultRenderLayer')
					cmds.delete(each)
					del self.zwfOutputRenderpassControlDatas[each]
					cmds.textScrollList('ritsl_V2',e=True,ri=each)

				else:
					cmds.warning('"defaultRenderLayer" can not delete!')
			self.selectrenderLayer_C()
		self.saveOutputRenderpassControlDatas()
	def renameRenderLayer(self,*args):
		sel_renderLN=cmds.textScrollList('ritsl_V2',q=True,si=True)
		if sel_renderLN!=None:
			if len(sel_renderLN)==1:
				if sel_renderLN[0]=="defaultRenderLayer":
					return cmds.warning('"defaultRenderLayer" can not rename!!!')
				tt=sel_renderLN[0]
				result = cmds.promptDialog(title='RenderLayerRename',message='RenderLayer Name:',text=tt,button=['OK', 'Cancel'],defaultButton='OK',cancelButton='Cancel',dismissString='Cancel')
				if result=='OK':
					newLayerName=cmds.promptDialog(q=True, text=True)
#=================================================================================================修改层中=MemberObjects==================================================================================================================================================
					if 'MemberObjects' in self.zwfOutputRenderpassControlDatas[tt]:
						menberobjs=self.zwfOutputRenderpassControlDatas[tt]['MemberObjects']
						if len(menberobjs):
							newmenberobjs=[]
							for single in menberobjs:
								splits=single.split(' : ')
								newsingle='%s : %s : %s'%(newLayerName,splits[1],splits[2])
								if single[:3]==' ! ':
									newsingle=' ! %s'%newsingle
								newmenberobjs.append(newsingle)
							self.zwfOutputRenderpassControlDatas[tt]['MemberObjects']=newmenberobjs
#=================================================================================================修改层中=addLightPass==================================================================================================================================================
					if 'AllAddlightpasses' in self.zwfOutputRenderpassControlDatas[tt]:
						addlightpasses=self.zwfOutputRenderpassControlDatas[tt]['AllAddlightpasses']
						if len(addlightpasses):
							for each in addlightpasses.keys():
								neweach=newLayerName+each[len(tt):]
								addlightpasses[neweach]=addlightpasses[each]
								del addlightpasses[each]
#=================================================================================================修改层中=Renderpasses==================================================================================================================================================
					if 'Renderpasses' in self.zwfOutputRenderpassControlDatas[tt]:
						renderpasses=self.zwfOutputRenderpassControlDatas[tt]['Renderpasses']
						if len(renderpasses):
							for eachrenderpass in renderpasses:
								oldname=renderpasses[eachrenderpass]['Name']
								newname=newLayerName+oldname[len(tt):]
								oldnamedatetype=renderpasses[eachrenderpass]['NameDataType']
								oldsplits=oldnamedatetype.split(' : ')
								newnamedatetype=oldsplits[0]+' : '+newLayerName+oldsplits[-1][len(tt):]
								renderpasses[eachrenderpass]['Name']=newname
								renderpasses[eachrenderpass]['NameDataType']=newnamedatetype
					self.zwfOutputRenderpassControlDatas[newLayerName]=self.zwfOutputRenderpassControlDatas[tt]
					del self.zwfOutputRenderpassControlDatas[tt]
#=================================================================================================修改层中其他层的link==================================================================================================================================================
					AnotherRenderLayers=self.getAnotherRenderLayer(tt)
					if len(AnotherRenderLayers):
						for each_rl in AnotherRenderLayers:
							if 'Reflection' in self.zwfOutputRenderpassControlDatas[each_rl]:
								reflectionlink=self.zwfOutputRenderpassControlDatas[each_rl]['Reflection']
								if len(reflectionlink):
									if tt in reflectionlink:
										self.zwfOutputRenderpassControlDatas[each_rl]['Reflection']=self.removeItem(self.zwfOutputRenderpassControlDatas[each_rl]['Reflection'],tt)
										self.zwfOutputRenderpassControlDatas[each_rl]['Reflection'].append(newLayerName)
							if 'Refraction' in self.zwfOutputRenderpassControlDatas[each_rl]:
								refractionlink=self.zwfOutputRenderpassControlDatas[each_rl]['Refraction']
								if len(refractionlink):
									if tt in refractionlink:
										self.zwfOutputRenderpassControlDatas[each_rl]['Refraction']=self.removeItem(self.zwfOutputRenderpassControlDatas[each_rl]['Refraction'],tt)
										self.zwfOutputRenderpassControlDatas[each_rl]['Refraction'].append(newLayerName)
							if 'Shadow' in self.zwfOutputRenderpassControlDatas[each_rl]:
								Shadowlink=self.zwfOutputRenderpassControlDatas[each_rl]['Shadow']
								if len(Shadowlink):
									if tt in Shadowlink:
										self.zwfOutputRenderpassControlDatas[each_rl]['Shadow']=self.removeItem(self.zwfOutputRenderpassControlDatas[each_rl]['Shadow'],tt)
										self.zwfOutputRenderpassControlDatas[each_rl]['Shadow'].append(newLayerName)
							if 'Matte' in self.zwfOutputRenderpassControlDatas[each_rl]:
								Mattelink=self.zwfOutputRenderpassControlDatas[each_rl]['Matte']
								if len(Mattelink):
									if tt in Mattelink:
										self.zwfOutputRenderpassControlDatas[each_rl]['Matte']=self.removeItem(self.zwfOutputRenderpassControlDatas[each_rl]['Matte'],tt)
										self.zwfOutputRenderpassControlDatas[each_rl]['Matte'].append(newLayerName)
#=================================================================================================重新命名渲染层和addlightPass==================================================================================================================================================
					newtt=cmds.rename(tt,newLayerName)
					addlightpasses=cmds.listConnections(newtt,s=False,type='passContributionMap')
					if addlightpasses!=None:
						[cmds.rename(s,(newLayerName+s[len(tt):])) for s in addlightpasses]
					cmds.textScrollList('ritsl_V2',e=True,ra=True)
					cmds.textScrollList('ritsl_V2',e=True,append=self.getAllRenderLayers())
					self.selectrenderLayer_C()
			else:
				cmds.warning('plase select one in RenderLayer textScrollList.')
		else:
			cmds.warning('no selected in RenderLayer textScrollList.')
		self.saveOutputRenderpassControlDatas()
#====================================================================================================添加物体到选择的渲染层=====================================================================================================================
	def addSelectToRenderLayer(self,*args):
		sel_renderLN=cmds.textScrollList('ritsl_V2',q=True,si=True)
		all_renderLN=cmds.textScrollList('m_ritsl_V2',q=True,ai=True)
		selected=self.selectObj()
		if selected==[]:
			return cmds.warning('no selected.')
		if sel_renderLN!=None:
			cmds.textScrollList('m_ritsl_V2',e=True,ra=True)
			for each in sel_renderLN:
				if each=="defaultRenderLayer":
					continue
				cmds.editRenderLayerMembers(each,selected,nr=True)
#				moveOverr(selected,eachsel)
				for single in selected:
					if single not  in self.zwfOutputRenderpassControlDatas[each]['AllObjects']:
#						self.zwfOutputRenderpassControlDatas[each]['AllObjects']=self.removeItem(self.zwfOutputRenderpassControlDatas[each]['AllObjects'],single)
#						selected.remove(single)
#					else:
						self.zwfOutputRenderpassControlDatas[each]['AllObjects'].append(single)
						m=self.getType(single)
						e=self.gaiBianBuJuInMenber(each,m,single)
						self.zwfOutputRenderpassControlDatas[each]['MemberObjects'].append(e)
				if len(selected):
					pns_objs=self.getobjFromRenderLayer(selected,['mesh','subdiv','nurbsSurface'])
					light_objs=self.getobjFromRenderLayer(selected,'light')
					if len(pns_objs):
						if 'PNSObjects'not  in self.zwfOutputRenderpassControlDatas[each]:
							self.zwfOutputRenderpassControlDatas[each]['PNSObjects']=[]
						[self.zwfOutputRenderpassControlDatas[each]['PNSObjects'].append(s) for s in pns_objs if s not in self.zwfOutputRenderpassControlDatas[each]['PNSObjects']]
					if len(light_objs):
						if 'LIGHTObjects'not  in self.zwfOutputRenderpassControlDatas[each]:
							self.zwfOutputRenderpassControlDatas[each]['LIGHTObjects']=[]
						[self.zwfOutputRenderpassControlDatas[each]['LIGHTObjects'].append(l) for l in light_objs if l not in self.zwfOutputRenderpassControlDatas[each]['LIGHTObjects']]
				cmds.textScrollList('m_ritsl_V2',e=True,append=self.zwfOutputRenderpassControlDatas[each]['MemberObjects'])
		self.saveOutputRenderpassControlDatas()
	def removeSelectToRenderLayer(self,*args):
		sel_renderLN=cmds.textScrollList('ritsl_V2',q=True,si=True)
		allI=cmds.textScrollList('m_ritsl_V2',q=True,ai=True)
		if allI==None:
			return cmds.warning('no items in members textScrollList.')
		selected=self.selectObj()
		if selected==[]:
			return cmds.warning('no selected.')
		cmds.textScrollList('m_ritsl_V2',e=True,ra=True)
		if sel_renderLN!=None:
			for each in sel_renderLN:
				cmds.editRenderLayerMembers(each,selected,noRecurse=True,r=True)
				for single in selected:
					if single in self.zwfOutputRenderpassControlDatas[each]['AllObjects']:
						self.zwfOutputRenderpassControlDatas[each]['AllObjects']=self.removeItem(self.zwfOutputRenderpassControlDatas[each]['AllObjects'],single)
						pns_objs=self.getobjFromRenderLayer(single,['mesh','subdiv','nurbsSurface'])
						light_objs=self.getobjFromRenderLayer(single,'light')
						if len(pns_objs):
							for s in pns_objs:
								if s in self.zwfOutputRenderpassControlDatas[each]['PNSObjects']:
									self.zwfOutputRenderpassControlDatas[each]['PNSObjects']=self.removeItem(self.zwfOutputRenderpassControlDatas[each]['PNSObjects'],s) 
						if len(pns_objs):
							for l in light_objs:
								if l in self.zwfOutputRenderpassControlDatas[each]['LIGHTObjects']:
									self.zwfOutputRenderpassControlDatas[each]['LIGHTObjects']=self.removeItem(self.zwfOutputRenderpassControlDatas[each]['LIGHTObjects'],l) 
						m=self.getType(single)
						e=self.gaiBianBuJuInMenber(each,m,single)
						if e in self.zwfOutputRenderpassControlDatas[each]['MemberObjects']:
							self.zwfOutputRenderpassControlDatas[each]['MemberObjects']=self.removeItem(self.zwfOutputRenderpassControlDatas[each]['MemberObjects'],e)
				cmds.textScrollList('m_ritsl_V2',e=True,append=self.zwfOutputRenderpassControlDatas[each]['MemberObjects'])
		self.saveOutputRenderpassControlDatas()
#==================================================================================================添加分层灯光部分============================================================================================
	def getLightFromSelected(self,selectx):
		selected=cmds.listRelatives(cmds.listRelatives(selectx,ad=True,pa=True,type='light'),p=True,pa=True)
		return selected
	def createAddLightPass(self,*args):
		PCMName=cmds.textFieldGrp('pass_cm_V2',q=True,tx=True)
		selected=self.selectObj()
		if selected==[]:
			return cmds.warning( "No lights were selected!!" )
		else:
			cpcm_light=cmds.listRelatives(selected,ad=True,type='light',pa=True)
			if cpcm_light==None:
				return cmds.warning( "No lights were selected!!" )
			else:
				selected=self.getLightFromSelected(selected)
		if not len(PCMName):
			return cmds.warning( "no words in lightPassName:" )
		sel_renderLN=cmds.textScrollList('ritsl_V2',q=True,si=True)
		cmds.textScrollList('pitsl_V2',e=True,ra=True)
		for single in sel_renderLN:
			pcmn=cmds.createNode('passContributionMap', n=PCMName, skipSelect=True)
			pcmn=cmds.rename(pcmn,'%s_%s'%(single,pcmn))
			cmds.connectAttr('%s.passContributionMap'%single, '%s.owner'%pcmn,na=True )
			if 'AllAddlightpasses' not in self.zwfOutputRenderpassControlDatas[single]:
				self.zwfOutputRenderpassControlDatas[single]['AllAddlightpasses']={}
			self.zwfOutputRenderpassControlDatas[single]['AllAddlightpasses'][pcmn]=selected
			allLightPasses=self.zwfOutputRenderpassControlDatas[single]['AllAddlightpasses']
			cmds.textScrollList('pitsl_V2',e=True,append=allLightPasses.keys())
		cmds.textFieldGrp('pass_cm_V2',e=True,tx='')
		self.saveOutputRenderpassControlDatas()
	def selectAddlightPass_C(self,*args):
		PCMN=cmds.textScrollList('pitsl_V2',q=True,si=True)
		cmds.textScrollList('menp_itsl_V2',e=True,ra=True)
		if PCMN!=None:
			for each in PCMN:
				renderlayer=cmds.listConnections(each,d=False,type='renderLayer')[0]
				pcmn_obj=self.zwfOutputRenderpassControlDatas[renderlayer]['AllAddlightpasses'][each]
				for e in pcmn_obj:
					m=self.getType(e)
					e=self.gaiBianBuJuInMenber(each,m,e)
					cmds.textScrollList('menp_itsl_V2',e=True,append=e)

	def del_addlightPass(self,*args):
		sel_lightpassLN=cmds.textScrollList('pitsl_V2',q=True,si=True)
		if sel_lightpassLN==None:
			return cmds.warning('no selected in AddLightPass textScrollList.')
		else:
			for each in sel_lightpassLN:
				renderlayer=cmds.listConnections(each,d=False,type='renderLayer')[0]
				del self.zwfOutputRenderpassControlDatas[renderlayer]['AllAddlightpasses'][each]
				cmds.delete(each)
				cmds.textScrollList('pitsl_V2',e=True,ri=each)
			self.selectrenderLayer_C()
		self.saveOutputRenderpassControlDatas()
	def renameLightPass(self,*args):
		sel_lightPasses=cmds.textScrollList('pitsl_V2',q=True,si=True)
		if sel_lightPasses!=None:
			if len(sel_lightPasses)==1:
				layerName=cmds.listConnections(sel_lightPasses[0],d=False,type='renderLayer')[0]
				tt=sel_lightPasses[0][(len(layerName)+1):]
				result = cmds.promptDialog(title='Rename AddLightPass',message='AddLightPass Name:',text=tt,button=['OK', 'Cancel'],defaultButton='OK',cancelButton='Cancel',dismissString='Cancel')
				if result=='OK':
					LpName=cmds.promptDialog(q=True, text=True)
					newLightpassName='%s_%s'%(layerName,LpName)
					lightPassesd=self.zwfOutputRenderpassControlDatas[layerName]['AllAddlightpasses'][sel_lightPasses[0]]
					self.zwfOutputRenderpassControlDatas[layerName]['AllAddlightpasses'][newLightpassName]=lightPassesd
					del self.zwfOutputRenderpassControlDatas[layerName]['AllAddlightpasses'][sel_lightPasses[0]]

					cmds.rename(sel_lightPasses[0],newLightpassName)

					i=cmds.textScrollList('pitsl_V2',q=True,sii=True)[0]
					cmds.textScrollList('pitsl_V2',e=True,ri=sel_lightPasses[0])
					cmds.textScrollList('pitsl_V2',e=True,ap=[i,newLightpassName])
					cmds.textScrollList('menp_itsl_V2',e=True,ra=True)
			else:
				cmds.warning('please select one item in AddLightPass textScrollList!')
		else:
			cmds.warning('no selected in AddLightPass textScrollList!')
		self.saveOutputRenderpassControlDatas()
	def addSelectToAddLightPass(self,*ags):
		sel_passCM=cmds.textScrollList('pitsl_V2',q=True,si=True)
		if sel_passCM==None:
			return cmds.warning('no items were selectes in AddLightPass textScrollList.')
		selected=self.selectObj()
		if selected==[]:
			return cmds.warning('no selected.')
		else:
			cpcm_light=cmds.listRelatives(selected,ad=True,type='light',pa=True)
			if cpcm_light==None:
				return cmds.warning( "No lights were selected!!" )
			else:
				selected=self.getLightFromSelected(selected)
		cmds.textScrollList('menp_itsl_V2',e=True,ra=True)
		for each in sel_passCM:
			renderlayer=cmds.listConnections(each,d=False,type='renderLayer')[0]
			for single in selected:
				if single not in self.zwfOutputRenderpassControlDatas[renderlayer]['AllAddlightpasses'][each]:
					self.zwfOutputRenderpassControlDatas[renderlayer]['AllAddlightpasses'][each].append(single)
			for singles in self.zwfOutputRenderpassControlDatas[renderlayer]['AllAddlightpasses'][each]:
				m=self.getType(singles)
				x=self.gaiBianBuJuInMenber(each,m,singles)
				cmds.textScrollList('menp_itsl_V2',e=True,append=x)

		sel_renderlayers=cmds.textScrollList('ritsl_V2',q=True,si=True)
		for single_renderlayer in sel_renderlayers:
			if 'LIGHTObjects' not in self.zwfOutputRenderpassControlDatas[single_renderlayer]:
				self.zwfOutputRenderpassControlDatas[single_renderlayer]['LIGHTObjects']=[]
			all_lights_inRl=self.zwfOutputRenderpassControlDatas[single_renderlayer]['LIGHTObjects']
			for ssssel in selected:
				if not ssssel in all_lights_inRl:
					self.addSelectToRenderLayer()
		self.saveOutputRenderpassControlDatas()
	def removeSelectToAddLightPass(self,*args):
		sel_passCM=cmds.textScrollList('pitsl_V2',q=True,si=True)
		if sel_passCM==None:
			return cmds.warning('no items were selectes in passContributionMap textScrollList.')
		selected=self.selectObj()
		if selected==[]:
			return cmds.warning('no selected.')
		else:
			cpcm_light=cmds.listRelatives(selected,ad=True,type='light',pa=True)
			if cpcm_light==None:
				return cmds.warning( "No lights were selected!!" )
			else:
				selected=self.getLightFromSelected(selected)
		cmds.textScrollList('menp_itsl_V2',e=True,ra=True)
		for each in sel_passCM:
			renderlayer=cmds.listConnections(each,d=False,type='renderLayer')[0]
			addlightpass=self.zwfOutputRenderpassControlDatas[renderlayer]['AllAddlightpasses'][each]
			for single in selected:
				if single in addlightpass:
					self.zwfOutputRenderpassControlDatas[renderlayer]['AllAddlightpasses'][each]=self.removeItem(self.zwfOutputRenderpassControlDatas[renderlayer]['AllAddlightpasses'][each],single) 
			addlightpass=self.zwfOutputRenderpassControlDatas[renderlayer]['AllAddlightpasses'][each]
			for singlex in addlightpass:
				m=self.getType(singlex)
				x=self.gaiBianBuJuInMenber(each,m,singlex)
				cmds.textScrollList('menp_itsl_V2',e=True,append=x)
		self.saveOutputRenderpassControlDatas()
#=============================================================================================创建renderPass部分====================================================================================================================================
	def addRenderpass(self,*args):
		sel_renderLayer=cmds.textScrollList('ritsl_V2',q=True,si=True)
		if sel_renderLayer==None:
			return cmds.warning('no selected in RenderLayer textScrollList.')
		sel_presets_pass=cmds.textScrollList('rb_ritsl_V2',q=True,si=True)
		if sel_presets_pass==None:
			cmds.warning ('no pass were selected in Presets.')
		else:
			cmds.textScrollList('rrbb_itsl_V2',e=True,ra=True)
			for single in sel_renderLayer:
				if single =="defaultRenderLayer":
					continue
				if 'Renderpasses' not in self.zwfOutputRenderpassControlDatas[single]:
					self.zwfOutputRenderpassControlDatas[single]['Renderpasses']={}
				for each in sel_presets_pass:
					if each not in self.zwfOutputRenderpassControlDatas[single]['Renderpasses']:
						self.zwfOutputRenderpassControlDatas[single]['Renderpasses'][each]={}
						name=single+'_'+self.renamePass(each)
						type=self.getPassDataType(each)
						nametype=self.getRenderpassType(each,name)
						self.zwfOutputRenderpassControlDatas[single]['Renderpasses'][each]['Name']=name
						self.zwfOutputRenderpassControlDatas[single]['Renderpasses'][each]['DataType']=type
						self.zwfOutputRenderpassControlDatas[single]['Renderpasses'][each]['NameDataType']=nametype
				renderpasseskeys=self.zwfOutputRenderpassControlDatas[single]['Renderpasses'].keys()
				[cmds.textScrollList('rrbb_itsl_V2',e=True,append=self.zwfOutputRenderpassControlDatas[single]['Renderpasses'][s]['NameDataType']) for s in renderpasseskeys]
			cmds.textScrollList('rb_ritsl_V2',e=True,da=True)
		self.saveOutputRenderpassControlDatas()
	def getPassDataType(self,passName):
		if passName=='Color':
			datatype=1
		if passName=='DiffuseColor':
			datatype=512
		if passName=='Light':
			datatype=256
		if passName=='Indirect':
			datatype=256
		if passName=='Specular':
			datatype=512
		if passName=='AmbientColor':
			datatype=256
		if passName=='Incandescence':
			datatype=1
		if passName=='SSS':
			datatype=256
		if passName=='Reflection':
			datatype=256
		if passName=='Refraction':
			datatype=256
		if passName=='GlowSource':
			datatype=256
		if passName=='VolumeLight':
			datatype=256
		if passName=='VolumeObject':
			datatype=256
		if passName=='VolumeScene':
			datatype=256
		if passName=='AddSpecular':
			datatype=256
		if passName=='AddReflection':
			datatype=256
		if passName=='AO':
			datatype=256
		if passName=='WorldNormal':
			datatype=256
		if passName=='Zdepth':
			datatype=256
		if passName=='FacingRatio':
			datatype=256
		if passName=='AssetObjectID':
			datatype=1
		if passName=='MV':
			datatype=512
		if passName=='MaterialID':
			datatype=1
		return datatype
	def renamePass(self,passName):
		if passName=='Color':
			passName='color'
		if passName=='DiffuseColor':
			passName='dif'
		if passName=='Light':
			passName='light'
		if passName=='Indirect':
			passName='indirect'
		if passName=='Specular':
			passName='spe'
		if passName=='AmbientColor':
			passName='amb'
		if passName=='Incandescence':
			passName='inc'
		if passName=='SSS':
			passName='sss'
		if passName=='Reflection':
			passName='refl'
		if passName=='Refraction':
			passName='refr'
		if passName=='GlowSource':
			passName='glow'
		if passName=='VolumeLight':
			passName='volLig'
		if passName=='VolumeObject':
			passName='volObj'
		if passName=='VolumeScene':
			passName='volScn'
		if passName=='AddSpecular':
			passName='addSpe'
		if passName=='AddReflection':
			passName='addRefl'
		if passName=='AO':
			passName='ao'
		if passName=='WorldNormal':
			passName='wNormal'
		if passName=='Zdepth':
			passName='camZ'
		if passName=='FacingRatio':
			passName='FR'
		if passName=='AssetObjectID':
			passName='assetId'
		if passName=='MV':
			passName='mv'
		if passName=='MaterialID':
			passName='matId'
		return passName
	def getRenderpassType(self,passName,newpassName):
		dataType=self.getPassDataType(passName)
		if dataType==1:
			bufferType='8-bit Integer (unsigned)'
		if dataType==2:
			bufferType='16-bit Integer (unsigned)'
		if dataType==256:
			bufferType='16-bit Float'
		if dataType==512:
			bufferType='32-bit Float'
		textName='{ %s : %s }      %s'%(passName,newpassName,bufferType)
		return textName

	def getObjInRenderLayer(self,obj):
		sel_renderLayer=cmds.textScrollList('ritsl_V2',q=True,si=True)
		sel_renderLayer=self.houxiaoRendeLayer(sel_renderLayer)
		pre_passname=obj.split(' : ')[0][2:]
		for each in sel_renderLayer:
			if 'Renderpasses' in self.zwfOutputRenderpassControlDatas[each]:
				if pre_passname in self.zwfOutputRenderpassControlDatas[each]['Renderpasses']:
					if self.zwfOutputRenderpassControlDatas[each]['Renderpasses'][pre_passname]['NameDataType']==obj:
						return each

	def houxiaoRendeLayer(self,renderLayerList):
		newrenderLayer=[]
		[newrenderLayer.append(single) for single in renderLayerList if single!="defaultRenderLayer"]
		return newrenderLayer

	def renderTextScrollList_C(self,*args):
		renderPassText=cmds.textScrollList('rrbb_itsl_V2',q=True,si=True)
		if renderPassText!=None:
			for single in renderPassText:
				cmds.optionMenu('datetype_V2',e=True,en=True)
			if len(renderPassText)==1:
				passName=single.split(' : ')[-1].split(' } ')[0]
				cmds.text('buffername_t_V2',e=True,en=True)
				cmds.textField('buffername_V2',e=True,en=True)
				rendeLayername=self.getObjInRenderLayer(renderPassText[0])
				part_passName=passName[(len(rendeLayername)+1):]
				cmds.textField('buffername_V2',e=True,tx=part_passName)
				cmds.textField('qz_V2',e=True, tx='%s_'%rendeLayername)
			else:
				cmds.text('buffername_t_V2',e=True,en=False)
				cmds.textField('buffername_V2',e=True,en=False)
				cmds.textField('buffername_V2',e=True,tx='')
				cmds.textField('qz_V2',e=True, tx='')
		else:
			cmds.textField('buffername_V2',e=True,en=False)
			cmds.optionMenu('datetype_V2',e=True,en=False)
			cmds.textField('qz_V2',e=True, tx='')

	def deleteRenderpass(self,*args):
		renderPassText=cmds.textScrollList('rrbb_itsl_V2',q=True,si=True)
		sel_renderLayer=cmds.textScrollList('ritsl_V2',q=True,si=True)
		sel_renderLayer=self.houxiaoRendeLayer(sel_renderLayer)
		if renderPassText!=None:
			for single in renderPassText:
				pre_passname=single.split(' : ')[0][2:]
				renderlayername=self.getObjInRenderLayer(single)
				del self.zwfOutputRenderpassControlDatas[renderlayername]['Renderpasses'][pre_passname]
			cmds.textScrollList('rrbb_itsl_V2',e=True,ra=True)
			for s in sel_renderLayer:
				if 'Renderpasses' in self.zwfOutputRenderpassControlDatas[s]:
					keys=self.zwfOutputRenderpassControlDatas[s]['Renderpasses'].keys()
					if len(keys):
						[cmds.textScrollList('rrbb_itsl_V2',e=True,append=self.zwfOutputRenderpassControlDatas[s]['Renderpasses'][each]['NameDataType']) for each in keys]
		else:
			cmds.warning('no selected in Render textScrollList.')
		self.saveOutputRenderpassControlDatas()
	def renameRenderPassName(self,*args):
		renderPassText=cmds.textScrollList('rrbb_itsl_V2',q=True,si=True)
		if len(renderPassText)!=1:
			cmds.warning('please you select one renderPass in Render textScrolllist.')
		else:
			bn=cmds.textField('buffername_V2',q=True,tx=True)
			if not len(bn):
				cmds.warning('no worlds in Buffer Name.')
			else:
				sel_renderLayer=cmds.textScrollList('ritsl_V2',q=True,si=True)
				sel_renderLayer=self.houxiaoRendeLayer(sel_renderLayer)
				sel_renderPass=renderPassText[0]
				oldname=sel_renderPass.split(' : ')[-1].split(' } ')[0]
				QZ=cmds.textField('qz_V2',q=True,tx=True)
				name='%s%s'%(QZ,bn)
				pre_passname=sel_renderPass.split(' : ')[0][2:]
				renderlayername=self.getObjInRenderLayer(sel_renderPass)
				self.zwfOutputRenderpassControlDatas[renderlayername]['Renderpasses'][pre_passname]['Name']=name
				self.zwfOutputRenderpassControlDatas[renderlayername]['Renderpasses'][pre_passname]['NameDataType']=sel_renderPass.replace(oldname,name)
				nrenderPassText=self.zwfOutputRenderpassControlDatas[renderlayername]['Renderpasses'][pre_passname]['NameDataType']
				i=cmds.textScrollList('rrbb_itsl_V2',q=True,sii=True)[0]
				cmds.textScrollList('rrbb_itsl_V2',e=True,ri=renderPassText[0])
				cmds.textScrollList('rrbb_itsl_V2',e=True,ap=[i,nrenderPassText])
				cmds.textField('buffername_V2',e=True,tx='')
				cmds.textField('buffername_V2',e=True,en=False)
				cmds.optionMenu('datetype_V2', e=True,en=False)
		self.saveOutputRenderpassControlDatas()
	def dataType_C(self,*args):
		renderPassText=cmds.textScrollList('rrbb_itsl_V2',q=True,si=True)
		dtn=cmds.optionMenu('datetype_V2',q=True,sl=True)
		for single in renderPassText:
			cmds.textScrollList('rrbb_itsl_V2',e=True,si=single)
			renderPassNum=cmds.textScrollList('rrbb_itsl_V2',q=True,sii=True)[0]
			single_L=single.split(' : ')[-1].split(' }      ')
			single_pass=single_L[0]
			single_type=single_L[1]
			passname=single.split(' : ')[0][2:]
			renderlayername=self.getObjInRenderLayer(single)
			cmds.textScrollList('rrbb_itsl_V2',e=True,ri=single)
			if dtn==1:
				n_text=single.replace(single_type,'8-bit Integer (unsigned)')
				self.zwfOutputRenderpassControlDatas[renderlayername]['Renderpasses'][passname]['DataType']=1
				self.zwfOutputRenderpassControlDatas[renderlayername]['Renderpasses'][passname]['NameDataType']=n_text
				cmds.textScrollList('rrbb_itsl_V2',e=True,ap=[renderPassNum,n_text])
			if dtn==2:
				n_text=single.replace(single_type,'16-bit Integer (unsigned)')
				self.zwfOutputRenderpassControlDatas[renderlayername]['Renderpasses'][passname]['DataType']=2
				self.zwfOutputRenderpassControlDatas[renderlayername]['Renderpasses'][passname]['NameDataType']=n_text
				cmds.textScrollList('rrbb_itsl_V2',e=True,ap=[renderPassNum,n_text])
			if dtn==3:
				n_text=single.replace(single_type,'16-bit Float')
				self.zwfOutputRenderpassControlDatas[renderlayername]['Renderpasses'][passname]['DataType']=256
				self.zwfOutputRenderpassControlDatas[renderlayername]['Renderpasses'][passname]['NameDataType']=n_text
				cmds.textScrollList('rrbb_itsl_V2',e=True,ap=[renderPassNum,n_text])
			if dtn==4:
				n_text=single.replace(single_type,'32-bit Float')
				self.zwfOutputRenderpassControlDatas[renderlayername]['Renderpasses'][passname]['DataType']=512
				self.zwfOutputRenderpassControlDatas[renderlayername]['Renderpasses'][passname]['NameDataType']=n_text
				cmds.textScrollList('rrbb_itsl_V2',e=True,ap=[renderPassNum,n_text])
			cmds.optionMenu('datetype_V2',e=True,en=False)
			cmds.textField('buffername_V2',e=True,en=False)
			cmds.textField('qz_V2',e=True,tx='')
		self.saveOutputRenderpassControlDatas()
	def setUpAndBreakLinks(self,*args):
		sel_renderLayer=cmds.textScrollList('ritsl_V2',q=True,si=True)
		if sel_renderLayer==None:
			return cmds.warning('no selected in RenderLayer textScrollList.')
		linkNum=cmds.textScrollList('linkL_ritsl_V2',q=True,si=True)
		if linkNum==None:
			return cmds.warning('no selected in Link Type textScrollList.')
		linkRL=cmds.textScrollList('linkR_itsl_V2',q=True,si=True)
		if linkRL==None:
			linkRL=[]
		for single in sel_renderLayer:
			self.zwfOutputRenderpassControlDatas[single][linkNum[0]]=linkRL
		self.saveOutputRenderpassControlDatas()
	def seleceLinkType_C(self,*args):
		sel_renderLayer=cmds.textScrollList('ritsl_V2',q=True,si=True)
		if sel_renderLayer!=None:
			if len(sel_renderLayer)!=1:
				return cmds.warning('please you select one renderLayer in RenderLayer textScrollList!')
			if sel_renderLayer[0]=='defaultRenderLayer':
				return
			linkNum=cmds.textScrollList('linkL_ritsl_V2',q=True,si=True)
			cmds.textScrollList('linkR_itsl_V2',e=True,da=True)
			if linkNum==None:
				cmds.textScrollList('linkR_itsl_V2',e=True,da=True)
			else:
				if linkNum[0] in self.zwfOutputRenderpassControlDatas[sel_renderLayer[0]]:
					linkRL=self.zwfOutputRenderpassControlDatas[sel_renderLayer[0]][linkNum[0]]
					if len(linkRL):
						[cmds.textScrollList('linkR_itsl_V2',e=True,si=each) for each in linkRL]

#=====================================================创建设置=======================================================================================================================================
#==========================================================删除列表中重复的物体（只留一个）===========================================================================================================
	def deleteDInList(self,listName=[]):
		midList=[]
		for eachName in listName:
			if not eachName in midList:
				midList.append(eachName)
		return midList

#=====================================================得到（除“lambert” 和 “particleCloud“ and "displacementShader"） 所有材质=======================================================================================================================================
	def getAllMyShader(self):
		allshaderList=cmds.ls(mat=True)
		shaders=[]
		for single in allshaderList:
			if cmds.nodeType(single)=='displacementShader':
				continue
			if single!='lambert1' and single!='particleCloud1':
				shaders.append(single)
		return shaders

#=====================================================根据renderLayer得到（除“lambert” 和 “particleCloud“ ） 材质======================================================================================================================================
	def getNewObjshapesList(self,oldshapesList):
		newShapeList=[]
		[newShapeList .append(single) for single in oldshapesList if not cmds.getAttr('%s.intermediateObject'%single)]
		return newShapeList

	def getShadersFromRenderlayer(self,RenderLayerName=''):
		shadersList=[]
		if RenderLayerName in self.zwfOutputRenderpassControlDatas:
			if 'AllObjects' in self.zwfOutputRenderpassControlDatas[RenderLayerName]:
				objs=self.zwfOutputRenderpassControlDatas[RenderLayerName]['AllObjects']
				if len(objs):
					objshapes=cmds.listRelatives(objs,ad=True,pa=True,type=['mesh','subdiv','nurbsSurface'])
					if objshapes!=None:
						objshapes=self.getNewObjshapesList(objshapes)
						if objshapes:
							#for singleshape in objshapes:
							shaderSGs=cmds.listConnections(objshapes,s=False,type='shadingEngine')
							if shaderSGs!=None:
								shaderSGs=self.deleteDInList(shaderSGs)
								shaders=[]
								if shaderSGs:
									for singleSG in shaderSGs:
										shade=cmds.listConnections('%s.surfaceShader'%singleSG,d=False)
										if shade :
											[shaders.append(cc) for cc in shade]
										else:
											miShade=cmds.listConnections('%s.miMaterialShader'%singleSG,d=False)
											if miShade:
												[shaders.append(xx) for xx in miShade]
								if len(shaders):
									shaders=self.deleteDInList(shaders)
									for single in shaders:
										if single!='lambert1' and single!='particleCloud1':
											shadersList.append(single)
		return shadersList

	def connectionSomePassToMyShader(self,shadername, shaderQY, shaderTD, sPassTD, samples,spread,maxDistance, outputMode,falloff,idInclexcl,renderLayer):
		allshaderList=self.getShadersFromRenderlayer(renderLayer)
		if not len(allshaderList):
			cmds.warning('no shaders in %s.'%renderLayer)
		else:
			cmd='mrCreateCustomNode -%s "" %s'%(shaderQY,shadername)
			ss=mel.eval(cmd)
			ssd=cmds.listConnections(ss,s=False,type='shadingEngine')
			if ssd!=None:
				cmds.delete(ssd)
	#		if cmds.nodeType(ss)=='zdepth':
				#cmds.setAttr("%s.invert"%ss, 1)
			else:
				pass
			if cmds.nodeType(ss)=='mib_amb_occlusion':
				cmds.setAttr("%s.samples"%ss ,samples)
				cmds.setAttr("%s.spread"%ss ,spread)
				cmds.setAttr("%s.max_distance"%ss ,maxDistance)
				cmds.setAttr("%s.output_mode"%ss, outputMode)
				cmds.setAttr("%s.id_inclexcl"%ss,idInclexcl )
				cmds.setAttr("%s.falloff"%ss,falloff)
			elif cmds.nodeType(ss)=='p_facing_ratio':
				cmds.setAttr("%s.color1"%ss,0 ,0, 0, type="double3" )
				cmds.setAttr("%s.color2"%ss,1 ,1, 1, type="double3" )
			else:
				pass
			j=0
			for single in allshaderList:
				if cmds.objExists('%s.%s'%(single,shaderTD)):
					j+=1
					conmember=cmds.connectionInfo('%s.%s'%(single,shaderTD),id=True)
					if not conmember:
						cmds.connectAttr('%s.%s'%(ss , sPassTD),'%s.%s'%(single,shaderTD))
#					else:
#						cmds.delete(cmds.listConnections('%s.%s'%(single,shaderTD),d=False)[0])
#						cmds.connectAttr('%s.%s'%(ss , sPassTD),'%s.%s'%(single,shaderTD))
			if j==0:
				cmds.delete(ss)

	def createRenderpasses(self,passName, passType, passN, dataType, number,renderLayer):
		CPassName=cmds.shadingNode('renderPass',n=passName,asRendering=True)
		cmds.setRenderPassType(CPassName,type=passType)
		cmds.addAttr(CPassName,ln="renderpassType",dt="string")
		cmds.setAttr ("%s.renderpassType"%CPassName,passType,type='string',l=True)
		cmds.setAttr('%s.numChannels'%CPassName, passN)
		cmds.setAttr('%s.frameBufferType'%CPassName ,dataType)
		if cmds.objExists("%s.maxRefractionLevel"%CPassName ):
			cmds.setAttr("%s.maxRefractionLevel"%CPassName ,10)
		if not passType in ['SPEC', 'REFL', 'REFR','VOLLIT','VOLOBJ','VOLSCN']:
			cmds.setAttr ("%s.transparentAttenuation"%CPassName,number)
		cmds.setAttr ("%s.useTransparency"%CPassName,1)
		cmds.connectAttr('%s.renderPass'%renderLayer, '%s.owner'%CPassName, nextAvailable=True)
		return CPassName

	def createWriteToColorBuffer(self,passName,shaderout,renderLayer):
		ColorBufferlist=[]
		allshaderList=self.getShadersFromRenderlayer(renderLayer)
		if not len(allshaderList):
			cmds.warning('no shaders in %s.'%renderLayer)
		else:
			for single in allshaderList:
				if cmds.objExists('%s.%s'%(single,shaderout)):
					ColorBufferName=mel.eval('mrCreateCustomNode -asUtility "" writeToColorBuffer')
					ColorBufferName=cmds.rename(ColorBufferName,"%s_ColorBuffer_%s"%(single,passName))
					cmds.connectAttr('%s.message'%single, '%s.evaluationPassThrough'%ColorBufferName,f=True)
					if cmds.objExists("%s.refractions"%single):
						if cmds.getAttr("%s.refractions"%single):
							reverse=cmds.listConnections('%s.transparency'%single,s=False,type='reverse')
							if reverse==None:
								newreverse=cmds.shadingNode('reverse', asUtility=True)
								cmds.connectAttr('%s.transparency'%single, '%s.input'%newreverse,f=True)
							else:
								newreverse=reverse[0]
							multiplyD=cmds.shadingNode('multiplyDivide',asUtility=True)
							cmds.connectAttr('%s.%s'%(single,shaderout), '%s.input1'%multiplyD,f=True)
							cmds.connectAttr('%s.output'%newreverse, '%s.input2'%multiplyD,f=True)
							shn=multiplyD
							out='output'
						else:
							shn=single
							out=shaderout
					else:
						shn=single
						out=shaderout
					cmds.connectAttr('%s.%s'%(shn,out), '%s.color'%ColorBufferName,f=True)
					ColorBufferlist.append(ColorBufferName)
					vBox=cmds.checkBox(self.cBox,q=True,v=True)
					if vBox:
						if shaderout in ['facingRatio','worldNormal','ambientOcclusion']:
							if cmds.objExists('%s.normalCamera'%single):
								bumpNode=cmds.listConnections('%s.normalCamera'%single,d=False)
								if bumpNode:
									if cmds.listConnections('%s.bumpValue'%bumpNode[0],d=False):
										lambert_n=cmds.shadingNode('lambert',asShader=True,n='%s_%s_output'%(single,shaderout))
										cmds.addAttr(lambert_n,ln="TMAD_DELETE",at='bool')
										cmds.setAttr('%s.TMAD_DELETE'%lambert_n,1)
										cmds.setAttr('%s.ambientColor'%lambert_n,1,1,1,type='double3')
										cmds.setAttr('%s.diffuse'%lambert_n,0)
										cmds.connectAttr('%s.normalCamera'%single, '%s.normalCamera'%lambert_n)
										conn=cmds.listConnections('%s.%s'%(single,shaderout),s=False,p=True)
										if conn:
											try:
												cmds.connectAttr('%s.%s'%(single,shaderout), '%s.color'%lambert_n,f=True)
												cmds.connectAttr('%s.outColor'%lambert_n,conn[0],f=True)
											except: pass
		return ColorBufferlist

	def connectionRenderPassAndColorBuffer(self,passName, passType, passN, dataType, number,shaderout,renderLayer):
		color_pass=self.createRenderpasses(passName, passType, passN, dataType, number,renderLayer)
		CBL=self.createWriteToColorBuffer(color_pass,shaderout,renderLayer)
		if len(CBL):
			for each in CBL:
				cmds.connectAttr("%s.message"%color_pass, "%s.renderPass"%each)
		else:
			cmds.delete(color_pass)
		return color_pass

	def createPass(self,renderLayer):
		renderpasses=self.zwfOutputRenderpassControlDatas[renderLayer]['Renderpasses']
		#=======================================Color==============================================================================
		if 'Color' in renderpasses:
			Color_pass=self.connectionRenderPassAndColorBuffer(renderpasses['Color']['Name'], 'CSTCOL', 3, renderpasses['Color']['DataType'], 1,'color',renderLayer)
		#=======================================DiffuseColor==============================================================================
		if 'DiffuseColor' in renderpasses:
			Diffuse_pass=self.createRenderpasses(renderpasses['DiffuseColor']['Name'], 'DIFF', 3, renderpasses['DiffuseColor']['DataType'], 1,renderLayer)
		#=======================================Light==============================================================================
		if 'Light' in renderpasses:
			Light_pass=self.createRenderpasses(renderpasses['Light']['Name'], 'DIRIRR', 3, renderpasses['Light']['DataType'], 1,renderLayer)
		#=======================================Specular==============================================================================
		if 'Indirect' in renderpasses:
			Indirect_pass=self.createRenderpasses(renderpasses['Indirect']['Name'], 'INDIRR', 3, renderpasses['Indirect']['DataType'], 1,renderLayer)
		#=======================================Specular==============================================================================
		if 'Specular' in renderpasses:
			Specular_pass=self.createRenderpasses(renderpasses['Specular']['Name'], 'SPEC', 3, renderpasses['Specular']['DataType'], 0,renderLayer)
		#=======================================Ambient Color==============================================================================
		if 'AmbientColor' in renderpasses:
			AmbientColor_pass=self.connectionRenderPassAndColorBuffer(renderpasses['AmbientColor']['Name'], 'CSTCOL', 3, renderpasses['AmbientColor']['DataType'], 1,'ambientColor',renderLayer)
		#=======================================Incandescence==============================================================================
		if 'Incandescence' in renderpasses:
			Incandescence_pass=self.connectionRenderPassAndColorBuffer(renderpasses['Incandescence']['Name'], 'CSTCOL', 3, renderpasses['Incandescence']['DataType'], 0,'incandescence',renderLayer)
		#=======================================SSS==============================================================================
		if'SSS' in renderpasses:
			SSS_pass=self.connectionRenderPassAndColorBuffer(renderpasses['SSS']['Name'], 'CSTCOL', 4, renderpasses['SSS']['DataType'], 1,'sss',renderLayer)
		#=======================================Reflection==============================================================================
		if 'Reflection' in renderpasses:
			Reflection_pass=self.createRenderpasses(renderpasses['Reflection']['Name'], 'REFL', 3, renderpasses['Reflection']['DataType'], 0,renderLayer)
		#=======================================Refration==============================================================================
		if 'Refraction' in renderpasses:
			Refraction_pass=self.createRenderpasses(renderpasses['Refraction']['Name'], 'REFR', 4, renderpasses['Refraction']['DataType'], 0,renderLayer)
		#=======================================GlowSource==============================================================================
		if 'GlowSource' in renderpasses:
			GlowSource_pass=self.createRenderpasses(renderpasses['GlowSource']['Name'], 'GLORAW', 3, renderpasses['GlowSource']['DataType'], 0,renderLayer)
		#=======================================VolumeLight==============================================================================
		if 'VolumeLight' in renderpasses:
			Refraction_pass=self.createRenderpasses(renderpasses['VolumeLight']['Name'], 'VOLLIT', 3, renderpasses['VolumeLight']['DataType'], 0,renderLayer)
		#=======================================VolumeObject==============================================================================
		if 'VolumeObject' in renderpasses:
			Refraction_pass=self.createRenderpasses(renderpasses['VolumeObject']['Name'], 'VOLOBJ', 3, renderpasses['VolumeObject']['DataType'], 0,renderLayer)
		#=======================================VolumeScene==============================================================================
		if 'VolumeScene' in renderpasses:
			Refraction_pass=self.createRenderpasses(renderpasses['VolumeScene']['Name'], 'VOLSCN', 3, renderpasses['VolumeScene']['DataType'], 0,renderLayer)
		#=======================================Special Specular==============================================================================
		if'AddSpecular' in renderpasses:
			AddSpecular_pass=self.connectionRenderPassAndColorBuffer(renderpasses['AddSpecular']['Name'], 'CSTCOL', 3, renderpasses['AddSpecular']['DataType'], 0,'addSpecular',renderLayer)
		#=======================================Special Reflection==============================================================================
		if'AddReflection' in renderpasses:
			AddReflection_pass=self.connectionRenderPassAndColorBuffer(renderpasses['AddReflection']['Name'], 'CSTCOL', 3, renderpasses['AddReflection']['DataType'], 0,'addReflection',renderLayer)
		#=======================================AO==============================================================================
		if'AO' in renderpasses:
			self.connectionSomePassToMyShader('mib_amb_occlusion', 'asTexture', 'ambientOcclusion', 'outValue', 45,0.8,25,0,0.5,-1,renderLayer)
			AO_pass=self.connectionRenderPassAndColorBuffer(renderpasses['AO']['Name'], 'CSTCOL', 3, renderpasses['AO']['DataType'], 1,'ambientOcclusion',renderLayer)
		#=======================================worldNormal==============================================================================
		if'WorldNormal' in renderpasses:
			self.connectionSomePassToMyShader('mib_amb_occlusion', 'asTexture', 'worldNormal', 'outValue', 0, 0,0,3,1,0,renderLayer)
			worldNormal_pass=self.connectionRenderPassAndColorBuffer(renderpasses['WorldNormal']['Name'], 'CSTCOL', 3, renderpasses['WorldNormal']['DataType'], 1,'worldNormal',renderLayer)
		#=======================================Zdepth==============================================================================
		if'Zdepth' in renderpasses:
			self.connectionSomePassToMyShader('zdepth', 'asShader', 'zdepth', 'output', 0, 0,0,0,0,0,renderLayer)
			Zdepth_pass=self.connectionRenderPassAndColorBuffer(renderpasses['Zdepth']['Name'], 'CSTCOL', 3, renderpasses['Zdepth']['DataType'], 1,'zdepth',renderLayer)
		#=======================================Facing Ratio==============================================================================
		if'FacingRatio' in renderpasses:
			self.connectionSomePassToMyShader('p_facing_ratio', 'asShader', 'facingRatio', 'outValue', 0, 0,0,0,0,0,renderLayer)
			FacingRatio_pass=self.connectionRenderPassAndColorBuffer(renderpasses['FacingRatio']['Name'], 'CSTCOL', 3, renderpasses['FacingRatio']['DataType'], 1,'facingRatio',renderLayer)
		#=======================================3DMV==============================================================================
		if'MV' in renderpasses:
			self.connectionSomePassToMyShader('p_motion_to_rgb', 'asShader', 'mv', 'outValue', 0, 0,0,0,0,0,renderLayer)
			MV_pass=self.connectionRenderPassAndColorBuffer(renderpasses['MV']['Name'], 'CSTCOL', 3, renderpasses['MV']['DataType'], 1,'mv',renderLayer)
			try:
				cmds.setAttr("miDefaultOptions.motionBlur",2)
				cmds.setAttr("miDefaultOptions.shutterDelay" ,1)
				cmds.setAttr("mentalrayGlobals.exportMotionOffset",1)
				cmds.setAttr("miDefaultOptions.motionBlurShadowMaps", 0)
			except: pass
		#=======================================Another One==============================================================================
		if'AssetObjectID' in renderpasses:
			AnotherOne_pass=self.connectionRenderPassAndColorBuffer(renderpasses['AssetObjectID']['Name'], 'CSTCOL', 3, renderpasses['AssetObjectID']['DataType'], 1,'assetObjectID',renderLayer)
		#=======================================Another Two==============================================================================
		if'MaterialID' in renderpasses:
			AnotherTwo_pass=self.connectionRenderPassAndColorBuffer(renderpasses['MaterialID']['Name'], 'CSTCOL', 3, renderpasses['MaterialID']['DataType'], 1,'materialID',renderLayer)

	def BeforeCreateSetingsdeleteAll(self):
		cmds.editRenderLayerGlobals(currentRenderLayer='defaultRenderLayer')
		renderlayers=cmds.ls(type='renderLayer')
		if len(renderlayers): 
			for sss in renderlayers:
				if sss!='defaultRenderLayer':
					try:
						cmds.delete(sss)
					except: pass
		writeToColorBuffers=cmds.ls(type='writeToColorBuffer')
		if len(writeToColorBuffers):
			for single in writeToColorBuffers:
				try:
					cmds.delete(single)
				except: pass
		renderPasses=cmds.ls(type='renderPass')
		if len(renderPasses):
			for each in renderPasses:
				try:
					cmds.delete(each)
				except: pass
		passContributionMaps=cmds.ls(type='passContributionMap')
		if len(passContributionMaps):
			for s in passContributionMaps:
				try:
					cmds.delete(s)
				except: pass
		all_lamberts=cmds.ls(type='lambert')
		if all_lamberts:
			for sin_lambert in all_lamberts:
				if cmds.objExists('%s.TMAD_DELETE'%sin_lambert):
					if cmds.getAttr('%s.TMAD_DELETE'%sin_lambert):
						try:
							cmds.delete(sin_lambert)
						except: pass
		mat=self.getAllMyShader()
		if len(mat):
			for e in mat:
				try:
					if cmds.nodeType(e)=='p_motion_to_rgb':
						continue
				except: pass
				try:
					reverses=cmds.listConnections(e,s=False,type='reverse')
					if reverses!=None:
						for x in reverses:
							multiplyDivides=cmds.listConnections(x,s=False,type='multiplyDivide')
							if multiplyDivides!=None:
								cmds.delete(multiplyDivides)
						cmds.delete(reverses)
				except: pass
				if cmds.objExists('%s.mv'%e):
					MVs=cmds.listConnections('%s.mv'%e,d=False,type='p_motion_to_rgb')
					if MVs!=None:
						try:
							cmds.delete(MVs)
						except: pass
				if cmds.objExists('%s.ambientOcclusion'%e):
					AOs=cmds.listConnections('%s.ambientOcclusion'%e,d=False,type='mib_amb_occlusion')
					if AOs!=None:
						try:
							cmds.delete(AOs)
						except: pass
				if cmds.objExists('%s.worldNormal'%e):
					WNs=cmds.listConnections('%s.worldNormal'%e,d=False,type='mib_amb_occlusion')
					if WNs!=None:
						try:
							cmds.delete(WNs)
						except: pass
				if cmds.objExists('%s.zdepth'%e):
					ZDs=cmds.listConnections('%s.zdepth'%e,d=False,type='zdepth')
					if ZDs!=None:
						try:
							cmds.delete(ZDs)
						except: pass
				if cmds.objExists('%s.facingRatio'%e):
					FRs=cmds.listConnections('%s.facingRatio'%e,d=False,type='facingRatio')
					if FRs!=None:
						try:
							cmds.delete(FRs)
						except: pass
	def deleteIntermediateObjects(self):
		all=cmds.ls(type='geometryVarGroup')
		for single in all:
			if single[:31]=='RenderLayer_IntermediateObject_':
				if cmds.lockNode(single,q=True,l=True)[0]:
					cmds.lockNode(single,l=False)
				cmds.delete(single)

	def CreateIntermediateObject(self,objectName,objs):
		if not cmds.objExists(objectName):
			interme=cmds.createNode('geometryVarGroup',n=objectName)
			cmds.setAttr('%s.visibility'%interme,0)
		else:
			interme=objectName
		attrlist=['primaryVisibility','miTransparencyCast','receiveShadows','visibleInReflections','visibleInRefractions','castsShadows','overrideEnabled','overrideDisplayType','overrideShading']
		for attrName in attrlist:
			if not cmds.objExists('%s.%s'%(interme,attrName)):
				cmds.addAttr(interme,ln=attrName,at='bool')
				cmds.setAttr('%s.%s'%(interme,attrName),1)
		#print u'\n\n=================================================" %s "扫描第%d开始================================================='%(rl,i)
		for single in objs:
			print single
			for attrName_n in attrlist:
				try:
					cmds.connectAttr('%s.%s'%(interme,attrName_n),'%s.%s'%(single,attrName_n))
				except:pass

	def createSetings(self,*args):
		self.BeforeCreateSetingsdeleteAll()
		self.deleteIntermediateObjects()
		renderlayers=self.zwfOutputRenderpassControlDatas.keys()
		layersize=len(renderlayers)
		if layersize:
			amount=0
			cmds.progressWindow(title='create progress',progress=amount,status='Sleeping: 0%',isInterruptable=True )
			for single in renderlayers:
				if cmds.progressWindow( query=True, isCancelled=True ) :
					break
#=================================================================================创建renderLayer============================================================================================
				renderL=cmds.createRenderLayer(name=single, number=True, empty=True)
				layer=self.zwfOutputRenderpassControlDatas[single]
				if 'PNSObjects' in layer:
					pnsobjs=layer['PNSObjects']
				else:
					pnsobjs=[]
				allobjs=layer['AllObjects']
				if len(allobjs):
					cmds.editRenderLayerMembers(renderL,allobjs,nr=True)
#===========================================================================================link关系=========================================================================================================
				anotherlayers=self.getAnotherRenderLayer(single)
				if len(anotherlayers):
					if 'Reflection' in layer:
						reflectionlayers=layer['Reflection']
					else:
						reflectionlayers=[]
					if 'Refraction' in layer:
						refractionlayers=layer['Refraction']
					else:
						refractionlayers=[]
					if 'Shadow' in layer:
						shadowayers=layer['Shadow']
					else:
						shadowayers=[]
					for eachlayer in anotherlayers:
						if eachlayer in reflectionlayers or eachlayer in refractionlayers or eachlayer in shadowayers :
							if 'AllObjects' in self.zwfOutputRenderpassControlDatas[eachlayer]:
								anotherLayerAllobj=self.zwfOutputRenderpassControlDatas[eachlayer]['AllObjects']
								if len(anotherLayerAllobj):
									cmds.editRenderLayerMembers(single,anotherLayerAllobj)
									anotherAllShapes=cmds.listRelatives(anotherLayerAllobj,ad=True,type=('mesh','subdiv','nurbsSurface'),pa=True)
									if anotherAllShapes:
										anotherAllShapes=self.getNewObjshapesList(anotherAllShapes)
									if anotherAllShapes:
										cmds.editRenderLayerGlobals(currentRenderLayer='defaultRenderLayer')
										IntermediateObjectName='RenderLayer_IntermediateObject_%s'%eachlayer
										if not cmds.objExists(IntermediateObjectName):
											print u'=================================================" %s "扫描开始================================================='%eachlayer
											self.CreateIntermediateObject(IntermediateObjectName,anotherAllShapes)
											print u'=================================================" %s "扫描结束================================================='%eachlayer
											'''
											jj=1
											print u'\n\n=================================================" %s "将进行9次扫描=================================================='%eachlayer
											for mmaa in ['primaryVisibility','miTransparencyCast','receiveShadows','visibleInReflections','visibleInRefractions','castsShadows','overrideEnabled','overrideDisplayType','overrideShading']:
												self.CreateIntermediateObject(mmaa,IntermediateObjectName,anotherAllShapes,eachlayer,jj)
												jj+=1
											print u'\n\n=================================================" %s "扫描结束================================================='%eachlayer'''
										cmds.editRenderLayerMembers(single,IntermediateObjectName)
										#cmds.editRenderLayerMembers(eachlayer,IntermediateObjectName,nr=True)
										cmds.editRenderLayerGlobals(currentRenderLayer=renderL)
										
										cmds.editRenderLayerAdjustment ("%s.primaryVisibility"%IntermediateObjectName,layer=single)
										cmds.setAttr("%s.primaryVisibility"%IntermediateObjectName, 0)
										cmds.editRenderLayerAdjustment ("%s.miTransparencyCast"%IntermediateObjectName,layer=single)
										cmds.setAttr("%s.miTransparencyCast"%IntermediateObjectName, 0)
										cmds.editRenderLayerAdjustment ("%s.receiveShadows"%IntermediateObjectName,layer=single)
										cmds.setAttr("%s.receiveShadows"%IntermediateObjectName ,0)
										cmds.editRenderLayerAdjustment ("%s.visibleInReflections"%IntermediateObjectName,layer=single)
										if eachlayer in reflectionlayers :
											cmds.setAttr("%s.visibleInReflections"%IntermediateObjectName ,1)
										else:
											cmds.setAttr("%s.visibleInReflections"%IntermediateObjectName ,0)
										cmds.editRenderLayerAdjustment ("%s.visibleInRefractions"%IntermediateObjectName,layer=single)
										if eachlayer in refractionlayers:
											cmds.setAttr("%s.visibleInRefractions"%IntermediateObjectName ,1)
										else:
											cmds.setAttr("%s.visibleInRefractions"%IntermediateObjectName ,0)
										cmds.editRenderLayerAdjustment ("%s.castsShadows"%IntermediateObjectName,layer=single)
										if eachlayer in shadowayers :
											cmds.setAttr("%s.castsShadows"%IntermediateObjectName ,1)
										else:
											cmds.setAttr("%s.castsShadows"%IntermediateObjectName ,0)
										cmds.editRenderLayerAdjustment ("%s.overrideEnabled"%IntermediateObjectName,layer=single)
										cmds.setAttr("%s.overrideEnabled"%IntermediateObjectName,1)
										cmds.editRenderLayerAdjustment ("%s.overrideDisplayType"%IntermediateObjectName,layer=single)
										cmds.setAttr("%s.overrideDisplayType"%IntermediateObjectName,2)
										cmds.editRenderLayerAdjustment ("%s.overrideShading"%IntermediateObjectName,layer=single)
										cmds.setAttr("%s.overrideShading"%IntermediateObjectName,0)
										if not cmds.lockNode(IntermediateObjectName,q=True,l=True)[0]:
											cmds.lockNode(IntermediateObjectName,l=True)
										#[self.connectionAttrIMOtoOBJS(ssxx,IntermediateObjectName,anotherAllShapes) for ssxx in ['primaryVisibility','miTransparencyCast','receiveShadows','visibleInReflections','visibleInRefractions','castsShadows']]
										'''
										for singleShape in anotherAllShapes:
											print singleShape
											cmds.editRenderLayerGlobals(currentRenderLayer=renderL)
											cmds.editRenderLayerAdjustment ("%s.primaryVisibility"%singleShape,layer=single)
											cmds.setAttr("%s.primaryVisibility"%singleShape, 0)
											cmds.editRenderLayerAdjustment ("%s.miTransparencyCast"%singleShape,layer=single)
											cmds.setAttr("%s.miTransparencyCast"%singleShape, 0)
											cmds.editRenderLayerAdjustment ("%s.receiveShadows"%singleShape,layer=single)
											cmds.setAttr("%s.receiveShadows"%singleShape ,0)
											cmds.editRenderLayerAdjustment ("%s.visibleInReflections"%singleShape,layer=single)
											if eachlayer in reflectionlayers :
												cmds.setAttr("%s.visibleInReflections"%singleShape ,1)
											else:
												cmds.setAttr("%s.visibleInReflections"%singleShape ,0)
											cmds.editRenderLayerAdjustment ("%s.visibleInRefractions"%singleShape,layer=single)
											if eachlayer in refractionlayers:
												cmds.setAttr("%s.visibleInRefractions"%singleShape ,1)
											else:
												cmds.setAttr("%s.visibleInRefractions"%singleShape ,0)
											cmds.editRenderLayerAdjustment ("%s.castsShadows"%singleShape,layer=single)
											if eachlayer in shadowayers :
												cmds.setAttr("%s.castsShadows"%singleShape ,1)
											else:
												cmds.setAttr("%s.castsShadows"%singleShape ,0)'''
#=================================================================================创建addLgihtPasses=========================================================================================================
				if 'AllAddlightpasses' in layer:
					addlightpasses=layer['AllAddlightpasses']
					lightpasses=addlightpasses.keys()
					if len(lightpasses):
						for each in lightpasses:
							addLP=cmds.createNode('passContributionMap', n=each, skipSelect=True)
							cmds.connectAttr('%s.passContributionMap'%renderL, '%s.owner'%addLP,na=True )
							if len(each):
								for e in addlightpasses[each]:
									cmds.connectAttr('%s.message'%e, '%s.owner'%addLP,na=True )
									li=cmds.listRelatives(e,c=True,type='light',pa=True)[0]
									cmds.connectAttr('%s.message'%li,'%s.light'%addLP,na=True)
							if len(pnsobjs):
								for s in pnsobjs:
									try:
										cmds.connectAttr('%s.message'%s, '%s.owner'%addLP,na=True )
									except: pass
#==================================================================Addlightpass_renderPass============================================================================================================
							passname='%s_light'%addLP
							CPassName=cmds.shadingNode('renderPass',n=passname,asRendering=True)
							cmds.setRenderPassType(CPassName,type="DIRIRR")
							cmds.setAttr('%s.numChannels'%CPassName, 3)
							cmds.setAttr('%s.frameBufferType'%CPassName ,256)
							cmds.setAttr("%s.maxRefractionLevel"%CPassName ,10)
							cmds.setAttr ("%s.useTransparency"%CPassName,1)
							cmds.setAttr ("%s.transparentAttenuation"%CPassName,1)
							cmds.connectAttr('%s.renderPass'%renderL, '%s.owner'%CPassName, nextAvailable=True)
							cmds.connectAttr('%s.message'%CPassName, '%s.renderPass'%addLP, nextAvailable=True)
#=================================================================================创建renderPasses=======================================================================================
				if 'Renderpasses' in layer:
					self.createPass(renderL)
				amount+=100/layersize
				amountInt=int(amount)
				cmds.progressWindow( edit=True, progress=amount, status=('Sleeping: ' + `amountInt` + '%' ) )
		cmds.textScrollList('ritsl_V2',e=True,da=True)
		cmds.textScrollList('ritsl_V2',e=True,si='defaultRenderLayer')
		self.selectrenderLayer_C()
#=================================================================================将内部数据库转到外部=======================================================================================
		self.saveOutputRenderpassControlDatas()
		cmds.progressWindow( edit=True, progress=100, status=('Sleeping: 100%' ) )
		cmds.progressWindow(endProgress=1)

	#//////////////////////////////////////////////////////////////////matteMask Parts//////////////////////////////////////////////////////////////////////////////////////////////////////////
	def fromMi_blinnGetObj(self,mi_blinn=''):
		getallObjList=[]
#		allmi_blinn=self.getAllMyShader()
		tr=cmds.getAttr("%s.transparencyR"%mi_blinn)
		tg=cmds.getAttr("%s.transparencyG"%mi_blinn)
		tb=cmds.getAttr("%s.transparencyB"%mi_blinn)
		if tr!=0 or tg!=0 or tb!=0:
			mi_blinn_g=cmds.listConnections(mi_blinn,s=False,type='shadingEngine')
			if mi_blinn_g!=None:
				for each in mi_blinn_g:
					objs=cmds.listConnections(each,d=False,sh=1)
					objs=cmds.ls(objs,type=['mesh','subdiv','nurbsSurface'])
					if objs:
						objs=self.getNewObjshapesList(objs)
					if objs:
						[getallObjList.append(s) for s in objs]
		return getallObjList
	def getShapeFromList(self,listname=[]):
		nlist=[]
		if len(listname):
			single=cmds.listRelatives(listname,ad=True,pa=True,type=['mesh','subdiv','nurbsSurface'])
			if single:
				single=self.getNewObjshapesList(single)
			if single:
				[nlist.append(each)for each in single]
		return nlist
	def createlambertmask(self,oldshader,newshader):
		cmds.setAttr("%s.color"%newshader, 0, 0, 0, type='double3')
		ci_all=cmds.connectionInfo('%s.transparency'%oldshader, isDestination=True)
		if ci_all:
			all=cmds.listConnections('%s.transparency'%oldshader,d=False,p=True)[0]
			cmds.connectAttr (all, '%s.transparency'%newshader,f=True)
		ci_r=cmds.connectionInfo('%s.transparencyR'%oldshader, isDestination=True)
		if ci_r:
			r=cmds.listConnections('%s.transparencyR'%oldshader,d=False,p=True)
			if r!=None:
				cmds.connectAttr (r[0], '%s.transparencyR'%newshader,f=True)
		ci_g=cmds.connectionInfo('%s.transparencyG'%oldshader, isDestination=True)
		if ci_g:
			g=cmds.listConnections('%s.transparencyG'%oldshader,d=False,p=True)
			if g!=None:
				cmds.connectAttr (g[0], '%s.transparencyG'%newshader,f=True)
		ci_b=cmds.connectionInfo('%s.transparencyB'%oldshader, isDestination=True)
		if ci_b:
			b=cmds.listConnections('%s.transparencyB'%oldshader,d=False,p=True)
			if b!=None:
				cmds.connectAttr (b[0], '%s.transparencyB'%newshader,f=True)
		if ci_all!=1 and ci_r!=1 and ci_g!=1 and ci_b!=1:
			number_r=cmds.getAttr('%s.transparencyR'%oldshader)
			number_g=cmds.getAttr('%s.transparencyG'%oldshader)
			number_b=cmds.getAttr('%s.transparencyB'%oldshader)
			cmds.setAttr('%s.transparency'%newshader, number_r, number_g, number_b,type='double3')
	def createMatteMask(self,*args):
		changjingts=cmds.confirmDialog( title=u'场景保存提示', message='您当前的场景保存了吗？',b=[u'继续',u'取消'])
		if changjingts==u'取消':
			return
#		matteList={'red':[],'green':[],'blue':[],'alpha':[]}
		matteName=cmds.textFieldGrp('matteMask_V2',q=True, tx=True)
#		sel_renderLayer=cmds.textScrollList('ritsl_V2',q=True,si=True)
		if len(matteName):
			sceneName=self.getsceneName()
			sn_dirN=os.path.dirname(sceneName)
			sn_ext=os.path.basename(sceneName).split('.')[-1]
			matteSceneName='%s/%s.%s'%(sn_dirN,matteName,sn_ext)
			if len(self.zwfOutputRenderpassControlDatas):
				matteLinks={}
				for singleLayer in self.zwfOutputRenderpassControlDatas:
					if 'Matte' in self.zwfOutputRenderpassControlDatas[singleLayer]:
						if len(self.zwfOutputRenderpassControlDatas[singleLayer]['Matte']):
							matteLinks[singleLayer]=self.zwfOutputRenderpassControlDatas[singleLayer]['Matte']
				if len(matteLinks):
					cmds.editRenderLayerGlobals(currentRenderLayer='defaultRenderLayer')
					for single in self.zwfOutputRenderpassControlDatas:
						if 'AllObjects' in self.zwfOutputRenderpassControlDatas[single]:
							Layerobjs=self.zwfOutputRenderpassControlDatas[single]['AllObjects']
							if len(Layerobjs):
								LayerobjShapes=self.getShapeFromList(Layerobjs)
								if len(LayerobjShapes):
									shaders=self.getShadersFromRenderlayer(single)
									if len(shaders):
										for each in shaders:
											red_lambert=cmds.shadingNode('lambert',asShader=True)
											red_lambert_G=cmds.sets(renderable=True, noSurfaceShader=True, empty=True, name='%sSG'%red_lambert)
											cmds.connectAttr('%s.outColor'%red_lambert, '%s.surfaceShader'%red_lambert_G)
											if cmds.objExists('%s.transparency'%each):
												self.createlambertmask(each,red_lambert)
											red_invert=cmds.shadingNode('reverse',asUtility=True) 
											cmds.connectAttr('%s.transparency'%red_lambert, '%s.input'%red_invert,f=True)
											red_multiplyDivide=cmds.shadingNode('multiplyDivide',asUtility=True)
											cmds.connectAttr('%s.output'%red_invert, '%s.input1'%red_multiplyDivide, force =True)
											cmds.connectAttr ('%s.output'%red_multiplyDivide,'%s.incandescence'%red_lambert)
											sg=cmds.listConnections(each,s=False,type='shadingEngine')[0]
											#disp=cmds.listConnections('%s.displacementShader'%sg,d=False,type='displacementShader',p=True)
											disp=cmds.listConnections('%s.displacementShader'%sg,d=False,p=True)
											if disp:
												cmds.connectAttr(disp[0],'%s.displacementShader'%red_lambert_G,f=True)
											shapes=cmds.listConnections(sg,d=False,sh=True)
											shapes=cmds.ls(shapes,type=['mesh','subdiv','nurbsSurface'])
											for ss in shapes :
												if ss in LayerobjShapes:
													cmds.sets(ss, e=True, forceElement=red_lambert_G)
					for eachmatte in matteLinks:
						#print eachmatte
						otherlayers=matteLinks[eachmatte]
						renderLayer=cmds.createRenderLayer(number=True, empty=True)
						eachobjs=self.zwfOutputRenderpassControlDatas[eachmatte]['PNSObjects']
						cmds.editRenderLayerMembers(renderLayer,eachobjs,nr=True)
						eachshaders=self.getShadersFromRenderlayer(eachmatte)
						#print eachshaders
						if len(eachshaders):
							cmds.editRenderLayerGlobals(currentRenderLayer=renderLayer)
							for sinleshade in eachshaders:
								#print sinleshade
								MD=cmds.listConnections('%s.incandescence'%sinleshade,d=False,type='multiplyDivide')[0]
								cmds.editRenderLayerAdjustment ("%s.input2"%MD,layer=renderLayer)
								cmds.setAttr("%s.input2Y"%MD, 0)
								cmds.setAttr("%s.input2Z"%MD, 0)
						NrenderLayerName='%s_'%eachmatte
						for singleotherlayer in otherlayers:
							NrenderLayerName='%s%s_'%(NrenderLayerName,singleotherlayer)
							singleobjs=self.zwfOutputRenderpassControlDatas[singleotherlayer]['PNSObjects']
							cmds.editRenderLayerMembers(renderLayer,singleobjs,nr=True)
							singleshaders=self.getShadersFromRenderlayer(singleotherlayer)
							if len(singleshaders):
								for eshader in singleshaders:
									#print singleshaders
									NMD=cmds.listConnections('%s.incandescence'%eshader,d=False,type='multiplyDivide')[0]
									cmds.editRenderLayerAdjustment ("%s.input2"%NMD,layer=renderLayer)
									cmds.setAttr("%s.input2X"%NMD, 0)
									cmds.setAttr("%s.input2Z"%NMD, 0)
						NrenderLayerName=NrenderLayerName[:-1]
						cmds.rename(renderLayer,NrenderLayerName)
					cmds.delete(self.zwfOutputRenderpassControlDatas.keys())
					self.zwfOutputRenderpassControlDatas={}
					mel.eval('hyperShadePanelMenuCommand("hyperShadePanel1", "deleteUnusedNodes")')
					cmds.setAttr("defaultRenderGlobals.ifp",'%l/%l',type="string")
					cmds.fileInfo(rm='zwfOutputRenderpassFileInfoDatas')
					cmds.textScrollList('ritsl_V2',e=True,ra=True)
					cmds.textScrollList('ritsl_V2',e=True,a='defaultRenderLayer')
					self.selectrenderLayer_C()
					self.deleteIntermediateObjects()
					cmds.file(rename=matteSceneName)
					cmds.file(save=True, type='mayaAscii')
				else:
					cmds.warning('No MatteLink in Link textScrollList!')
			else:
				cmds.warning('No renderLayers in the scene!')
		else:
			 cmds.warning('no worlds in MatteMask_SceneName:.')
	def createAndAssignMaskShader(self,objList,shaderlist,name,r,g,b,a):
		mlist=[]
		if len(objList):
			[mlist.append(x) for x in objList if not x in shaderlist]
			if len(mlist):
				matteShader=cmds.shadingNode('surfaceShader',n='%s_matteMask'%name,asShader=True)
				matteShaderG=cmds.sets(renderable=True, noSurfaceShader=True, empty=True,name='%sSG'%matteShader)
				cmds.connectAttr('%s.outColor'%matteShader,'%s.surfaceShader'%matteShaderG)
				cmds.setAttr("%s.outColor"%matteShader, r, g, b, type='double3')
				cmds.setAttr("%s.outMatteOpacity"%matteShader, a, a, a, type='double3')
				cmds.sets(mlist,e=True,forceElement=matteShaderG)

	def createSaverenderPasssPresetsWin(self,*args):
		if cmds.window('saverenderpasspre_win_V2',ex=True):
			cmds.deleteUI('saverenderpasspre_win_V2')
		cmds.window('saverenderpasspre_win_V2',t='Save RenderPass Preset',wh=(300,60))
		m_saveRenderpasspre_c=cmds.columnLayout('main_saveRenderpasspre_col_V2',cat=["both",10],adj=True)
		cmds.textFieldGrp('saverenderpasspre_preName_V2',l='Preset name:',text='',cl2=['left','left'],cw2=[65,210])
		cmds.separator('s_saveRenderpasspre_o_V2', height=10, style='in' )
		cmds.button('saverenderpasspre_B_V2',l='Save RenderPass Preset',c=lambda *args:self.SaverenderPasssPreset_c('D:/maya_renderPasses/Presets'))
		cmds.window('saverenderpasspre_win_V2',e=True,wh=(300,60))
		cmds.showWindow('saverenderpasspre_win_V2')
	def editrenderPasssPresetsWin(self,*args):
		if cmds.window('editrenderPasssPresets_win_V2',ex=True):
			cmds.deleteUI('editrenderPasssPresets_win_V2')
		cmds.window('editrenderPasssPresets_win_V2',t='Edit RenderPass Presets',wh=(300,200))
		m_editrenderPasssPresets_c=cmds.columnLayout('main_editrenderPasssPresets_col_V2',cat=["both",3],adj=True)
		cmds.textScrollList('editrenderPasssPresets_ts_V2',allowMultiSelection=True,h=100)
		cmds.separator('s_editrenderPasssPresets_o_V2', height=10, style='in' )
		cmds.button('delete_B_V2',l='Delete',c=self.deleteRenderpassPresets)
		cmds.window('editrenderPasssPresets_win_V2',e=True,wh=(400,135))
		presets=self.getrenderPasspresets('D:/maya_renderPasses/Presets')
		if len(presets):
			cmds.textScrollList('editrenderPasssPresets_ts_V2',e=True,append=presets)
		cmds.showWindow('editrenderPasssPresets_win_V2')
	def addpopupMenu(self):
		cmds.menuItem('pre_popupI_srp_V2',l='Save renderPass Preset...',p='pre_popupI_V2',c=self.createSaverenderPasssPresetsWin)
		cmds.menuItem('pre_popupI_ep_V2',l='Edit Presets...',p='pre_popupI_V2',c=self.editrenderPasssPresetsWin)
		renderPPs=self.getrenderPasspresets('D:/maya_renderPasses/Presets')
		if len(renderPPs):
			cmds.menuItem('pre_popupI_do_V2',d=True,p='pre_popupI_V2')
			for single_menuitem in renderPPs:
				menuitem=createPpmenuItems()
				menuitem.setmenuitem(single_menuitem)
				menuitem.addmenuItems()
				menuitem.zwfOutputRenderpassControlDatas=self.zwfOutputRenderpassControlDatas
		prepop_menuItems=cmds.popupMenu('pre_popupI_V2',q=True,ni=True)
		if prepop_menuItems>2:
			cmds.button('presets_V2',e=True,l='Presets*')
		else:
			cmds.button('presets_V2',e=True,l='Presets')
	def updatepopupMenu(self,*args):
		cmds.popupMenu('pre_popupI_V2',e=True,dai=True)
		self.addpopupMenu()
	def SaverenderPasssPreset_c(self,path=''):
		selectRPs=cmds.textScrollList('rb_ritsl_V2',q=True,si=True)
		if selectRPs==None:
			return cmds.warning('No selected in Presets textScrollList!')
		saverenderpassname=cmds.textFieldGrp('saverenderpasspre_preName_V2',q=True,tx=True)
		if not len(saverenderpassname):
			return cmds.warning('No worlds in Preset name!')
		filename='%s/%s.prp'%(path,saverenderpassname)
		self.createFolders(path)
		f=open(filename,'w')
		try:
			if len(selectRPs)==1:
				x=selectRPs[0]
			if len(selectRPs)>1:
				for i in range((len(selectRPs)-1)):
					x=selectRPs[i]+';'+selectRPs[(i+1)]
					selectRPs[(i+1)]=x
			f.writelines(x)
		finally:
			f.close()
		cmds.button('presets_V2',e=True,l='Presets*')
	def createFolders(self,path=''):
		if not os.path.exists(path):
			os.makedirs(path)
	def getrenderPasspresets(self,path=''):
		renderpassespre=[]
		if os.path.exists(path):
			all_files=os.listdir(path)
			if len(all_files):
				[renderpassespre.append(each[:-4]) for each in all_files if each[-4:]=='.prp' and os.path.isfile('%s/%s'%(path,each))]
		return renderpassespre

	def deleteRenderpassPresets(self,*args):
		sel_prests=cmds.textScrollList('editrenderPasssPresets_ts_V2',q=True,si=True)
		if sel_prests!=None:
			[self.delRenderpassPresets_fdir(s,'D:/maya_renderPasses/Presets') for s in sel_prests]
			all_pres=self.getrenderPasspresets('D:/maya_renderPasses/Presets')
			cmds.textScrollList('editrenderPasssPresets_ts_V2',e=True,ra=True)
			if len(all_pres):
				cmds.textScrollList('editrenderPasssPresets_ts_V2',e=True,append=all_pres)
			else:
				cmds.button('presets_V2',e=True,l='Presets')
		else:
			cmds.warning('no selected in Edit RenderPass Presets!')
	def delRenderpassPresets_fdir(self,preset,path):
		os.remove('%s./%s.prp'%(path,preset))
#============================================================================================================修改部分====================================================================================================================================================
	def renderPassesOnOrOff(self,bool):
		allrenderPasses=cmds.ls(type='renderPass')
		if len(allrenderPasses):
			[cmds.setAttr("%s.renderable"%single, bool) for single in allrenderPasses]
		else:
			cmds.warning('No renderPasses in the scene!!')
	def deleteOutcolorBuffer(self,passAttr,shaderName):
		if cmds.objExists('%s.%s'%(shaderName,passAttr)):
			outR=cmds.connectionInfo('%s.%sR'%(shaderName,passAttr), isDestination=True)
			outG=cmds.connectionInfo('%s.%sG'%(shaderName,passAttr), isDestination=True)
			outB=cmds.connectionInfo('%s.%sB'%(shaderName,passAttr), isDestination=True)
			if outR==0 and outG==0 and outB==0:
				Out=cmds.getAttr('%s.%s'%(shaderName,passAttr))
				if Out==[(0, 0, 0)]:
					ColorBuffers=cmds.listConnections('%s.%s'%(shaderName,passAttr),s=False,type='writeToColorBuffer')
					if ColorBuffers!=None:
						cmds.delete(ColorBuffers)
					multiplyDivides=cmds.listConnections('%s.%s'%(shaderName,passAttr),s=False,type='multiplyDivide')
					if multiplyDivides!=None:
						cb=cmds.listConnections(multiplyDivides,s=False,type='writeToColorBuffer')
						if cb!=None:
							cmds.delete(cb)
						cmds.delete(multiplyDivides)

	def deleteUnusedrenderPasses(self,*args):
		allshaders=self.getAllMyShader()
		if len(allshaders):
			for single in allshaders:
				self.deleteOutcolorBuffer('color',single)
				self.deleteOutcolorBuffer('ambientColor',single)
				self.deleteOutcolorBuffer('sss',single)
				self.deleteOutcolorBuffer('incandescence',single)
				self.deleteOutcolorBuffer('addSpecular',single)
				self.deleteOutcolorBuffer('addReflection',single)
				self.deleteOutcolorBuffer('ambientOcclusion',single)
				self.deleteOutcolorBuffer('worldNormal',single)
				self.deleteOutcolorBuffer('zdepth',single)
				self.deleteOutcolorBuffer('facingRatio',single)
				self.deleteOutcolorBuffer('mv',single)
				self.deleteOutcolorBuffer('assetObjectID',single)
				self.deleteOutcolorBuffer('materialID',single)
				if cmds.objExists('%s.transparency'%single):
					reverses=cmds.listConnections('%s.transparency'%single,s=False,type='reverse')
					if reverses!=None:
						for each in reverses:
							if cmds.listConnections(each ,s=False)==None:
								cmds.delete(each)
		allrenderPasses=cmds.ls(type='renderPass')
		if len(allrenderPasses):
			fgsize=cmds.getAttr('miDefaultOptions.finalGather')
			for singlerp in allrenderPasses:
				if cmds.objExists('%s.renderpassType'%singlerp):
					if cmds.getAttr('%s.renderpassType'%singlerp)=='CSTCOL':
						if cmds.listConnections('%s.message'%singlerp,s=False,type='writeToColorBuffer')==None:
							cmds.delete(singlerp)
					elif cmds.getAttr('%s.renderpassType'%singlerp)=='INDIRR':
						if fgsize==0:
							cmds.delete(singlerp)
		renderLayers=self.getAllRenderLayers_exc()
		if len(renderLayers):
			for singleLayer in renderLayers:
				renderPasses=cmds.listConnections(singleLayer,s=False,type='renderPass')
				if renderPasses!=None:
					difflist=[]
					specslist=[]
					reflslist=[]
					refrslist=[]
					shaders=self.getShadersFromRenderlayer(singleLayer)
					if len(shaders):
						for singleshader in shaders:
							nodetype=cmds.nodeType(singleshader)
							if cmds.objExists('%s.diffuse'%singleshader):
								if cmds.getAttr('%s.diffuse'%singleshader)==0:
									difflist.append(singleshader)
							if cmds.objExists('%s.eccentricity'%singleshader):
								if cmds.getAttr('%s.eccentricity'%singleshader)==0:
									specslist.append(singleshader)
							if cmds.objExists('%s.specularRollOff'%singleshader):
								if cmds.getAttr('%s.specularRollOff'%singleshader)==0:
									specslist.append(singleshader)
									reflslist.append(singleshader)
							if cmds.objExists('%s.specularColor'%singleshader):
								outR=cmds.connectionInfo('%s.specularColorR'%singleshader, isDestination=True)
								outG=cmds.connectionInfo('%s.specularColorG'%singleshader, isDestination=True)
								outB=cmds.connectionInfo('%s.specularColorB'%singleshader, isDestination=True)
								if outR==0 and outG==0 and outB==0:
									Out=cmds.getAttr('%s.specularColor'%singleshader)
									if Out==[(0, 0, 0)]:
										specslist.append(singleshader)
										reflslist.append(singleshader)
							if cmds.objExists('%s.roughness'%singleshader):
								if cmds.getAttr('%s.roughness'%singleshader)==0:
									specslist.append(singleshader)
							if cmds.objExists('%s.highlightSize'%singleshader):
								if cmds.getAttr('%s.highlightSize'%singleshader)==0:
									specslist.append(singleshader)
							if cmds.objExists('%s.spreadX'%singleshader):
								if cmds.getAttr('%s.spreadX'%singleshader)==0:
									specslist.append(singleshader)
							if cmds.objExists('%s.spreadY'%singleshader):
								if cmds.getAttr('%s.spreadY'%singleshader)==0:
									specslist.append(singleshader)
							if cmds.objExists('%s.roughness'%singleshader):
								if cmds.getAttr('%s.roughness'%singleshader)==0:
									specslist.append(singleshader)
							if cmds.objExists('%s.fresnelRefractiveIndex'%singleshader):
								if cmds.getAttr('%s.fresnelRefractiveIndex'%singleshader)==1:
									specslist.append(singleshader)
							if cmds.objExists('%s.specularity'%singleshader):
								if cmds.getAttr('%s.specularity'%singleshader)==1:
									specslist.append(singleshader)

							if cmds.objExists('%s.reflectivity'%singleshader):
								if cmds.getAttr('%s.reflectivity'%singleshader)==0:
									reflslist.append(singleshader)
							if cmds.objExists('%s.anisotropicReflectivity'%singleshader):
								if cmds.getAttr('%s.anisotropicReflectivity'%singleshader)==1:
									reflslist.append(singleshader)

							if cmds.objExists('%s.refractions'%singleshader):
								if cmds.getAttr('%s.refractions'%singleshader)==0:
									refrslist.append(singleshader)
					if len(difflist):
						difflist=self.deleteDInList(difflist)
					if len(specslist):
						specslist=self.deleteDInList(specslist)
					if len(reflslist):
						reflslist=self.deleteDInList(reflslist)
					if len(refrslist):
						refrslist=self.deleteDInList(refrslist)
					self.deleteSomeRenderpass(difflist,shaders,renderPasses, singleLayer,'DIFF')
					self.deleteSomeRenderpass(specslist,shaders,renderPasses, singleLayer,'SPEC')
					self.deleteSomeRenderpass(reflslist,shaders,renderPasses, singleLayer,'REFL')
					self.deleteSomeRenderpass(refrslist,shaders,renderPasses, singleLayer,'REFR')
			newrenderpasses=cmds.ls(type='renderPass')
			for eachrenderLayer in renderLayers:
				self.deletedatarays(eachrenderLayer,newrenderpasses)
		self.saveOutputRenderpassControlDatas()
	def deleteSomeRenderpass(self,list,shaderlist,renderpasslist,renderLayer,type):
#		print list,shaderlist
		if len(list)==len(shaderlist):
			for singlePass in renderpasslist:
				if cmds.objExists('%s.renderpassType'%singlePass):
					if cmds.getAttr('%s.renderpassType'%singlePass)==type:
						cmds.delete(singlePass)
	def deletedatarays(self,renderLayer,renderPases):
		if 'Renderpasses' in self.zwfOutputRenderpassControlDatas[renderLayer]:
			if len (self.zwfOutputRenderpassControlDatas[renderLayer]['Renderpasses']):
				dir={}
				for single in self.zwfOutputRenderpassControlDatas[renderLayer]['Renderpasses']:
					if self.zwfOutputRenderpassControlDatas[renderLayer]['Renderpasses'][single]['Name']  in renderPases:
						dir[single]=self.zwfOutputRenderpassControlDatas[renderLayer]['Renderpasses'][single]
				self.zwfOutputRenderpassControlDatas[renderLayer]['Renderpasses']=dir
	def getobjsAssLambertOrNoshader(self,*args):
		objs=[]
		obj=cmds.listConnections('initialShadingGroup',d=False,sh=True)
		if obj!=None:
			objs=cmds.ls(obj,type=['mesh','subdiv','nurbsSurface'])
			if objs:
				objs=self.getNewObjshapesList(objs)
		allobjs=cmds.ls(type=['mesh','subdiv','nurbsSurface'])
		if allobjs:
			allobjs=self.getNewObjshapesList(allobjs)
		if len(allobjs):
			for single in allobjs:
				sg=cmds.listConnections(single,s=False,type='shadingEngine')
				if sg!=None:
					for each in sg:
						if cmds.connectionInfo('%s.surfaceShader'%each, isDestination=True)==0 and cmds.connectionInfo('%s.miMaterialShader'%each, isDestination=True)==0:
							objs.append(single)
				else:
					objs.append(single)
		cmds.select(cl=True)
		if len(objs):
			cmds.select(objs)

#=========================================================================================================picture output folder========================================================================================================================================
	def pic_outPut(self,*args):
		scenename=cmds.file(q=True,sn=True,shn=True)
		if '_' in scenename:
			split=scenename.split('_')
			if len(split)>2:
				pathp=split[0]+'/'+split[0]+'_'+split[1]
			else:
				pathp=scenename[:-3]
				cmds.warning('this maya file name is non-standard file name!')
		else:
			pathp=scenename[:-3]
			cmds.warning('this maya file name is non-standard file name!')
		renderpass=cmds.checkBox(self.Modify_picoutput_cb,q=True,v=True)
		outputkeys=cmds.textFieldButtonGrp(self.Modify_picoutput_outputkey,q=True,text=True)
		if len(outputkeys):
			if renderpass:
				Pathname=pathp+'/'+outputkeys+'/<RenderPass>/<RenderPass>'
			else:
				Pathname=pathp+'/'+outputkeys+'/'+outputkeys
			cmds.setAttr("defaultRenderGlobals.ifp",Pathname,type="string")
			cmds.text(self.Modify_picoutput_text_ts,e=True,l='renderOutput : .../'+Pathname)
		else:
			cmds.warning('No worlds in output key:')

#=========================================================================================================ID and transparent relationship========================================================================================================================================
	def IDAndTransparentBreakRelationship(self,*args):
		mi_blinns=cmds.ls(type='mi_blinn')
		if len(mi_blinns):
			for single in mi_blinns:
				if not cmds.connectionInfo('%s.transparency'%single,id=True):
					size=cmds.getAttr('%s.transparency'%single)
					if size!=[(0,0,0)]:
						self.breakfunction(single,'assetObjectID')
						self.breakfunction(single,'materialID')
	def breakfunction(self,shader='',td=''):
		assidDown=cmds.listConnections('%s.%s'%(shader,td),s=False)
		if assidDown!=None:
			for each in assidDown:
				if cmds.nodeType(each)=='multiplyDivide':
					assidDown=cmds.listConnections('%s.output'%each,s=False,type='writeToColorBuffer')
					if assidDown!=None:
						if not cmds.objExists('%s.LingshiTd'%assidDown[0]):
							cmds.addAttr(assidDown[0],ln="LingshiTd",at='double3')
							cmds.addAttr(assidDown[0],ln="LingshiTdX",at='double',p='LingshiTd')
							cmds.addAttr(assidDown[0],ln="LingshiTdY",at='double',p='LingshiTd')
							cmds.addAttr(assidDown[0],ln="LingshiTdZ",at='double',p='LingshiTd')
	#					if cmds.connectionInfo('%s.evaluationPassThrough'%assidDown[0],id=True):
	#						cmds.disconnectAttr('%s.outColor'%shader, '%s.evaluationPassThrough'%assidDown[0])
						try:
							cmds.connectAttr('%s.output'%each,'%s.LingshiTd'%assidDown[0],f=True)
							cmds.connectAttr('%s.%s'%(shader,td),'%s.color'%assidDown[0],f=True)
						except:
							pass
						renderpass=cmds.listConnections('%s.renderPass'%assidDown[0],d=False,type='renderPass')
				elif cmds.nodeType(each)=='writeToColorBuffer':
	#				if cmds.connectionInfo('%s.evaluationPassThrough'%each,id=True):
	#					cmds.disconnectAttr('%s.outColor'%shader, '%s.evaluationPassThrough'%each)
					renderpass=cmds.listConnections('%s.renderPass'%each,d=False,type='renderPass')
				if renderpass!=None:
					for ss in renderpass:
						cmds.setAttr("%s.useTransparency"%ss,0)
						cmds.setAttr("%s.transparentAttenuation"%ss,0)
	def IDAndTransparentConnectionRelationship(self,*args):
		colorBuffers=cmds.ls(type='writeToColorBuffer')
		if len(colorBuffers):
			for single in colorBuffers:
				if cmds.objExists('%s.LingshiTd'%single):
					dup=cmds.listConnections('%s.LingshiTd'%single,d=False)
					if dup!=None:
						cmds.connectAttr('%s.output'%dup[0],'%s.color'%single,f=True)
						cmds.disconnectAttr('%s.output'%dup[0], '%s.LingshiTd'%single)
		renderPasses=cmds.ls(type='renderPass')
		if len(renderPasses):
			for each in renderPasses:
				if cmds.objExists('%s.renderpassType'%each):
					if cmds.getAttr('%s.renderpassType'%each)=='CSTCOL':
						cmds.setAttr("%s.useTransparency"%each,1)
						cmds.setAttr("%s.transparentAttenuation"%each,1)
class createPpmenuItems:
	menuitem=''
	def __init__(self):
		cc=CreateOutputRenderPasses()
		self.zwfOutputRenderpassControlDatas=cc.zwfOutputRenderpassControlDatas
	def setmenuitem(self,menuitem):
		self.menuitem=menuitem
	def addmenuItems(self):
		cmds.menuItem('pre_popupI_%s_V2'%self.menuitem,l=self.menuitem,p='pre_popupI_V2',c=self.doaddmenuItems)
	def doaddmenuItems(self,*args):
		self.createPresetRenderPass(self.menuitem,'D:/maya_renderPasses/Presets')
		cmds.fileInfo('zwfOutputRenderpassFileInfoDatas',str(self.zwfOutputRenderpassControlDatas))
	def createPresetRenderPass(self,presetname,path):
		sel_renderlayer=cmds.textScrollList('ritsl_V2',q=True,si=True)
	#	pcm=cmds.textScrollList('pitsl_V2',q=True,si=True)
		if sel_renderlayer!=None:
#			all_passes=cmds.listConnections(sel_renderlayer,s=False,type='renderPass')
#			if all_passes!=None:
#				for each in all_passes:
#					self.fromRenderPassDeleteColorBuffer(each)
			filename='%s/%s.prp'%(path,presetname)
			ff=open(filename,'r')
			try:
				nr=ff.readlines(1)[0]
			finally:
				ff.close()
			nr=nr.split(';')
			cmds.textScrollList('rb_ritsl_V2',e=True,da=True)
			[cmds.textScrollList('rb_ritsl_V2',e=True,si=single) for single in nr]
			self.addRenderpass()
		else:
			cmds.warning('no selected in RenderLayer textScrollList.')
	def addRenderpass(self):
		sel_renderLayer=cmds.textScrollList('ritsl_V2',q=True,si=True)
		if sel_renderLayer==None:
			return cmds.warning('no selected in RenderLayer textScrollList.')
		sel_presets_pass=cmds.textScrollList('rb_ritsl_V2',q=True,si=True)
		if sel_presets_pass==None:
			cmds.warning ('no pass were selected in Presets.')
		else:
			cmds.textScrollList('rrbb_itsl_V2',e=True,ra=True)
			for single in sel_renderLayer:
				if single =="defaultRenderLayer":
					continue
#				if 'Renderpasses' not in self.zwfOutputRenderpassControlDatas[single]:
				self.zwfOutputRenderpassControlDatas[single]['Renderpasses']={}
				for each in sel_presets_pass:
					if each not in self.zwfOutputRenderpassControlDatas[single]['Renderpasses']:
						self.zwfOutputRenderpassControlDatas[single]['Renderpasses'][each]={}
						cc=CreateOutputRenderPasses()
						name=single+'_'+cc.renamePass(each)
						type=cc.getPassDataType(each)
						nametype=cc.getRenderpassType(each,name)
						self.zwfOutputRenderpassControlDatas[single]['Renderpasses'][each]['Name']=name
						self.zwfOutputRenderpassControlDatas[single]['Renderpasses'][each]['DataType']=type
						self.zwfOutputRenderpassControlDatas[single]['Renderpasses'][each]['NameDataType']=nametype
				renderpasseskeys=self.zwfOutputRenderpassControlDatas[single]['Renderpasses'].keys()
				[cmds.textScrollList('rrbb_itsl_V2',e=True,append=self.zwfOutputRenderpassControlDatas[single]['Renderpasses'][s]['NameDataType']) for s in renderpasseskeys]
			cmds.textScrollList('rb_ritsl_V2',e=True,da=True)
def call_OutputRenderPasses():
	a=CreateOutputRenderPasses()
	a.create_opt_ui()
if __name__=="__main__":
	call_OutputRenderPasses()