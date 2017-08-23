# -*- Coding: Utf-8 -*- 
# coding=gbk

import maya.cmds as cmds
import os
import AotoSwitchFilesSizeFollowCam as ASFC
class TextureManageMaster:
	def __init__(self):
		self.printdir={'Non-standard path':[],'Path does not exist':[]}
	def TextureManage_UI(self):
		mr=cmds.pluginInfo("Mayatomr", q=True, l=True)
		if not mr:
			cmds.loadPlugin("Mayatomr")
			cmds.confirmDialog( title='load mr_V2', message='++++++"Mayatomr" was loaded,please Try again.++++++',b='colse')
			return 
		if cmds.window('TMM_win',ex=True):
			cmds.deleteUI('TMM_win')
		window=cmds.window('TMM_win',t='Texture Manage Master V1.0',wh=(420,500))
		tabs= cmds.tabLayout('main_tabs',innerMarginWidth=5, innerMarginHeight=5)
		Hand_mainscrollLayout=cmds.scrollLayout(cr=True)
		Hand_col=cmds.columnLayout('hand_c',adj=True,cat=['both',1],rs=5)
		Hand_refresh_col=cmds.columnLayout('hand_ref_c',adj=True,cat=['both',30],rs=10)
		Refresh_Files_butt=cmds.button('ref_f_s_b',l='Refresh Files For Select...',c=self.refreshButtonFun,h=30)
		cmds.text('sel_f_t',l='Select files you want to modify')
		cmds.setParent(Hand_col)
		Hand_scrollLayout=cmds.scrollLayout('Hand_scr',h=260)
		cmds.setParent(Hand_col)
		cmds.separator(style='in' )
		prj=cmds.workspace(q=True,rd=True)
		fileprj=cmds.workspace("sourceImages",q=True, rte=True)
		prjfile='%s%s/'%(prj,fileprj)
		self.Hand_tfb_TarDir=cmds.textFieldButtonGrp(label='   Target Directory:', text=prjfile, buttonLabel='Folder...',adj=2,cl3=['left','left','left'],cw3=[90,220,30] )
		cmds.textFieldButtonGrp(self.Hand_tfb_TarDir,e=True,bc=lambda *args:self.openDirectory_function(self.Hand_tfb_TarDir))
		Hand_set_b=cmds.button('Hand_set_b',l='Set Path...',c=self.setPath_function)
		cmds.separator(style='in' )
		Hand_frame_swf=cmds.frameLayout('Hand_frame_switchFiles',label='Switch Files ("high","mid","low","draft")',cll=True,borderStyle='etchedOut')
		Hand_frame_col_swf=cmds.columnLayout('Hand_frame_col_switchFiles',adj=True,cat=['both',3],rs=2)
		Hand_Radio=cmds.radioButtonGrp('Hand_radiob',labelArray4=['high', 'mid', 'low','draft'], numberOfRadioButtons=4,sl=2)
		cmds.button('Switch_Selected_b',l='Switch For Selected',c=lambda *args:self.switchFiles('select'))
		cmds.button('Switch_All_b',l='Switch For All',c=lambda *args:self.switchFiles('all'))
		#cmds.textScrollList('file_coupleBack',allowMultiSelection=True,h=150)
		cmds.setParent(Hand_col)
		cmds.separator(style='in' )
		Hand_frame_pr=cmds.frameLayout(label='Root Replace',cll=True,cl=True,borderStyle='etchedOut')
		Hand_frame_col=cmds.columnLayout(adj=True,cat=['both',3],rs=2)
		self.Hand_tfb_OldRoot=cmds.textFieldButtonGrp(label='        Old Root:', text='', buttonLabel='Folder...',adj=2,cl3=['left','left','left'],cw3=[70,220,30] )
		cmds.textFieldButtonGrp(self.Hand_tfb_OldRoot,e=True,bc=lambda *args:self.openDirectory_function(self.Hand_tfb_OldRoot))
		self.Hand_tfb_NewRoot=cmds.textFieldButtonGrp(label='        New Root:', text=prjfile, buttonLabel='Folder...',adj=2,cl3=['left','left','left'],cw3=[70,220,30] )
		cmds.textFieldButtonGrp(self.Hand_tfb_NewRoot,e=True,bc=lambda *args:self.openDirectory_function(self.Hand_tfb_NewRoot))
		Hand_replace_b=cmds.button('Hand_r_b',l='Replace...',c=self.replacePartPath)
		
		cmds.setParent(tabs)
		Aoto_mainscrollLayout=cmds.scrollLayout(cr=True)
		Aoto_col=cmds.columnLayout('aoto_c',adj=True,cat=['both',2],rs=5)
		self.Aoto_camera=cmds.optionMenu( label='Camera Name:')
		self.addmenuItems()
		Aoto_frame_fct=cmds.frameLayout(label='Form Camera To Obj Distance ',cll=True,borderStyle='etchedOut')
		Aoto_frame_fct_col=cmds.columnLayout(adj=True,cat=['both',3],rs=5)
		Aoto_row_n=cmds.rowLayout(nc=2, cw2=(150,80), adjustableColumn=2, columnAttach=[(1, 'right', 0), (2, 'right', 150)] )
		Aoto_near_text=cmds.text(l='Near (<=)')
		self.Aoto_near_float=cmds.floatField(value=50,min=0,pre=2)
		cmds.setParent(Aoto_frame_fct_col)
		Aoto_row_n=cmds.rowLayout(nc=2, cw2=(150,80), adjustableColumn=2, columnAttach=[(1, 'right', 0), (2, 'right', 150)] )
		Aoto_middle_text=cmds.text(l='Middle ( > Near && <=)')
		self.Aoto_middle_float=cmds.floatField(value=200,min=0,pre=2)
		cmds.setParent(Aoto_frame_fct_col)
		Aoto_Far=cmds.text(l='Far (>Middle)')
		cmds.setParent(Aoto_col)
		cmds.separator(style='in' )
		Aoto_frame_fs=cmds.frameLayout(label='Frame steps ',cll=True,borderStyle='etchedOut')
		Aoto_frame_fs_col=cmds.columnLayout(adj=True,cat=['both',3],rs=5)
		self.Aoto_near=cmds.intFieldGrp(l='Frame steps', value1=5,cl2=['right','left'],cw2=[150,70])
		cmds.setParent(Aoto_col)
		cmds.separator(style='in' )
		Aoto_setpath=cmds.button(l='Aoto Set texture Path',c=self.AotoSetTexturePath,h=30)
		cmds.separator(style='in' )
		Aoto_setsubdivisionLe=cmds.button(l='Aoto Set Subdivision Proxy',c=self.AotoSetSubdivisionProxy,h=30)
		cmds.separator(style='in' )
		Aoto_frame_coupBack=cmds.frameLayout(label='Couple Back ',borderStyle='etchedOut')
		self.Aoto_scroll_coupBack=cmds.scrollLayout(h=195)
		cmds.button(l='Select the problem of mapping files...',p=Aoto_col,h=30,c=self.selectProblemFiles)

		cmds.setParent(tabs)
		Help_mainscrollLayout=cmds.scrollLayout(cr=True)
		Help_col=cmds.columnLayout('help_c',adj=True,cat=['both',2],rs=5)
		help_text=u'''
工作描述：\n                                                          
    1.贴图管理插件，转换和管理场景中使用的文件贴图。\n\n
..................................................\n\n
使用方法：\n
    1. 刷新选择物体的贴图，在场景选择您需要查找贴图的物体，单击Refresh Files For Select按钮。在下面的（Select Files you want tomodify）列表中反馈出与选择物体有关的贴图有在的文件夹。\n
    2. 改变贴图途径，在（Select Files you want tomodify）列表中选择需要更改的贴图，在Target Directory中填入新的贴图路径（可以单击Folder按钮搜索，也可以用复制的方式），单击Set Path按钮执行。\n
    3. 切换贴图的大小，（1.选择物体切换,在场景选择需要切换的模型,选择相应的模式（“high”,“mid”，“low”），单击Switch For Selected 按钮执行；2.所有贴图切换，选择相应的模式（“high”,“mid”，“low”），单击Switch For All 按钮执行。）。\n
    4. 替换贴图途径，在（Select Files you want tomodify）列表中选择需要更改的贴图，在Old Rood 中填入原始的部分路径（可以单击Folder按钮搜索），在New Rood 中填入新的部分路径（可以单击Folder按钮搜索），单击Replace按钮执行。\n
    5. 自动切换贴图大小（根据距离），在（CameraName中选择摄像机，在Near（<=）和 Middle（>Near &&<=）中填入物体离摄像机的距离），单击Aoto Set texture Path按钮切换。\n
    6. 自动更改细分代理的级别（根据距离），在（CameraName中选择摄像机，在Near（<=）和 Middle（>Near &&<=）中填入物体离摄像机的距离），单击Aoto Set Subdivision Proxy按钮更改。\n
\n\n
'''
		Help_scroll_descr=cmds.scrollField(ww=True,tx=help_text,editable=False,h=395)
		cmds.setParent(Help_col)
		Help_frame_about=cmds.frameLayout(label=u'关于“Texture Manage Master” ',borderStyle='in')
		cmds.text(l=u'   工具名字 :                              Texture Manage Master',align='left')
		cmds.text(l=u'   更新时间 :                              2012 年 9 月',align='left')
		cmds.text(l=u'   作者 :                                     郑卫福',align='left')
		cmds.text(l=u'   版本 :                                     v1.0',align='left')
		cmds.text(l=u'   电子邮箱 :                              651999307@qq.com',align='left')
		cmds.text(l=u'   maya版本 :                             maya2011以上',align='left')
		cmds.setParent(tabs)
		cmds.tabLayout('main_tabs',e=True,tl=((Hand_mainscrollLayout,'HandPart'),(Aoto_mainscrollLayout,'AotoPart'),(Help_mainscrollLayout,'Help')))
		cmds.window('TMM_win',e=True,wh=(420,562))
		cmds.showWindow('TMM_win')
	def addmenuItems(self):
		cameraShapes=cmds.ls(ca=True)
		oldcameras=['perspShape','frontShape','sideShape','topShape']
		#[cameraShapes.remove(single) for single in oldcameras]
		#[cameraShapes.append(each) for each in oldcameras]
		for singleca in cameraShapes:
			cmds.menuItem(l=singleca)
	def deleteDInList(self,listName=[]):
		midList=[]
		for eachName in listName:
			if not eachName in midList:
				midList.append(eachName)
		return midList
	def selectOBJs(self):
		sels=cmds.ls(sl=True)
		return sels
	def getShapesFromSelect(self):
		allshapes=[]
		sels=self.selectOBJs()
		if len(sels):
			shapes=cmds.listRelatives(sels,ad=True,pa=True,type=['mesh','subdiv','nurbsSurface'])
			if shapes!=None:
				[allshapes.append(single) for single in shapes]
		return allshapes
	def getFilesFormSelected(self):
		fileTextureList=[]
		objshapes=self.getShapesFromSelect()
		if len(objshapes):
			fileTextureList=self.getFilesFormObjs(objshapes)
		return fileTextureList
	def getFilesFormObjs(self,objshapes):
		fileTextureList=[]
		shaderSGs=cmds.listConnections(objshapes,s=False,type='shadingEngine')
		if shaderSGs!=None:
			shaderSGs=self.deleteDInList(shaderSGs)
			alldowns=cmds.listConnections(shaderSGs,d=False)
			shaders=cmds.ls(alldowns,mat=True)
			if shaders:
				shaders=self.deleteDInList(shaders)
				allhistory=cmds.listHistory(shaders)
				fileTextureList=cmds.ls(allhistory,type=['file','psdFileTex','mentalrayTexture'])
		if len(fileTextureList):
			fileTextureList=self.deleteDInList(fileTextureList)
		return fileTextureList
	def createTextScrollList(self,objlist,tishi):
		cmds.text(self.imfor_text,e=True,bgc=[1,0,0],l=' ! Error Files Path:')
		if not cmds.rowLayout('file_coupleBack_%s'%tishi,ex=True):
			cmds.rowLayout('file_coupleBack_%s'%tishi,numberOfColumns=2, columnWidth2=(30,300), adjustableColumn=2, columnAlign=(1, 'right'),columnAttach=[(1, 'both', 0), (2, 'both', 0)],p='lingshi_col')
		Nsp_img=cmds.iconTextButton(style='iconOnly', image='open_biaoqian.png',h=20)
		Nsp_cb=cmds.iconTextButton(style='iconAndTextHorizontal',h=20,label='%s :'%tishi,fn="boldLabelFont")
		cmds.setParent('lingshi_col')
		self.ccc_col=cmds.columnLayout(adj=True,cat=['left',55])
