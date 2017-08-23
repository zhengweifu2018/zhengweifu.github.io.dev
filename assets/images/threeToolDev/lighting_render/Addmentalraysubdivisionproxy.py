# -*- Coding: Utf-8 -*- 
# coding=gbk

#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

#工具名字 ："Mentalray Subdivision Proxy Tool"
#书写时间 ：2012 . 8
#作      者 ：郑卫福
#版      本 ：V1.0
#电子邮件 ：651999307@qq.com
#maya版本 ：V2012-x64

#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

#使用方法：
#		1. 拷贝"Addmentalraysubdivisionproxy.py"到"...\Documents\maya\2012-x64\scripts"(或者python可以调用的路径下面)。
#		3. 打开maya2012。
#		4. 进入script Editor,python模块(编写 import Addmentalraysubdivisionproxy as addmsp ;addmsp.call_Addmsp())。

#/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////


import maya.cmds as cmds
import maya.mel as mel
class Addmentalraysubdivisionproxy:
	def Addmentalraysubdivisionproxy_UI(self):
		mr=cmds.pluginInfo("Mayatomr", q=True, l=True)
		if not mr:
			cmds.loadPlugin("Mayatomr")
			cmds.confirmDialog( title='load mr_V2', message='++++++"Mayatomr" was loaded,please Try again.++++++',b='colse')
			return 
		if cmds.window('mentalraysubdivisionproxy_win',ex=True):
			cmds.deleteUI('mentalraysubdivisionproxy_win')
		sp_window=cmds.window('mentalraysubdivisionproxy_win',t='Mentalray Subdivision Proxy Tool',wh=(325,300))
		men_sun_pro_mcol=cmds.columnLayout('msp_mcol',cat=["both",3],adj=True)
		men_sun_pro_refbutton=cmds.button('msp_refbutton',l='Refresh Subdivision Level ...',c=self.refreshSubdivisionLevels,bgc=[0.3,0.6,0.4])
		cmds.separator('msp_o', height=5, style='in' )
		men_sun_pro_sl=cmds.textScrollList('msp_sl',allowMultiSelection=True,append=self.textScroll_append(),sc=self.selectedObjects,h=200)
		cmds.separator('msp_t', height=10, style='in' )
		cmds.frameLayout('msp_addsunlevelframe',label='Add Subdivision Level (Attribute)',cll=True,borderStyle='etchedOut')
		cmds.columnLayout('msp_aslfcol',cat=["both",3],adj=True)
		men_sun_pro_addsublevelAttr=cmds.button('msp_addsublevelAttr',l='Add Subdivision Level Attribute (for all "polygon")',c=self.addsubdivisionLevel,bgc=[0.6,0.3,0.4],h=30)
		cmds.rowLayout('msp_setsublevel_r',nc=3, cw3=(90,80,50), adjustableColumn=2, columnAlign=(1, 'both'), columnAttach=[(1, 'both', 0), (2, 'both', 0), (3, 'both', 0)] )
		cmds.text('msp_setsubleveltext',l='Subdivision Levels')
		cmds.intField('msp_setsublevelintF', minValue=0, value=0,step=1)
		cmds.button('msp_setsublevelset',l='set...',c=self.setSubdivisionLevelForselect)
		cmds.setParent('msp_mcol')
		cmds.separator('msp_th', height=10, style='in' )
		cmds.frameLayout('msp_addsunporframe',label='Add Subdivision Proxy (Nodes)',cll=True,borderStyle='etchedOut')
		cmds.columnLayout('msp_aspfcol',cat=["both",3],adj=True)
