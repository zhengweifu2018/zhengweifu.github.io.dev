# -*- coding: utf-8 -*-
import maya.cmds as cmds
import maya.mel as mel
ZWFGlobalbuttonResultCJ={}
ZWFGlobalbuttonMiddCJ={}
ZWFGlobalbuttonResultJS={}
ZWFGlobalbuttonMiddJS={}
class CheckRenderSeting(object):
	'UI class'
	uiName=''
	def __init__(self):
		fileInfoDateCJ=cmds.fileInfo('zwfRenderSetingButtonColorDatasCJ',q=True)
		fileInfoDateJS=cmds.fileInfo('zwfRenderSetingButtonColorDatasJS',q=True)
		if len(fileInfoDateCJ):
			self.zwfRenderSetingButtonColorDatasCJ=eval(fileInfoDateCJ[0])
		else:
			self.zwfRenderSetingButtonColorDatasCJ=[]
		if len(fileInfoDateJS):
			self.zwfRenderSetingButtonColorDatasJS=eval(fileInfoDateJS[0])
		else:
			self.zwfRenderSetingButtonColorDatasJS=[]
	def setUiName(self,uiName):
		'Set a name of window'
		self.uiName=uiName
	def creatUi(self):
		'UI core functions'
		if cmds.window(self.uiName,ex=1):
			cmds.deleteUI(self.uiName)
		cmds.window(self.uiName,t=u'提交渲染前检查工具',wh=(550,400))
		self.maiform=cmds.formLayout(numberOfDivisions=100)

		Help_b=cmds.button(l=u'帮助',h=30)
		close_b=cmds.button(l=u'关闭',h=30,c=self.closeWindow)
		paneL=cmds.paneLayout( configuration='vertical2' ,ps=[1,60,40])

		self.tabs = cmds.tabLayout(innerMarginWidth=5, innerMarginHeight=5)

		self.button_listScr_CJ=cmds.scrollLayout(vst=1,hst=0,cr=1)
		frameCJ=cmds.frameLayout(label=u'场景提交渲染前执行按钮', borderStyle='etchedIn')
		bb=CreateButton()
		bb.create_button(True)

		cmds.setParent(self.tabs)
		self.button_listScr_JS=cmds.scrollLayout(vst=1,hst=0,cr=1)
		frameJS=cmds.frameLayout(label=u'角色提交渲染前执行按钮', borderStyle='etchedIn')
		cc=CreateButton()
		cc.create_button(False)

		cmds.tabLayout(self.tabs, edit=True, tabLabel=((self.button_listScr_CJ, u'场景'),(self.button_listScr_JS, u'角色')))
		
		cmds.setParent(paneL)
		self.help_listScr =cmds.scrollLayout(vst=1,hst=0,cr=1)
		cmds.frameLayout('ann_ts_frame',label=u'按钮提示', borderStyle='etchedIn')

		cmds.formLayout(self.maiform,e=True,
								af=[(Help_b,'left',5),(Help_b,'bottom',5),
									(close_b,'right',5),(close_b,'bottom',5),
									(paneL,'left',5),(paneL,'right',5),(paneL,'top',5)],
								ac=[(paneL,'bottom',5,Help_b),(Help_b,'right',5,close_b)],
								ap=[(close_b,'left',0,50)]
								)
		#cmds.tabLayout(self.tabs, edit=True, tabLabel=((frameCJ, u'场景'), (frameCJ, u'角色')))
		cmds.window(self.uiName,e=True,wh=(730,400))
		cmds.showWindow(self.uiName)
	def closeWindow(self,*args):
		'delete UI'
		cmds.deleteUI(self.uiName)