#		itcbname_img=[]
		subFileTextScor=cmds.textScrollList(ams=True,h=18)
		ll=len(objlist)
		cmds.textScrollList(subFileTextScor,e=True,append=objlist,h=13*ll+25)
#		for single in objlist:
#			File=cmds.iconTextCheckBox(style='iconAndTextHorizontal',i='lianjie_biaoqian.png',w=400,h=20, l=single,bgc=[0.265,0.265,0.265])
		bb=TextCheckBox_class()
		bb.setlabe(subFileTextScor)
		cmds.textScrollList(subFileTextScor,e=1,sc=bb.sub_checkon_c)
#			itcbname_img.append(File)
#		print itcbname_img
#		for each in itcbname_img:
		aa=BiaozhiConvisions()
		aa.setname(Nsp_img,subFileTextScor)
		cmds.iconTextButton(Nsp_img,e=1,c=aa.biaozhi_c)
		cc=SelSub_TextCheckBox_class()
		cc.setFilesList(subFileTextScor,objlist)
		cmds.iconTextButton(Nsp_cb,e=1,dcc=cc.SelSub_chechon_c)
	def switchFiles(self,key=''):
		if cmds.columnLayout('lingshi_col',ex=True):
			cmds.deleteUI('lingshi_col')
		cmds.columnLayout('lingshi_col',adj=True,cat=['both',1],p='Hand_scr')
		self.imfor_text=cmds.text(l='',p='lingshi_col',align='left')
		if key=='select':
			selfiles=self.getFilesFormSelected()
		if key=='all':
			selfiles=cmds.ls(type=['file','psdFileTex','mentalrayTexture'])
		if len(selfiles):
			filepartdir={}
			selRadiob=cmds.radioButtonGrp('Hand_radiob',q=True,sl=True)
			for single in selfiles:
				filepath=cmds.getAttr('%s.fileTextureName'%single)
				if filepath==None:
					if 'Path does not exist' not in filepartdir.keys():
						filepartdir['Path does not exist']=[]
					filepartdir['Path does not exist'].append(single)
				else:
					if os.path.isfile(filepath):
						dirName=os.path.dirname(filepath)
						baseName=os.path.basename(filepath)
						dirkey=dirName.split('/')[-1]
						fkl=baseName.split('.')
						filekey=fkl[0].split('_')[-1]
						splitfile=os.path.splitext(filepath)
						if filekey and dirkey in ['high', 'mid', 'low','draft']:
							if selRadiob==1:
								selRadiobs='high'
							elif selRadiob==2:
								selRadiobs='mid'
								#newpath=dirName[:-len(dirkey)]+'mid/'+fkl[0][:-len(dirkey)]+'mid.'+fkl[-1]
							elif selRadiob==3:
								selRadiobs='low'
								#newpath=dirName[:-len(dirkey)]+'low/'+fkl[0][:-len(dirkey)]+'low.'+fkl[-1]
							elif selRadiob==4:
								selRadiobs='draft'
							newpath=splitfile[0][:-len(filekey)]+selRadiobs+splitfile[-1]
							if os.path.isfile(newpath):
								cmds.setAttr('%s.fileTextureName'%single,newpath,type='string')
							else:
								ts=' No "%s" '%selRadiobs
								if ts not in filepartdir.keys():
									filepartdir[ts]=[]
								filepartdir[ts].append(single)
						else:
							if 'Non-standard path' not in filepartdir.keys():
								filepartdir['Non-standard path']=[]
							filepartdir['Non-standard path'].append(single)
					else:
						if 'Path does not exist' not in filepartdir.keys():
							filepartdir['Path does not exist']=[]
						filepartdir['Path does not exist'].append(single)
			if len(filepartdir):
				dirkeys=filepartdir.keys()
				dirkeys.sort()
				[self.createTextScrollList(filepartdir[each],each) for each in dirkeys if len(filepartdir[each])]
		else:
			if key=='select':
				textn="No selected (type:['mesh','subdiv','nurbsSurface']) or No textures in your select!"
			if key=='all':
				textn="No textures in your scene!"
			cmds.text(self.imfor_text,e=True,l=textn)
	def selectfiles(self,*args):
		sel_tses=cmds.textScrollList('file_coupleBack',q=True,si=True)
		allfiles=cmds.ls(type=['file','psdFileTex','mentalrayTexture'])
		cmds.select(allfiles,d=True)
		if sel_tses!=None:
			for single in sel_tses:
				single=single.split(' : ')[1]
				cmds.select(single,add=True)

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++更换texture文件路径++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
	def createdisplayListcomm(self,path,allfileNum,existsfileNum,notexistsfileNum):
		rowLN=path.replace('/','ZWF').replace(':','ZWF')
		if not cmds.rowLayout('file_coupleBack_%s'%rowLN,ex=True):
			cmds.rowLayout('file_coupleBack_%s'%rowLN,numberOfColumns=2, columnWidth2=(30,300), adjustableColumn=2, columnAlign=(1, 'right'),columnAttach=[(1, 'both', 0), (2, 'both', 0)],p='lingshi_col')
		Nsp_img=cmds.iconTextButton(style='iconOnly', image='open_biaoqian.png',h=20,bgc=[0.265,0.265,0.265])
		Nsp_label='%d texture(s) point to "%s"'%(allfileNum,path)
		Nsp_w=len(Nsp_label)*6
		Nsp_cb=cmds.iconTextButton(style='iconAndTextHorizontal',h=20,label=Nsp_label,bgc=[0.265,0.265,0.265],fn="boldLabelFont")
		if Nsp_w>100:
			cmds.iconTextButton(Nsp_cb,e=True,w=Nsp_w)
		cmds.setParent('lingshi_col')
		self.ccc_col=cmds.columnLayout(adj=True,cat=['left',35])
		exists_ITB=cmds.iconTextButton(style='iconAndTextHorizontal',h=20,image='lianjie_biaoqian.png',label='%d of them exist(s)'%existsfileNum,bgc=[0.265,0.265,0.265])
		notexists_ITB=cmds.iconTextButton(style='iconAndTextHorizontal',h=20,image='lianjie_biaoqian.png',label='%d of them not exist(s)'%notexistsfileNum,bgc=[0.265,0.265,0.265])
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
		aa=TMMBiaozhiConvisions()
		aa.setname(Nsp_img,exists_ITB,notexists_ITB)
		cmds.iconTextButton(Nsp_img,e=True,c=aa.biaozhi_c)
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
		bb=Sub_iconTextButton_class()
		bb.setName(exists_ITB,self.zhengweifufilesdirCTL[path]['Exists'])
		cmds.iconTextButton(exists_ITB,e=True,c=bb.function)
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
		cc=Sub_iconTextButton_class()
		cc.setName(notexists_ITB,self.zhengweifufilesdirCTL[path]['Notexists'])
		cmds.iconTextButton(notexists_ITB,e=True,c=cc.function)
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
		allfiles=self.zhengweifufilesdirCTL[path]['Exists']+self.zhengweifufilesdirCTL[path]['Notexists']
		dd=Parent_iconTextButton_class()
		dd.setNames(exists_ITB,notexists_ITB,allfiles)
		cmds.iconTextButton(Nsp_cb,e=True,dcc=dd.dccfunction)

	def createdisplayListspar(self,errorfileNum):
		Error_itb=cmds.iconTextButton(style='iconAndTextHorizontal',w=370,h=20,image='cuowu_biaoqian.png',label='  %d texture(s) not specified,so they are not exist(s)'%errorfileNum,bgc=[0.265,0.265,0.265],p='lingshi_col')
		ee=Sub_iconTextButton_class()
		ee.setName(Error_itb,self.zhengweifufilesdirCTL['Errorfiles'])
		cmds.iconTextButton(Error_itb,e=True,c=ee.function)

	def refreshButtonFun(self,*args):
		if cmds.columnLayout('lingshi_col',ex=True):
			cmds.deleteUI('lingshi_col')
		cmds.columnLayout('lingshi_col',adj=True,cat=['both',1],p='Hand_scr')
		cmds.text(l='',p='lingshi_col')
		imfor_text=cmds.text(l='',p='lingshi_col',align='left')