#		men_sun_pro_addsubPro_s=cmds.button('msp_addsubPro_s',l='Add Subdivision Proxy (Select)',c=self.addSubdivisionProxyNodes_sel,bgc=[0.3,0.4,0.7],h=30)
#		cmds.separator('msp_f', height=10, style='in' )
		men_sun_pro_addsubPro_a=cmds.button('msp_addsubPro_a',l='Add Subdivision Proxy Nodes (All)',c=self.addSubdivisionProxyNodes_all,bgc=[0.3,0.4,0.7],h=30)
		cmds.setParent('msp_mcol')
		cmds.separator('msp_fo', height=10, style='in' )
		cmds.frameLayout('msp_help',label='Help',cll=True,cl=True,borderStyle='etchedOut',ec=lambda *args:self.resizewindow(475),cc=lambda *args:self.resizewindow(415))
		cmds.text('msp_help_t',l=u'"!" 该符号在列表中说明细分代理未完全添加，需要重新添加。',al='left',h=30)
		cmds.text('msp_help_tt',l=u'最大细分级别为四级。',al='left',h=30)
		cmds.window('mentalraysubdivisionproxy_win',e=True,wh=(325,415))
		cmds.showWindow('mentalraysubdivisionproxy_win')
	def deleteDInList(self,listName=[]):
		midList=[]
		for eachName in listName:
			if not eachName in midList:
				midList.append(eachName)
		return midList
	def getAllMeshs(self):
		meshsList=[]
		allmeshs=cmds.ls(type='mesh')
		if allmeshs:
			[meshsList.append(mesh) for mesh in allmeshs if not cmds.getAttr('%s.intermediateObject'%mesh)]
		return meshsList
	def getMeshUp(self,mesh):
		meshUp=cmds.listRelatives(mesh,p=True,pa=True)[0]
		return meshUp
	def getAllMeshUp(self):
		allMeshUps=[]
		allmeshs=self.getAllMeshs()
		if len(allmeshs):
			[allMeshUps.append(self.getMeshUp(single))for single in allmeshs]
		return allMeshUps
	def getSubdivisionLevel(self):
		SubdivisionLevels=[]
		allMeshUps=self.getAllMeshUp()
		if len(allMeshUps):
			for single in allMeshUps:
				if cmds.objExists('%s.subdivisionLevel'%single):
					SL_number=cmds.getAttr('%s.subdivisionLevel'%single)
					if SL_number not in SubdivisionLevels:
						SubdivisionLevels.append(SL_number)
		SubdivisionLevels.sort()
		return SubdivisionLevels
	def getconnection(self,level):
		i=0
		if level!=0:
			allmeshs=self.getAllMeshs()
			if len(allmeshs):
				all_ploygon_ts=cmds.listRelatives(allmeshs,p=True,pa=True,type='transform')
				for single in all_ploygon_ts:
					if cmds.objExists('%s.subdivisionLevel'%single):
						newlevel=cmds.getAttr('%s.subdivisionLevel'%single)
						if newlevel==level:
							nextshapes=cmds.listRelatives(single,c=True,type='mesh',pa=True)
							if nextshapes:
								for nextshape in nextshapes:
									if not cmds.getAttr('%s.intermediateObject'%nextshape):
										if self.checkProblem(nextshape):
											downSmooth=cmds.listConnections('%s.inMesh'%nextshape,d=False,type='polySmoothFace')
											if downSmooth==None:
												i+=1
												break
											else:
												dvlevels=cmds.getAttr('%s.divisions'%downSmooth[0])
												if dvlevels!=level:
													i+=1
													break
										else:
											if not cmds.objExists('%s.miSubdivApprox'%nextshape):
												i+=1
												break
											else:
												lisDown=cmds.listConnections('%s.miSubdivApprox'%nextshape,d=False,type='mentalraySubdivApprox')
												if lisDown==None:
													i+=1
													break
												else:
													nsub=cmds.getAttr("%s.nSubdivisions"%lisDown[0])
													if nsub!=level:
														i+=1
														break
		else:
			objsdir=self.getObjectsFormSubdivisionLevels([0])
			if objsdir!={}:
				for each in objsdir:
					objs=objsdir[each]
					for s in objs:
						sshape=cmds.listRelatives(s,c=True,type='mesh',pa=True)[0]
						if self.checkProblem(sshape):
							dsmooth=cmds.listConnections('%s.inMesh'%sshape,d=False,type='polySmoothFace')
							if dsmooth!=None:
								if cmds.getAttr('%s.divisions'%dsmooth[0])!=level:
									i+=1
									break
						else:
							if cmds.objExists('%s.miSubdivApprox'%sshape):
								down=cmds.listConnections('%s.miSubdivApprox'%sshape,d=False,type='mentalraySubdivApprox')
								if down!=None:
									i+=1
									break
		return i
	def fromIntToString(self):
		string_SubdivisionLevels=[]
		int_SubdivisionLevels=self.getSubdivisionLevel()
		if len(int_SubdivisionLevels):
			for each in int_SubdivisionLevels:
				ss='Subdivision Level : %d'%each
				i=self.getconnection(each)
				if i!=0:
					ss=' ! '+ss
				string_SubdivisionLevels.append(ss)
		return string_SubdivisionLevels
	def textScroll_append(self):
		appendlist=[]
		if not len(self.fromIntToString()):
			appendlist.append('No subdivision levels in the scene!')
		else:
			appendlist=self.fromIntToString()
		return appendlist
	def refreshSubdivisionLevels(self,*args):
		string_SubdivisionLevels=self.fromIntToString()
		cmds.textScrollList('msp_sl',e=True,ra=True)
		if len(string_SubdivisionLevels):
			cmds.textScrollList('msp_sl',e=True,append=string_SubdivisionLevels)
		else:
			cmds.textScrollList('msp_sl',e=True,append=["No subdivision levels in the scene!"])
	def getObjectsFormSubdivisionLevels(self,subLevels):
		subLevelsdir={}
		allMeshUps=self.getAllMeshUp()
		for single in subLevels:
			subLevelsdir['SubdivisionLevel>%d'%single]=[]
			if len(allMeshUps):
				for each in allMeshUps:
					if cmds.objExists('%s.subdivisionLevel'%each):
						number=cmds.getAttr('%s.subdivisionLevel'%each)
						if number==single:
							subLevelsdir['SubdivisionLevel>%d'%single].append(each)
		return subLevelsdir
	def selectInTextScrollList(self):
		sel_TextScro=cmds.textScrollList('msp_sl',q=True,si=True)
		return sel_TextScro
	def fromStringToInt(self):
		int_SubdivisionLevels=[]
		sel_TextScro=self.selectInTextScrollList()
		if sel_TextScro!=None:
			[int_SubdivisionLevels.append(int(single.split(' : ')[-1])) for single in sel_TextScro]
		return int_SubdivisionLevels
	def selectedObjects(self,*args):
		int_SubdivisionLevels=self.fromStringToInt()
		if not len(int_SubdivisionLevels):
			cmds.select(cl=True)
		else:
			subLevelsdir=self.getObjectsFormSubdivisionLevels(int_SubdivisionLevels)
			if subLevelsdir!={}:
				cmds.select(cl=True)
				for single in subLevelsdir:
					objects=subLevelsdir[single]
					if len(objects):
						cmds.select(objects,add=True)
	def addsubdivisionLevel(self,*args):
		all_mesh=cmds.ls(type='mesh')
		if len(all_mesh):
			all_mesh_p=cmds.listRelatives(all_mesh,p=True,pa=True)
			lname='subdivisionLevel'
			for each in all_mesh_p:
				if not cmds.objExists('%s.subdivisionLevel'%each):
					cmds.addAttr(each,ln=lname, keyable=True ,at='long', min=0, dv=0)
			print ' ^_^ All ploygons add subdivisionLevel successful.'
		else:
			cmds.warning('No Ploygons in the sence!')
	def checkProblem(sefl,obj):
		cmds.select(obj)