class ZhuButton(object):
	'Create button class'
	label=''
	def __init__(self,isCJ):
		self.buttonlabel=''
		self.isCJ=isCJ
	def saveRenderSetingButtonColorControlDatasCJ(self,baochuanwenjianCJ):
		cmds.fileInfo('zwfRenderSetingButtonColorDatasCJ',str(baochuanwenjianCJ))

	def saveRenderSetingButtonColorControlDatasJS(self,baochuanwenjianJS):
		cmds.fileInfo('zwfRenderSetingButtonColorDatasJS',str(baochuanwenjianJS))

	def setname(self,label):
		'set a name of button'
		self.labelname=label
	def createButton(self):
		'create button core function'
		anform=cmds.formLayout(numberOfDivisions=100)
		self.button=cmds.button(l=self.labelname)
		self.button_labelname()
		if self.isCJ:
			ZWFGlobalbuttonResultCJ[self.button]=[]
			for each in ZWFGlobalbuttonResultCJ:
				ZWFGlobalbuttonResultCJ[each].append(self.button)

			ZWFGlobalbuttonMiddCJ[self.buttonlabel]=[]
			for single in ZWFGlobalbuttonMiddCJ:
				ZWFGlobalbuttonMiddCJ[single].append(self.buttonlabel)

			bb=CheckRenderSeting()
			if self.buttonlabel in bb.zwfRenderSetingButtonColorDatasCJ:
				cmds.button(self.button,e=True,bgc=[0,1,0])
			else:
				cmds.button(self.button,e=True,bgc=[0.51,0.51,0.51])
		else:
			ZWFGlobalbuttonResultJS[self.button]=[]
			for each in ZWFGlobalbuttonResultJS:
				ZWFGlobalbuttonResultJS[each].append(self.button)

			ZWFGlobalbuttonMiddJS[self.buttonlabel]=[]
			for single in ZWFGlobalbuttonMiddJS:
				ZWFGlobalbuttonMiddJS[single].append(self.buttonlabel)

			bb=CheckRenderSeting()
			if self.buttonlabel in bb.zwfRenderSetingButtonColorDatasJS:
				cmds.button(self.button,e=True,bgc=[0,1,0])
			else:
				cmds.button(self.button,e=True,bgc=[0.51,0.51,0.51])

		cmds.button(self.button,e=True,c=self.setbutton_bgc_g)
		self.ht_b=cmds.button(l='H&&T',c=self.button_ts,bgc=[0.51,0.51,0.51])
		self.r_b=cmds.button(l='R',c=self.setbutton_bgc_l,bgc=[0.51,0.51,0.51])
		cmds.formLayout(anform,e=True,
								af=[(self.button,'left',5),(self.button,'top',0),
									(self.r_b,'right',5),(self.r_b,'top',0),
									(self.ht_b,'top',0)],
								ac=[(self.ht_b,'left',1,self.button),(self.ht_b,'right',1,self.r_b)],
								ap=[(self.button,'right',0,70),(self.r_b,'left',0,85)]
								)
	def setbutton_bgc_g(self,*args):
		cmds.button(self.button,e=True,bgc=[0,1,0])
		bb=CheckRenderSeting()
		if self.isCJ:
			if self.buttonlabel not in bb.zwfRenderSetingButtonColorDatasCJ:
				bb.zwfRenderSetingButtonColorDatasCJ.append(self.buttonlabel)
			self.saveRenderSetingButtonColorControlDatasCJ(bb.zwfRenderSetingButtonColorDatasCJ)
		else:
			if self.buttonlabel not in bb.zwfRenderSetingButtonColorDatasJS:
				bb.zwfRenderSetingButtonColorDatasJS.append(self.buttonlabel)
			self.saveRenderSetingButtonColorControlDatasJS(bb.zwfRenderSetingButtonColorDatasJS)

	def setbutton_bgc_l(self,*args):
		if self.isCJ:
			for single in ZWFGlobalbuttonResultCJ[self.button]:
				cmds.button([single],e=True,bgc=[0.51,0.51,0.51])
			bb=CheckRenderSeting()
			if len(bb.zwfRenderSetingButtonColorDatasCJ):
				for each in ZWFGlobalbuttonMiddCJ[self.buttonlabel]:
					if each in bb.zwfRenderSetingButtonColorDatasCJ:
						bb.zwfRenderSetingButtonColorDatasCJ=self.removeItem(bb.zwfRenderSetingButtonColorDatasCJ,each)
				self.saveRenderSetingButtonColorControlDatasCJ(bb.zwfRenderSetingButtonColorDatasCJ)
		else:
			for single in ZWFGlobalbuttonResultJS[self.button]:
				cmds.button([single],e=True,bgc=[0.51,0.51,0.51])
			bb=CheckRenderSeting()
			if len(bb.zwfRenderSetingButtonColorDatasJS):
				for each in ZWFGlobalbuttonMiddJS[self.buttonlabel]:
					if each in bb.zwfRenderSetingButtonColorDatasJS:
						bb.zwfRenderSetingButtonColorDatasJS=self.removeItem(bb.zwfRenderSetingButtonColorDatasJS,each)
				self.saveRenderSetingButtonColorControlDatasJS(bb.zwfRenderSetingButtonColorDatasJS)
	def removeItem(self,oldlist,reItem):
		midlist=[]
		for i in oldlist:
			if i!=reItem:
				midlist.append(i)
		return midlist 

	def button_labelname(self):
		if self.labelname==u'搜索是否带有“_rig_slice.ma”关键字':
			self.buttonlabel='caizhimoxing'
		if self.labelname==u'制作cache文件':
			self.buttonlabel='zhizoudianhuanchuang'
		elif self.labelname==u'切换到材质模型':
			self.buttonlabel='wenjiandianhuanchuan'
		elif self.labelname==u'确认主光方向':
			self.buttonlabel='zhuguangfangxiang'
		elif self.labelname==u'保存角色交互的场景文件':
			self.buttonlabel='baocjuesejiaohuchangjing'
		elif self.labelname==u'设置assetID，并检查':
			self.buttonlabel='shezhiID'
		elif self.labelname==u'导入场景进行优化':
			self.buttonlabel='daoruyouhuachangjing'
		elif self.labelname==u'优化场景':
			self.buttonlabel='youhuachangjing'
		elif self.labelname==u'清除灯光连接':
			self.buttonlabel='deletedengguanglianjie'
		elif self.labelname==u'拷贝贴图至本地':
			self.buttonlabel='tietudaobendi'
		elif self.labelname==u'导出场景影响角色物体(Occ,shadow)':
			self.buttonlabel='daochuchangjingos'
		elif self.labelname==u'导出场景影响角色物体(mask)':
			self.buttonlabel='daochuchangjingmask'
		elif self.labelname==u'导入场景影响角色物体(Occ,shadow)':
			self.buttonlabel='daoruchangjingos'
		elif self.labelname==u'导入场景影响角色物体(mask)':
			self.buttonlabel='daoruchangjingmask'
		elif self.labelname==u'优化无用的材质和材质球':
			self.buttonlabel='youhuamap'
		elif self.labelname==u'优化sssMap':
			self.buttonlabel='youhuasssmap'
		elif self.labelname==u'贴图精度优化':
			self.buttonlabel='daoruHDR'
		elif self.labelname==u'建立HDR环境球':
			self.buttonlabel='jianliHDR'
		elif self.labelname==u'导入相应灯光rig(CJ)':
			self.buttonlabel='daorudengguangrigcj'
		elif self.labelname==u'导入相应灯光rig(JS)':
			self.buttonlabel='daorudengguangrigjs'
		elif self.labelname==u'设置摄像机的远近裁切平面':
			self.buttonlabel='sxjqaiqiu'
		elif self.labelname==u'灯光使用shadowMap(MR)':
			self.buttonlabel='shadowmap'
		elif self.labelname==u'分层设置':
			self.buttonlabel='fengcengshizhi'
		elif self.labelname==u'细分代理':
			self.buttonlabel='xifendaili'
		elif self.labelname==u'另存场景':
			self.buttonlabel='baochunchuangjing'
		elif self.labelname==u'场景渲染测试':
			self.buttonlabel='xuanranceshi'
		elif self.labelname==u'渲染连续5帧(1280尺寸)':
			self.buttonlabel='xuanranwuzhen'
		elif self.labelname==u'文件贴图过滤':
			self.buttonlabel='wenjianguolu'
		elif self.labelname==u'请提高阴影品质':
			self.buttonlabel='yingyingpz'
		elif self.labelname==u'修改原始模型':
			self.buttonlabel='xgyuanshimoxing'
		elif self.labelname==u'贴图路径指回服务器':
			self.buttonlabel='tietiedaofuwuqi'
		elif self.labelname==u'指定渲染前需要执行的mel':
			self.buttonlabel='xuanranmel'
		elif self.labelname==u'另存Occ文件':
			self.buttonlabel='baochuanoccwenjian'
		elif self.labelname==u'文件提交服务器':
			self.buttonlabel='wenjiantijiaofuwuqi'
		elif self.labelname==u'deadline提交渲染':
			self.buttonlabel='deadlinetijiaoxuanran'

	def button_h(self):
		if self.labelname==u'搜索是否带有“_rig_slice.ma”关键字':
			h=u'''
使用文本工具（ultraedit：//server-epic01/Software/PC_Softwares/other_Softwares/book/ultraEdit）打开文件，搜索是否带有“_rig_slice.ma”关键字，如果有，记录下来要求动画切换成带绑定高模文件。（遇到slice文件不做cache要直接做灯光的，操作步骤为灯光制作流程文档注3）。
'''
			return h
		
		if self.labelname==u'制作cache文件':
			h=u'''
第一步通过后，直接提交cache农场，制作cache文件。
'''
			return h

		elif self.labelname==u'切换到材质模型':
			h=u'''
打开cache文件，切换好带材质模型。
'''
			import switchShadingModel as SSM
			SSM.main()
			return h

		elif self.labelname==u'确认主光方向':
			h=u'''
确认主光方向，制作方式(与组长，总监确认)。
'''
			return h

		elif self.labelname==u'保存角色交互的场景文件':
			h=u'''
打开作为角色交互的场景文件，赋予默认材质，去除细分节点，清除灯光连接，打组命名，保存。
'''
			return h

		elif self.labelname==u'设置assetID，并检查':
			h=u'''
请您设置assetID，并检查（必须在Reference时做，Reference可能会在以后的步骤中被破坏）。
'''
			return h

		elif self.labelname==u'导入场景进行优化':
			h=u'''
请您考虑是否导入场景进行优化。
'''
			return h

		elif self.labelname==u'优化场景':
			h=u'''
请您根据镜头优化场景，删除看不到无影响的物体。
'''
			return h

		elif self.labelname==u'清除灯光连接':
			h=u'''
请清除灯光连接。
'''
			mel.eval('RenderSettings')
			return h

		elif self.labelname==u'拷贝贴图至本地':
			h=u'''
使用指定工具拷贝贴图至本地路径。
'''
			return h

		elif self.labelname==u'导出场景影响角色物体(Occ,shadow)':
			h=u'''
根据动画layout及灯光效果图，判断对角色有阴影有遮罩或Occ影响的物体。选择他们另存一个文件供角色制作交互影响时使用（可以自己做简化的模型）
'''
			return h

		elif self.labelname==u'导出场景影响角色物体(mask)':
			h=u'''
根据动画layout及灯光效果图，以及场景做好的分层关系，判断角色和场景之间的遮挡关系，导出相应的模型作为场景对角色的遮挡影响，如果和之前做做阴影和Occ的物体有重叠，请自行考虑是否使用同一文件
'''
			return h

		elif self.labelname==u'导入场景影响角色物体(Occ,shadow)':
			h=u'''
根据镜头导入事先优化的场景，作为场景对角色的 Occ,shadow 的影响。
'''
			return h

		elif self.labelname==u'导入场景影响角色物体(mask)':
			h=u'''
根据镜头导入事先优化的场景，作为场景对角色的 遮挡的影响。
'''
			return h

		elif self.labelname==u'优化无用的材质和材质球':
			h=u'''
优化无用的材质和材质球。
'''
			return h

		elif self.labelname==u'优化sssMap':
			h=u'''
优化sssMap。
'''
			import checkShadingModel as CSM
			CSM.checkShadingModel()
			return h

		elif self.labelname==u'贴图精度优化':
			h=u'''
贴图精度优化。
'''
			return h

		elif self.labelname==u'建立HDR环境球':
			h=u'''
建立HDR环境球，导入对应场次HDR，取消环境球主渲染。
'''
			return h

		elif self.labelname==u'导入相应灯光rig(CJ)':
			h=u'''
导入相应灯光rig, 设置直接光照。注意在摄像机前约束一个只开高光的灯并链接所有眼球。
'''
			return h

		elif self.labelname==u'导入相应灯光rig(JS)':
			h=u'''
导入相应灯光rig（缺少预设文件，和路径设置）, 设置直接光照。注意在摄像机前约束一个只开高光的灯并链接所有眼球。
'''
			return h


		elif self.labelname==u'设置摄像机的远近裁切平面':
			h=u'''
设置摄像机的远近裁切平面（分别是摄像机的NearClipPlane,FarClipPlane值）。MR它只读设置的数值，不自动。
'''
			return h

		elif self.labelname==u'灯光使用shadowMap(MR)':
			h=u'''
对没有场景物件移动的，灯光使用shadowMap（MR）的，注意设置偏移值（一般不用
设置）自阴影，和采样值；对于使用 Raytrace Shadow 的要注意设置灯光阴影半角，
阴影采样射线数，防止噪点闪烁。并且请注意渲染效率，减少使用阴影。
'''
			return h

		elif self.labelname==u'分层设置':
			h=u'''
设置分层（分层工具需要注意的点：阴影，反射等关联的设置，分离灯光，Z,ID等
不要忘记设置，并注意减少 Layer Override 。由于场景灯光种类繁多，分离灯光
请选择性使用提高渲染效率）。设置阴影，反射，遮罩（注意不要忘记设置之前导
入的作为角色影响的场景文件）等关联。使用Pass工具全局设置 ，
使用Global Midfy Shaders来设置AO，Z，ID等（Z，ID必须根据场景场景设置）。
详细使用请参看帮助。
'''
			import Output_Pass_Tool_new as OPTN
			OPTN.call_OutputRenderPasses()
			return h

		elif self.labelname==u'细分代理':
			h=u'''
细分优化（需要模型提交时设置好smoothID，代理为代理，有问题的模型使用smooth）。
'''
			import Addmentalraysubdivisionproxy as addMSP
			addMSP.call_Addmsp()
			return h

		elif self.labelname==u'另存场景':
			h=u'''
另存场景，设置GI场景（渲染面板预制mel，注意GI是32位图片。并且mi_blinn并不支持任何GI。）,和Occ。其实occ最好分开做，因为会对材质进行 Override 大大影响效率。后面有一步制作occ，当时因为场景较小所以一起做了。
'''
			mel.eval('RenderSettings')
			return h

		elif self.labelname==u'场景渲染测试':
			h=u'''
场景渲染测试（渲染面板设置mel），如镜头运动，出多角度全尺寸合成图片。制作一张类似下图的HDR作为角色反射，灯光，GI的参考（需要等正常镜头QC通过，方能制作）。
'''
			return h

		elif self.labelname==u'渲染连续5帧(1280尺寸)':
			h=u'''
成品质量1280尺寸，检测连续5帧（请选择运动镜头），用于检测是否有贴图，模型缝隙，阴影的闪烁。
'''
			mel.eval('RenderSettings')
			return h

		elif self.labelname==u'文件贴图过滤':
			h=u'''
如有贴图闪烁，或者感觉太模糊需要更好的过滤方式保证近景贴图清晰度的，改变贴图的过滤方式为MR的椭圆过滤(脚本更改)。
'''
			mel.eval('RenderSettings')
			return h

		elif self.labelname==u'请提高阴影品质':
			h=u'''
如有阴影闪烁请提高阴影品质。
'''
			return h

		elif self.labelname==u'修改原始模型':
			h=u'''
如有模型闪烁，请适当修改原始模型，保证后续镜头不受其影响。
'''
			return h

		elif self.labelname==u'贴图路径指回服务器':
			h=u'''
所有贴图路径指回服务器。
'''
			return h

		elif self.labelname==u'指定渲染前需要执行的mel':
			h=u'''
指定渲染前需要执行的mel。
'''
			return h

		elif self.labelname==u'另存Occ文件':
			h=u'''
另存Occ文件，删除所有pass。在masterLayer，把mi_blinn转为lambert，转为occ材质(mel)，使用HyperShader的"Delete Unueses Nodes"命令删除无用材质，执行Occ渲染预设，保存文件。
'''
			import Shader_Tool as ST
			ST.shader_ui()
			return h

		elif self.labelname==u'文件提交服务器':
			h=u'''
把该文件提交到服务器上面。
'''
			return h

		elif self.labelname==u'deadline提交渲染':
			h=u'''
deadline提交渲染。
'''
			return h

	def button_ts(self,*args):
		if cmds.columnLayout('RenderSeting_H_col',ex=True):
			cmds.deleteUI('RenderSeting_H_col')
		cmds.columnLayout('RenderSeting_H_col',adj=True,p='ann_ts_frame')
		cmds.scrollField(ww=True,editable=False,text=self.button_h(),h=321,p='RenderSeting_H_col')