#		separator_d=cmds.separator( height=5, style='in',vis=False)
		files=self.getFilesFormSelected()
		if len(files):
			cmds.text(imfor_text,e=True,l='    %d texture(s) after shaders of selected objects.'%len(files))
			cmds.separator( height=30, style='in')
			self.zhengweifufilesdirCTL={}
			for single in files:
				filePath=cmds.getAttr('%s.fileTextureName'%single)
				if filePath==None:
					if 'Errorfiles' not in self.zhengweifufilesdirCTL:
						self.zhengweifufilesdirCTL['Errorfiles']=[]
					self.zhengweifufilesdirCTL['Errorfiles'].append(single)
				else:
					if '/' in filePath:
						filedirName=os.path.dirname(filePath)
						if filedirName not in self.zhengweifufilesdirCTL:
							self.zhengweifufilesdirCTL[filedirName]={}
						if 'Exists' not in self.zhengweifufilesdirCTL[filedirName]:
							self.zhengweifufilesdirCTL[filedirName]['Exists']=[]
						if 'Notexists' not in self.zhengweifufilesdirCTL[filedirName]:
							self.zhengweifufilesdirCTL[filedirName]['Notexists']=[]
						if os.path.isfile(filePath):
							self.zhengweifufilesdirCTL[filedirName]['Exists'].append(single)
						else:
							self.zhengweifufilesdirCTL[filedirName]['Notexists'].append(single)
					else:
						if 'Errorfiles' not in self.zhengweifufilesdirCTL:
							self.zhengweifufilesdirCTL['Errorfiles']=[]
						self.zhengweifufilesdirCTL['Errorfiles'].append(single)
			if len(self.zhengweifufilesdirCTL):
				zwfkeys=self.zhengweifufilesdirCTL.keys()
				if 'Errorfiles' in zwfkeys:
					zwfkeys.remove('Errorfiles')
					zwfkeys.insert(0,'Errorfiles')
				for each in zwfkeys:
					if each=='Errorfiles':
						ErrorfilesNumbers=len(self.zhengweifufilesdirCTL['Errorfiles'])
						self.createdisplayListspar(ErrorfilesNumbers)
					else:
						fileExistsNumbers=len(self.zhengweifufilesdirCTL[each]['Exists'])
						fileNotexistsNumbers=len(self.zhengweifufilesdirCTL[each]['Notexists'])
						allfilesNumbers=fileExistsNumbers+fileNotexistsNumbers
						self.createdisplayListcomm(each,allfilesNumbers,fileExistsNumbers,fileNotexistsNumbers)
		else:
			cmds.text(imfor_text,e=True,l='    No objects were selected or No files after selected objects!!')
	def setPath_function(self,*args):
		selfiles=cmds.ls(sl=True,type=['file','psdFileTex','mentalrayTexture'])
		if len(selfiles):
			txname=cmds.textFieldButtonGrp(self.Hand_tfb_TarDir,q=True,tx=True)
			if len(txname):
				txname=txname.replace('\\','/')
				for single in selfiles:
					filePath=cmds.getAttr('%s.fileTextureName'%single)
					baseName=os.path.basename(filePath)
					#print single,txname,baseName
					cmds.setAttr('%s.fileTextureName'%single,'%s%s'%(txname,baseName),type='string')
			else:
				cmds.warning('No world in "Target Directory:" textFieldButtonGrp!!')
		else:
			cmds.warning('No files were selected in scrollList!!')

	def openDirectory_function(self,textName):
		filename = cmds.fileDialog2(fileMode=3, caption="Open Directory")
		if filename!=None:
			cmds.textFieldButtonGrp(textName,e=True,tx=filename[0])

	def replacePartPath(self,*args):
		selfiles=cmds.ls(sl=True,type=['file','psdFileTex','mentalrayTexture'])
		if len(selfiles):
			oldpath=cmds.textFieldButtonGrp(self.Hand_tfb_OldRoot,q=True,tx=True)
			if len(oldpath):
				newpath=cmds.textFieldButtonGrp(self.Hand_tfb_NewRoot,q=True,tx=True)
				if len(newpath):
					oldpath=oldpath.replace('\\','/')
					newpath=newpath.replace('\\','/')
					for single in selfiles:
						filepath=cmds.getAttr('%s.fileTextureName'%single)
						path=filepath.replace(oldpath,newpath)
						cmds.setAttr('%s.fileTextureName'%single,path,type='string')
				else:
					cmds.warning('No world in "New Root:" textFieldButtonGrp!!')
			else:
				cmds.warning('No world in "Old Root:" textFieldButtonGrp!!')
		else:
			cmds.warning('No files were selected in scrollList!!')

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++自动更改贴图品质++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
	def removeItem(self,oldlist,reItem):
		midlist=[]
		for i in oldlist:
			if i!=reItem:
				midlist.append(i)
		return midlist 
	def getDistancefilesdir(self):
		framesteps=cmds.intFieldGrp(self.Aoto_near,q=True,v1=True)
		cameraShape=cmds.optionMenu(self.Aoto_camera,q=True,v=True)
		minNum=cmds.floatField(self.Aoto_near_float,q=True,v=True)
		maxNum=cmds.floatField(self.Aoto_middle_float,q=True,v=True)
		bb=ASFC.AotoSwitchFilesSizeFollowCam()
		filedir=bb.getMinDistanceDirFromObjToCam(framesteps,cameraShape)
		distancefilesdir={'Near':[],'mid':[],'far':[]}
		if len(filedir):
			for single in filedir:
				distance=filedir[single]
				if distance<=minNum:
					distancefilesdir['Near'].append(single)
				elif distance>minNum and distance<=maxNum:
					distancefilesdir['mid'].append(single)
				elif distance>maxNum:
					distancefilesdir['far'].append(single)
		return distancefilesdir
	def AotoSetTexturePath(self,*args):
		if cmds.columnLayout('fankui_col',ex=True):
			cmds.deleteUI('fankui_col')
		cmds.columnLayout('fankui_col',adj=True,cat=['both',1],p=self.Aoto_scroll_coupBack)
		distancefilesdir=self.getDistancefilesdir()
		if len(distancefilesdir['Near']):
			NearFiles=self.getFilesFormObjs(distancefilesdir['Near'])
		else:
			NearFiles=[]
		if len(distancefilesdir['mid']):
			midFiles=self.getFilesFormObjs(distancefilesdir['mid'])
		else:
			midFiles=[]
		if len(distancefilesdir['far']):
			farFiles=self.getFilesFormObjs(distancefilesdir['far'])
		else:
			farFiles=[]
		if len(farFiles):
			for eachfarfile in farFiles:
				if eachfarfile in NearFiles or midFiles:
					NearFiles=self.removeItem(NearFiles,eachfarfile)
		if len(midFiles):
			for eachmidfile in midFiles:
				if eachmidfile in NearFiles:
					midFiles=self.removeItem(midFiles,eachmidfile)
		if len(NearFiles):
			self.aotogaibianTT(NearFiles,'high')
		if len(midFiles):
			self.aotogaibianTT(midFiles,'mid')
		if len(farFiles):
			self.aotogaibianTT(farFiles,'low')
		if len(self.printdir['Non-standard path']):
			cmds.text(l='   Non-standard path:',al='left',p='fankui_col',bgc=[1,0,0])
			for sN in self.printdir['Non-standard path']:
				cmds.text(l='                                   %s'%sN,al='left',p='fankui_col')
		if len(self.printdir['Path does not exist']):
			cmds.text(l='   Path does not exist:',al='left',p='fankui_col',bgc=[1,0,0])
			for sP in self.printdir['Path does not exist']:
				cmds.text(l='                                   %s'%sP,al='left',p='fankui_col')
	def AotoSetSubdivisionProxy(self,*args):
		self.setsubpp('mid',1)
		self.setsubpp('far',2)
	def setsubpp(self,dirkey,size):
		distancefilesdir=self.getDistancefilesdir()
		midfiles=distancefilesdir[dirkey]
		if len(midfiles):
			for midfile in midfiles:
				midfileshape=cmds.listRelatives(midfile,ap=True,type='transform',pa=True)[0]
				if cmds.objExists('%s.subdivisionLevel'%midfileshape):
					oldvalue=cmds.getAttr('%s.subdivisionLevel'%midfileshape)
					if oldvalue:
						newvalue=oldvalue-size
						if newvalue<0:
							newvalue=0
						cmds.setAttr('%s.subdivisionLevel'%midfileshape,newvalue)
	def aotogaibianTT(self,files,key):
		for N_eachnearfile in files:
			N_path=cmds.getAttr('%s.fileTextureName'%N_eachnearfile)
			if os.path.isfile(N_path) :
				N_dirName=os.path.dirname(N_path)
				Ndir_key=N_dirName.split('/')[-1]
				N_baseName=os.path.basename(N_path)
				N_baseName_split=N_baseName.split('.')
				Nbase_key=N_baseName_split[0].split('_')[-1]
				splitfile=os.path.splitext(N_path)
				if Nbase_key and Ndir_key in ['high', 'mid', 'low']:
					newpath=splitfile[0][:-len(Nbase_key)]+key+splitfile[-1]
					if os.path.isfile(newpath):
						cmds.setAttr('%s.fileTextureName'%N_eachnearfile,newpath,type='string')
					else:
						self.printdir['Path does not exist'].append(N_eachnearfile)
				else:
					self.printdir['Non-standard path'].append(N_eachnearfile)
			else:
				self.printdir['Non-standard path'].append(N_eachnearfile)
	def selectProblemFiles(self,*args):
		selfiles=self.printdir['Non-standard path']+self.printdir['Path does not exist']
		if len(selfiles):
			cmds.select(selfiles)
		else:
			print 'No problem map files in this scene!'
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++更换texture文件路径class++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
class TMMBiaozhiConvisions:
	nsp_img=''
	ItcbName_imgone=''
	ItcbName_imgtwo=''
	def setname(self,nsp_img,ItcbName_imgone,ItcbName_imgtwo):
		self.nsp_img=nsp_img
		self.ItcbName_imgone=ItcbName_imgone
		self.ItcbName_imgtwo=ItcbName_imgtwo

	def biaozhi_c(self,*args):
		ttttt=cmds.iconTextButton(self.nsp_img,q=1,image=1)
		if ttttt=='open_biaoqian.png':
			cmds.iconTextButton(self.nsp_img,e=1,image='close_biaoqian.png')
			cmds.iconTextButton(self.ItcbName_imgone,e=1,vis=0)
			cmds.iconTextButton(self.ItcbName_imgtwo,e=1,vis=0)
		if ttttt=='close_biaoqian.png':
			cmds.iconTextButton(self.nsp_img,e=1,image='open_biaoqian.png') 
			cmds.iconTextButton(self.ItcbName_imgone,e=1,vis=1)
			cmds.iconTextButton(self.ItcbName_imgtwo,e=1,vis=1)