#		out=mel.eval('polyCleanupArgList 3 { "0","2","0","0","1","0","0","0","0","1e-005","0","1e-005","0","1e-005","0","1","0" }')
		out=cmds.polyInfo(obj,nmv=True)
		if out!=None:
			return True
		else:
			cmds.select(obj,r=True)
			mel.eval('polySelectConstraint -m 3 -t 8 -sz 3')
			out=cmds.ls(sl=True)
			cmds.select(cl=True)
			if len(out):
				return True
			else:
				down=cmds.listConnections('%s.inMesh'%obj,d=False,type='polySmoothFace')
				if down!=None:
					return True
				else:
					return False
	def addSubdivisionProxyNodes(self,subLevels):
		subLevelsdir=self.getObjectsFormSubdivisionLevels(subLevels)
		if subLevelsdir!={}:
			for single in subLevelsdir:
				singlevlues=subLevelsdir[single]
				if len(singlevlues):
					singlevlues=self.deleteDInList(singlevlues)
					singlevlueShapes=cmds.listRelatives(singlevlues,c=True,type='mesh',pa=True)
					if singlevlueShapes!=None:
						singlevlueShapes=self.deleteDInList(singlevlueShapes)
						nsub=int(single[17:])
						smooth=[]
						subdivApprox=[]
						for each in singlevlueShapes:
							if cmds.getAttr('%s.intermediateObject'%each):
								continue
							elif cmds.listConnections('%s.outMesh'%each,s=False,type='polySmoothFace')!=None:
								continue
							elif self.checkProblem(each):
								smooth.append(each)
							else:
								subdivApprox.append(each)
						if len(subdivApprox) and nsub!=0:
							self.ctreateSunProxyNodesAndConnetionsToPloygon(nsub,subdivApprox)
						if len(smooth):
							for singleP in smooth:
								self.ctreateSmoothNode(nsub,singleP)
	def ctreateSmoothNode(self,Nsmooth,objshape):
		smoothNode=cmds.listConnections('%s.inMesh'%objshape,d=False,type='polySmoothFace')
		if smoothNode!=None:
			cmds.setAttr('%s.divisions'%smoothNode[0],Nsmooth)
		else:
			if Nsmooth>0:
				print objshape
				mel.eval('polySmooth  -mth 0 -dv %d -bnr 1 -c 1 -kb 0 -ksb 1 -khe 0 -kt 1 -kmb 1 -suv 1 -peh 0 -sl 1 -dpe 1 -ps 0.1 -ro 1 -ch 1 %s'%(Nsmooth,objshape))
	def ctreateSunProxyNodesAndConnetionsToPloygon(self,Nsub,meshes):
		sub_proxy=cmds.createNode('mentalraySubdivApprox')
		cmds.setAttr("%s.nSubdivisions"%sub_proxy, Nsub)
		mentalrayItems=cmds.ls(type='mentalrayItemsList')
		if len(mentalrayItems):
			mrItemsListNode=mentalrayItems[0]
		else:
			mrItemsListNode=cmds.createNode('mentalrayItemsList',n='mentalrayItemsList')
		cmds.connectAttr("%s.message"%sub_proxy, "%s.subdivApproxs"%mrItemsListNode,na=True)
		for single in meshes:
			if not cmds.objExists("%s.miSubdivApprox"%single):
				cmds.addAttr(single,ln="miSubdivApprox",sn="miva",at='message')
			try:
				cmds.connectAttr('%s.message'%sub_proxy, '%s.miSubdivApprox'%single,f=True)
			except: pass
	def addSubdivisionProxyNodes_all(self,*args):
		allSubProxys=cmds.ls(type='mentalraySubdivApprox')
		if len(allSubProxys):
			try:
				cmds.delete(allSubProxys)
			except: pass
		subLevels=self.getSubdivisionLevel()
		if len(subLevels):