#		cmds.text(l=self.button_h(),al='left')

class CreateButton(object):
	def create_button(self,is_CJ):
		if is_CJ:
			labels=[u'搜索是否带有“_rig_slice.ma”关键字',u'制作cache文件',u'切换到材质模型',u'确认主光方向',u'设置assetID，并检查',
					u'导入场景进行优化',u'优化场景',u'清除灯光连接',u'导出场景影响角色物体(Occ,shadow)',u'导出场景影响角色物体(mask)',
					u'优化无用的材质和材质球',u'拷贝贴图至本地',u'贴图精度优化',u'导入相应灯光rig(CJ)',u'设置摄像机的远近裁切平面',
					u'灯光使用shadowMap(MR)',u'分层设置',u'细分代理',u'另存场景',u'场景渲染测试',u'渲染连续5帧(1280尺寸)',
					u'文件贴图过滤',u'请提高阴影品质',u'修改原始模型',u'贴图路径指回服务器',u'指定渲染前需要执行的mel',
					u'另存Occ文件',u'文件提交服务器',u'deadline提交渲染']
		else:
			labels=[u'搜索是否带有“_rig_slice.ma”关键字',u'制作cache文件',u'切换到材质模型',u'确认主光方向',u'保存角色交互的场景文件',u'设置assetID，并检查',
					u'导入场景进行优化',u'清除灯光连接',u'拷贝贴图至本地',u'导入场景影响角色物体(Occ,shadow)',u'导入场景影响角色物体(mask)',
					u'优化sssMap',u'贴图精度优化',u'建立HDR环境球',u'导入相应灯光rig(JS)',u'设置摄像机的远近裁切平面',
					u'灯光使用shadowMap(MR)',u'分层设置',u'细分代理',u'另存场景',u'场景渲染测试',u'渲染连续5帧(1280尺寸)',
					u'文件贴图过滤',u'请提高阴影品质',u'修改原始模型',u'贴图路径指回服务器',u'指定渲染前需要执行的mel',
					u'另存Occ文件',u'文件提交服务器',u'deadline提交渲染']
		an_col=cmds.columnLayout(adj=True,rs=2)
		for label in labels:
			cmds.setParent(an_col)
			bb=ZhuButton(is_CJ)
			bb.setname(label)
			bb.createButton()



def checkR():
	aa=CheckRenderSeting()
	aa.setUiName('checkRenderseting_win')
	aa.creatUi()
if __name__=='__main__':
	checkR()