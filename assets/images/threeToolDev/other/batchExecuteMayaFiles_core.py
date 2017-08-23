# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\BatchExecuteMayaFiles\batchExecuteMayaFiles_ui.ui'
#
# Created: Thu Nov 03 14:49:20 2011
#      by: PyQt4 UI code generator 4.8.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_batchMayaFiles_window(object):
    def setupUi(self, batchMayaFiles_window):
        batchMayaFiles_window.setObjectName(_fromUtf8("batchMayaFiles_window"))
        batchMayaFiles_window.setWindowModality(QtCore.Qt.NonModal)
        batchMayaFiles_window.setEnabled(True)
        batchMayaFiles_window.resize(708, 510)
        batchMayaFiles_window.setWindowTitle(QtGui.QApplication.translate("batchMayaFiles_window", "B-Maya", None, QtGui.QApplication.UnicodeUTF8))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("icon/batchmayaico.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        batchMayaFiles_window.setWindowIcon(icon)
        batchMayaFiles_window.setWindowOpacity(1.0)
        batchMayaFiles_window.setAutoFillBackground(False)
        self.verticalLayout_3 = QtGui.QVBoxLayout(batchMayaFiles_window)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.Mayapath_Label = QtGui.QLabel(batchMayaFiles_window)
        self.Mayapath_Label.setText(QtGui.QApplication.translate("batchMayaFiles_window", "Maya Path:", None, QtGui.QApplication.UnicodeUTF8))
        self.Mayapath_Label.setObjectName(_fromUtf8("Mayapath_Label"))
        self.horizontalLayout.addWidget(self.Mayapath_Label)
        self.lineEdit = QtGui.QLineEdit(batchMayaFiles_window)
        self.lineEdit.setText(QtGui.QApplication.translate("batchMayaFiles_window", "C:\\Program Files\\Autodesk\\Maya2012\\bin\\maya.exe", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.horizontalLayout.addWidget(self.lineEdit)
        self.OpenMayaPath = QtGui.QPushButton(batchMayaFiles_window)
        self.OpenMayaPath.setText(QtGui.QApplication.translate("batchMayaFiles_window", "open...", None, QtGui.QApplication.UnicodeUTF8))
        self.OpenMayaPath.setObjectName(_fromUtf8("OpenMayaPath"))
        self.horizontalLayout.addWidget(self.OpenMayaPath)
        self.horizontalLayout.setStretch(1, 5)
        self.horizontalLayout.setStretch(2, 1)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.line_1 = QtGui.QFrame(batchMayaFiles_window)
        self.line_1.setFrameShape(QtGui.QFrame.HLine)
        self.line_1.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_1.setObjectName(_fromUtf8("line_1"))
        self.verticalLayout_3.addWidget(self.line_1)
        self.groupBox = QtGui.QGroupBox(batchMayaFiles_window)
        self.groupBox.setTitle(QtGui.QApplication.translate("batchMayaFiles_window", "Maya Files:", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.groupBox)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.MayaFiles_List = QtGui.QListWidget(self.groupBox)
        self.MayaFiles_List.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.MayaFiles_List.setBatchSize(100)
        self.MayaFiles_List.setObjectName(_fromUtf8("MayaFiles_List"))
        self.horizontalLayout_3.addWidget(self.MayaFiles_List)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.AddMayaFiles_B = QtGui.QPushButton(self.groupBox)
        self.AddMayaFiles_B.setText(QtGui.QApplication.translate("batchMayaFiles_window", "add \"+\"", None, QtGui.QApplication.UnicodeUTF8))
        self.AddMayaFiles_B.setObjectName(_fromUtf8("AddMayaFiles_B"))
        self.verticalLayout_2.addWidget(self.AddMayaFiles_B)
        self.SubMayaFiles_B = QtGui.QPushButton(self.groupBox)
        self.SubMayaFiles_B.setText(QtGui.QApplication.translate("batchMayaFiles_window", "sub \"-\"", None, QtGui.QApplication.UnicodeUTF8))
        self.SubMayaFiles_B.setObjectName(_fromUtf8("SubMayaFiles_B"))
        self.verticalLayout_2.addWidget(self.SubMayaFiles_B)
        self.line = QtGui.QFrame(self.groupBox)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.verticalLayout_2.addWidget(self.line)
        self.SelectAllMayaFiles_B = QtGui.QPushButton(self.groupBox)
        self.SelectAllMayaFiles_B.setText(QtGui.QApplication.translate("batchMayaFiles_window", "Select All", None, QtGui.QApplication.UnicodeUTF8))
        self.SelectAllMayaFiles_B.setObjectName(_fromUtf8("SelectAllMayaFiles_B"))
        self.verticalLayout_2.addWidget(self.SelectAllMayaFiles_B)
        self.line_3 = QtGui.QFrame(self.groupBox)
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.verticalLayout_2.addWidget(self.line_3)
        self.Search_N = QtGui.QLineEdit(self.groupBox)
        self.Search_N.setObjectName(_fromUtf8("Search_N"))
        self.verticalLayout_2.addWidget(self.Search_N)
        self.Search_B = QtGui.QPushButton(self.groupBox)
        self.Search_B.setText(QtGui.QApplication.translate("batchMayaFiles_window", "search", None, QtGui.QApplication.UnicodeUTF8))
        self.Search_B.setObjectName(_fromUtf8("Search_B"))
        self.verticalLayout_2.addWidget(self.Search_B)
        self.line_5 = QtGui.QFrame(self.groupBox)
        self.line_5.setFrameShape(QtGui.QFrame.HLine)
        self.line_5.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_5.setObjectName(_fromUtf8("line_5"))
        self.verticalLayout_2.addWidget(self.line_5)
        self.SaveMayafile = QtGui.QCheckBox(self.groupBox)
        self.SaveMayafile.setText(QtGui.QApplication.translate("batchMayaFiles_window", "Save Maya", None, QtGui.QApplication.UnicodeUTF8))
        self.SaveMayafile.setChecked(False)
        self.SaveMayafile.setObjectName(_fromUtf8("SaveMayafile"))
        self.verticalLayout_2.addWidget(self.SaveMayafile)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.horizontalLayout_3.addLayout(self.verticalLayout_2)
        self.horizontalLayout_3.setStretch(0, 6)
        self.horizontalLayout_3.setStretch(1, 1)
        self.verticalLayout_3.addWidget(self.groupBox)
        self.line_2 = QtGui.QFrame(batchMayaFiles_window)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.verticalLayout_3.addWidget(self.line_2)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.MelPath_Label = QtGui.QLabel(batchMayaFiles_window)
        self.MelPath_Label.setText(QtGui.QApplication.translate("batchMayaFiles_window", "Command Path:", None, QtGui.QApplication.UnicodeUTF8))
        self.MelPath_Label.setObjectName(_fromUtf8("MelPath_Label"))
        self.horizontalLayout_2.addWidget(self.MelPath_Label)
        self.lineEdit_2 = QtGui.QLineEdit(batchMayaFiles_window)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.horizontalLayout_2.addWidget(self.lineEdit_2)
        self.OPenMelPath = QtGui.QPushButton(batchMayaFiles_window)
        self.OPenMelPath.setText(QtGui.QApplication.translate("batchMayaFiles_window", "open...", None, QtGui.QApplication.UnicodeUTF8))
        self.OPenMelPath.setObjectName(_fromUtf8("OPenMelPath"))
        self.horizontalLayout_2.addWidget(self.OPenMelPath)
        self.horizontalLayout_2.setStretch(1, 5)
        self.horizontalLayout_2.setStretch(2, 1)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.line_4 = QtGui.QFrame(batchMayaFiles_window)
        self.line_4.setFrameShape(QtGui.QFrame.HLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4.setObjectName(_fromUtf8("line_4"))
        self.verticalLayout_3.addWidget(self.line_4)
        self.Execute_B = QtGui.QPushButton(batchMayaFiles_window)
        self.Execute_B.setMinimumSize(QtCore.QSize(30, 30))
        self.Execute_B.setText(QtGui.QApplication.translate("batchMayaFiles_window", "execute>>", None, QtGui.QApplication.UnicodeUTF8))
        self.Execute_B.setObjectName(_fromUtf8("Execute_B"))
        self.verticalLayout_3.addWidget(self.Execute_B)

        self.retranslateUi(batchMayaFiles_window)
        QtCore.QMetaObject.connectSlotsByName(batchMayaFiles_window)

    def retranslateUi(self, batchMayaFiles_window):
        pass


#############################--core--##############################
import sys,os,subprocess
def addpath(pathName=''):
	if pathName not in sys.path:
		sys.path.insert(0,pathName)
addpath('Z:\\WorkflowTools\\Epic\\lib\\pyQt\\PyQt_2.7_x64')
from PyQt4 import QtGui,QtCore
import batchExecuteMayaFiles_ui as batchEMF
class BatchExecuteMayaFiles(batchEMF.Ui_batchMayaFiles_window,QtGui.QWidget):
	def __init__(self):
		QtGui.QWidget.__init__(self)
		self.setupUi(self)
		self.path=os.path.join(os.path.dirname(os.path.abspath(sys.argv[0])),'img')
		icon=QtGui.QIcon(os.path.join(self.path,'batchmayaico.png'))
		self.setWindowIcon(icon)
		searchIcon=QtGui.QIcon(os.path.join(self.path,'search.png'))
		self.Search_B.setIcon(searchIcon)
	def selectAllfiles(self,bool):
		allrows=self.MayaFiles_List.count()
		if allrows:
			for row in range(allrows):
				item=self.MayaFiles_List.item(row)
				self.MayaFiles_List.setItemSelected(item,bool)
	def getAllItemsString(self):
		stringList=[]
		allrows=self.MayaFiles_List.count()
		if allrows:
			for row in range(allrows):
				item=self.MayaFiles_List.item(row)
				text=item.text()
				stringList.append(text)
		return stringList
	def addMayaFiles(self):
		filters="files (*.ma *.mb);;ma (*.ma);;mb (*.mb)"
		filenames=QtGui.QFileDialog.getOpenFileNames(self,'add maya files','/home',filters)
		if len(filenames):
			allItemsString=self.getAllItemsString()
			for filename in filenames:
				if filename not in allItemsString:
					mayaicon=QtGui.QIcon(os.path.join(self.path,'mayaico.png'))
					mayaitemName=QtGui.QListWidgetItem()
					mayaitemName.setText(filename)
					mayaitemName.setIcon(mayaicon)
					self.MayaFiles_List.addItem(mayaitemName)
				else:
					print '"%s" was existed!'%filename
	def subMayaFiles(self):
		items=self.MayaFiles_List.selectedItems()
		if len(items):
			for single in items:
				row=self.MayaFiles_List.row(single)
				self.MayaFiles_List.takeItem(row)
		else:
			print "No selected (please selcet items in maya files list)!"
	def filesOpen(self):
		filters="maya//mel//py (*.exe *.mel *.py)"
		file=QtGui.QFileDialog.getOpenFileName(self,'open','/home',filters)
		return file
	def setPath(self,lineEdit):
		file=self.filesOpen()
		file.replace('/','\\')
		lineEdit.setText(file)
	def searchFiles(self):
		search_key=self.Search_N.text()
		self.selectAllfiles(False)
		if len(search_key):
			allrows=self.MayaFiles_List.count()
			if allrows:
				for row in range(allrows):
					item=self.MayaFiles_List.item(row)
					text=item.text()
					if str(search_key).lower() in str(text).lower():
						self.MayaFiles_List.setItemSelected(item,True)
		else:
			print "NO words in search filed!!"
	def executeFunction(self):
		mayaPath=self.lineEdit .text()
		melPath=self.lineEdit_2.text()
		mayaFiles=self.MayaFiles_List.selectedItems()
		if len(mayaPath):
			if len(melPath):
				melbasename=self.GeneratedMelFile(melPath)
				if melbasename==0:
					print "Execute error! please check exist \"D:\" or \"command file \"ext ('.mel','.py')!!!"
					return
				filesize=len(mayaFiles)
				if filesize:
					for file in mayaFiles:
						filePath=file.text()
						cmd='"%s" -file "%s" -command "source %s" -prompt'%(mayaPath,filePath,melbasename)
						subprocess.call(cmd,shell=True)
				else:
					print 'No files were selected in list!'
			else:
				print 'NO command file!'
		else:
			print 'No maya path!'
	def GeneratedMelFile(self,cpath):
		cpath=str(cpath)
		dir=os.path.dirname(cpath)
		base=os.path.basename(cpath)
		P_splitext=os.path.splitext(base)
		doc_pwin=os.path.join(os.getenv("USERPROFILE"),'Documents\\maya\\scripts')
		doc_pxp=os.path.join(os.getenv("USERPROFILE"),'My Documents\\maya\\scripts')
		if os.path.isdir(doc_pwin):
			melp=doc_pwin
		elif os.path.isdir(doc_pxp):
			melp=doc_pxp
		else:
			melp='D:\\MelTemps\\mel'
			try:
				if not os.path.isdir(melp):
					os.makedirs(melp)
				if 'MAYA_SCRIPT_PATH' in os.environ:
					scriptpaths=os.environ['MAYA_SCRIPT_PATH']
					if scriptpaths[-1]!=';':
						scriptpaths+=';'
					scriptpaths+=melp
				else:
					scriptpaths=melp
				comm='setx MAYA_SCRIPT_PATH "%s"'%scriptpaths
				subprocess.call(comm,shell=True)
			except:
				print 'No "D:" in your system!'
				return 0
		if self.SaveMayafile.checkState()==2:
			ss="file -save;"
		else:
			ss=""
		if P_splitext[-1]=='.mel':
			nn='source "%s";'%cpath.replace('\\','/')
		elif P_splitext[-1]=='.py':
			nn='python("import sys\\nif \\"%s\\" not in sys.path:\\n    sys.path.insert(0,\\"%s\\")\\nimport %s");'%(dir.replace('\\','/'),dir.replace('\\','/'),P_splitext[0])
		else:
			nn=''
			return 0
		mel='%s\\%s_Mel.mel'%(melp,P_splitext[0])
		if os.path.isdir(mel):
			os.remove(mel)
		script='''global proc %s_MEL()
{
	%s
	%s
	quit -f;
}
%s_MEL;
'''%(P_splitext[0],nn,ss,P_splitext[0])
		ff=open(mel,"w")
		try:
			ff.write(script)
		finally:
			ff.close()
		return '%s_Mel.mel'%P_splitext[0]
def BatchEMF_DY():
	app=QtGui.QApplication(sys.argv)
	bb=BatchExecuteMayaFiles()
	bb.show()
	bb.OpenMayaPath.clicked.connect(lambda *args:bb.setPath(bb.lineEdit))
	bb.connect(bb.AddMayaFiles_B,QtCore.SIGNAL('clicked()'),bb.addMayaFiles)
	bb.connect(bb.SubMayaFiles_B,QtCore.SIGNAL('clicked()'),bb.subMayaFiles)
	bb.SelectAllMayaFiles_B .clicked.connect(lambda *args:bb.selectAllfiles(True))
	bb.Search_B .clicked.connect(bb.searchFiles)
	bb.OPenMelPath.clicked.connect(lambda *args:bb.setPath(bb.lineEdit_2))
	bb.Execute_B.clicked.connect(bb.executeFunction)
	sys.exit(app.exec_())
if __name__=='__main__':
	BatchEMF_DY()