#			for single in subLevels:
#				if single==0:
#					subLevels.remove(single)
#			if len(subLevels):
			self.addSubdivisionProxyNodes(subLevels)
#			else:
#				cmds.warning('All ploygons are not subdivisionLevel or subdivisionLevels are 0!')
		else:
			cmds.warning('All ploygons are not subdivisionLevel!')
		self.refreshSubdivisionLevels()
	def addSubdivisionProxyNodes_sel(self,*args):
		subLevels=self.fromStringToInt()
		if len(subLevels):
			for single in subLevels:
				if single==0:
					subLevels.remove(single)
			if len(subLevels):
				self.addSubdivisionProxyNodes(subLevels)
			else:
				cmds.warning('Select ploygons subdivisionLevels are 0!')
		else:
			cmds.warning('No selected in textScrollList!')
	def setSubdivisionLevelForselect(self,*args):
		sublevel=cmds.intField('msp_setsublevelintF',q=True,v=True)
		if sublevel>4:
			cmds.confirmDialog( title=u'提示', message=u'==== 细分级别不能大于4，请重新设置。====',b='关闭')
		else:
			sel_transform=cmds.ls(sl=True,type='transform')
			if len(sel_transform):
				sel_mesh_shapes=cmds.listRelatives(sel_transform,ad=True,type='mesh',pa=True)
				if sel_mesh_shapes!=None:
					mu_transforms=cmds.listRelatives(sel_mesh_shapes,p=True,type='transform',pa=True)
					for single in mu_transforms:
						if not cmds.objExists('%s.subdivisionLevel'%single):
							cmds.addAttr(single,ln='subdivisionLevel', keyable=True ,at='long', min=0, dv=0) 
						cmds.setAttr('%s.subdivisionLevel'%single,sublevel)
					print '^_^ Selected ploygons set subdivisionLevel successful.'
				else:
					cmds.warning('No ploygons in your selected!')
			else:
				cmds.warning('No selected!')
			self.refreshSubdivisionLevels()
	def resizewindow(self,hsize):
		cmds.window('mentalraysubdivisionproxy_win',e=True,h=hsize)
def call_Addmsp():
	a=Addmentalraysubdivisionproxy()
	a.Addmentalraysubdivisionproxy_UI()
if __name__=='__main__':
	call_Addmsp()