class Sub_iconTextButton_class:
	itbName=''
	files=[]
	def setName(self,itbName,files):
		self.itbName=itbName
		self.files=files
	def function(self,*args):
		bgColor=cmds.iconTextButton(self.itbName,q=True,bgc=True)
		if bgColor==[0.26500343327992676, 0.26500343327992676, 0.26500343327992676]:
			if len(self.files):
				cmds.select(self.files,add=True)
			cmds.iconTextButton(self.itbName,e=True,bgc=[0.5,0.7,1])
		elif bgColor==[0.50000762951094835, 0.7000076295109483, 1.0]:
			if len(self.files):
				cmds.select(self.files,d=True)
			cmds.iconTextButton(self.itbName,e=True,bgc=[0.265,0.265,0.265])

class Parent_iconTextButton_class:
	itbNameone=''
	itbNametwo=''
	files=[]
	def setNames(self,itbNameone,itbNametwo,files):
		self.itbNameone=itbNameone
		self.itbNametwo=itbNametwo
		self.files=files
	def dccfunction(self,*args):
		if len(self.files):
			cmds.select(self.files,add=True)
		cmds.iconTextButton(self.itbNameone,e=True,bgc=[0.5,0.7,1])
		cmds.iconTextButton(self.itbNametwo,e=True,bgc=[0.5,0.7,1])

