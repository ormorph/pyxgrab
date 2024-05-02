# -*- coding: utf-8 -*-

# Distributed under dual license GPL-2 and GPL-3
# You can choose any of these licenses.

from PyTQt.tqt import *


class MainWindow(TQWidget):
    def __init__(self,parent = None,name = None,fl = 0):
        TQWidget.__init__(self, parent, name, fl)

        if not name:
            self.setName("MainWindow")


        MainWindowLayout = TQVBoxLayout(self,11,6,"MainWindowLayout")

        self.tabWidget = TQTabWidget(self,"tabWidget")

        self.tab = TQWidget(self.tabWidget,"tab")
        tabLayout = TQVBoxLayout(self.tab,11,6,"tabLayout")

        self.textLabel1 = TQLabel(self.tab,"textLabel1")
        tabLayout.addWidget(self.textLabel1)

        layout9 = TQHBoxLayout(None,0,6,"layout9")

        self.textLabel2 = TQLabel(self.tab,"textLabel2")
        layout9.addWidget(self.textLabel2)

        self.captureOptionsLineEdit = TQLineEdit(self.tab,"captureOptionsLineEdit")
        layout9.addWidget(self.captureOptionsLineEdit)
        tabLayout.addLayout(layout9)

        layout8 = TQHBoxLayout(None,0,6,"layout8")

        self.checkBoxSound = TQCheckBox(self.tab,"checkBoxSound")
        layout8.addWidget(self.checkBoxSound)
        spacer2 = TQSpacerItem(40,20,TQSizePolicy.Expanding,TQSizePolicy.Minimum)
        layout8.addItem(spacer2)
        tabLayout.addLayout(layout8)

        layout6 = TQHBoxLayout(None,0,6,"layout6")

        self.textLabel3 = TQLabel(self.tab,"textLabel3")
        layout6.addWidget(self.textLabel3)

        self.soundOptionsLineEdit = TQLineEdit(self.tab,"soundOptionsLineEdit")
        layout6.addWidget(self.soundOptionsLineEdit)
        tabLayout.addLayout(layout6)

        layout5 = TQHBoxLayout(None,0,6,"layout5")

        self.textLabel4 = TQLabel(self.tab,"textLabel4")
        layout5.addWidget(self.textLabel4)

        self.comboBoxCapture = TQComboBox(self.tab,"comboBoxCapture")
        layout5.addWidget(self.comboBoxCapture)
        tabLayout.addLayout(layout5)

        self.textLabel1_2 = TQLabel(self.tab,"textLabel1_2")
        tabLayout.addWidget(self.textLabel1_2)

        layout6_2 = TQHBoxLayout(None,0,6,"layout6_2")

        self.dirPathEdit = TQLineEdit(self.tab,"dirPathEdit")
        layout6_2.addWidget(self.dirPathEdit)

        self.dirPathButton = TQPushButton(self.tab,"dirPathButton")
        layout6_2.addWidget(self.dirPathButton)
        tabLayout.addLayout(layout6_2)
        spacer3 = TQSpacerItem(20,50,TQSizePolicy.Minimum,TQSizePolicy.Expanding)
        tabLayout.addItem(spacer3)
        self.tabWidget.insertTab(self.tab,TQString.fromUtf8(""))

        self.tab_2 = TQWidget(self.tabWidget,"tab_2")
        tabLayout_2 = TQVBoxLayout(self.tab_2,11,6,"tabLayout_2")

        self.textLabel5 = TQLabel(self.tab_2,"textLabel5")
        tabLayout_2.addWidget(self.textLabel5)

        self.compressLineEdit = TQLineEdit(self.tab_2,"compressLineEdit")
        tabLayout_2.addWidget(self.compressLineEdit)

        self.checkBoxCompress = TQCheckBox(self.tab_2,"checkBoxCompress")
        tabLayout_2.addWidget(self.checkBoxCompress)
        spacer6 = TQSpacerItem(20,40,TQSizePolicy.Minimum,TQSizePolicy.Expanding)
        tabLayout_2.addItem(spacer6)
        self.tabWidget.insertTab(self.tab_2,TQString.fromUtf8(""))
        MainWindowLayout.addWidget(self.tabWidget)

        layout14 = TQHBoxLayout(None,0,6,"layout14")
        spacer1 = TQSpacerItem(40,27,TQSizePolicy.Expanding,TQSizePolicy.Minimum)
        layout14.addItem(spacer1)

        self.okButton = TQPushButton(self,"okButton")
        layout14.addWidget(self.okButton)

        self.cancelButton = TQPushButton(self,"cancelButton")
        layout14.addWidget(self.cancelButton)
        MainWindowLayout.addLayout(layout14)

        self.languageChange()

        self.resize(TQSize(516,398).expandedTo(self.minimumSizeHint()))
        self.clearWState(TQt.WState_Polished)


    def languageChange(self):
        self.setCaption(self.__tr("Settings"))
        self.textLabel1.setText(self.__tr("Video capture options"))
        self.textLabel2.setText(self.__tr("Options video"))
        self.checkBoxSound.setText(self.__tr("Sound"))
        self.textLabel3.setText(self.__tr("Options Sound"))
        self.textLabel4.setText(self.__tr("Capture"))
        self.textLabel1_2.setText(self.__tr("Select save directory"))
        self.dirPathButton.setText(self.__tr("..."))
        self.tabWidget.changeTab(self.tab,self.__tr("X11 grab"))
        self.textLabel5.setText(self.__tr("Options compress"))
        self.checkBoxCompress.setText(self.__tr("Compress"))
        self.tabWidget.changeTab(self.tab_2,self.__tr("Compress"))
        self.okButton.setText(self.__tr("Ok"))
        self.cancelButton.setText(self.__tr("Cancel"))


    def __tr(self,s,c = None):
        return tqApp.translate(b"MainWindow",s.encode(),c)