class BiaozhiConvisions:
	nsp_img=''
	ItcbName_img=''
	def setname(self,nsp_img,ItcbName_img):
		self.nsp_img=nsp_img
		self.ItcbName_img=ItcbName_img

	def biaozhi_c(self,*args):
		ttttt=cmds.iconTextButton(self.nsp_img,q=1,image=1)
		if ttttt=='open_biaoqian.png':
			cmds.iconTextButton(self.nsp_img,e=1,image='close_biaoqian.png')
			cmds.textScrollList(self.ItcbName_img,e=1,vis=0)
#			[cmds.iconTextCheckBox(single,e=1,vis=0) for single in self.ItcbName_img]
		if ttttt=='close_biaoqian.png':
			cmds.iconTextButton(self.nsp_img,e=1,image='open_biaoqian.png') 
			cmds.textScrollList(self.ItcbName_img,e=1,vis=1)
#			[cmds.iconTextCheckBox(each,e=1,vis=1) for each in self.ItcbName_img]
class TextCheckBox_class:
	labe_name=''
	def setlabe(self,labe_name):
		self.labe_name=labe_name
	def getlabe_name(self):
		labe=cmds.textScrollList(self.labe_name,q=1,si=1)
		return labe
	def sub_checkon_c(self,*args):
		sel=self.getlabe_name()
		alabe=cmds.textScrollList(self.labe_name,q=1,ai=1)
		cmds.select(alabe,d=1)
		if sel!=None:
			cmds.select(sel,add=1)
#		cmds.iconTextCheckBox(self.labe_name,e=1,bgc=[0.5,0.7,1])
#	def sub_checkoff_c(self,*args):
#		sel=self.getlabe_name()
#		cmds.select(sel,d=1)
#		cmds.iconTextCheckBox(self.labe_name,e=1,bgc=[0.265,0.265,0.265])
class SelSub_TextCheckBox_class:
	textcheckName=''
	fileslist=[]
	def setFilesList(self,textcheckName,fileslist):
		self.textcheckName=textcheckName
		self.fileslist=fileslist
	def SelSub_chechon_c(self,*args):
		cmds.select(self.fileslist,add=1)
		[cmds.textScrollList(self.textcheckName,e=1,si=single) for single in self.fileslist]
#		cmds.iconTextCheckBox(self.textcheckName,e=1,bgc=[0.5,0.7,1])

def call_TMM():
	tmm=TextureManageMaster()
	tmm.TextureManage_UI()
if __name__=='__main__':
	call_TMM()