# -*- coding: utf-8 -*-

# Distributed under dual license GPL-2 and GPL-3
# You can choose any of these licenses.

import sys
from PyTQt.tqt import *

from widget.mainwindow import MainWindow
from tools.config import SettingConf
import signal

class settingWindow(MainWindow):
    def __init__(self,parent = None,name = None,fl = 0):
        MainWindow.__init__(self,parent,name,fl)
        #config
        self.config = SettingConf()
        self.captureOptionsLineEdit.setText(self.config.getVoptions())
        self.soundOptionsLineEdit.setText(self.config.getSoundOptions())
        self.comboBoxCapture.insertItem(self.__tr("Display"), 0)
        self.comboBoxCapture.insertItem(self.__tr("Window"), 1)
        self.comboBoxCapture.insertItem(self.__tr("Size"), 2)
        self.comboBoxCapture.setCurrentItem(int(self.config.getCaptureSelection()))
        if self.config.getSoundCheck() == 'yes':
            self.checkBoxSound.setChecked(True)
        else:
            self.checkBoxSound.setChecked(False)
        self.dirPathEdit.setText(self.config.getDirPath())

        # Compress
        self.soundOptionsLineEdit.setText(self.config.getSoundOptions())
        self.compressLineEdit.setText(self.config.getCompressVoptions())
        if self.config.getCompressCheck() == 'yes':
            self.checkBoxCompress.setChecked(True)
        else:
            self.checkBoxCompress.setChecked(False)
        self.connect(self.cancelButton, TQ_SIGNAL("clicked()"), self.slotClose)
        self.connect(self.dirPathButton, TQ_SIGNAL("clicked()"), self.slotOpenFileDialog)
        self.connect(self.okButton, TQ_SIGNAL("clicked()"), self.slotSaveSettings)

    def slotSaveSettings(self):
        self.config.setVoptions(str(self.captureOptionsLineEdit.text()))
        self.config.setSoundOptions(str(self.soundOptionsLineEdit.text()))
        self.config.setCaptureSelection(str(self.comboBoxCapture.currentItem()))
        self.config.setDirPath(str(self.dirPathEdit.text()))
        if self.checkBoxSound.isChecked():
            self.config.setSoundCheck('yes')
        else:
            self.config.setSoundCheck('no')

        self.config.setCompressVoptions(str(self.compressLineEdit.text()))
        if self.checkBoxCompress.isChecked():
            self.config.setCompressCheck('yes')
        else:
            self.config.setCompressCheck('no')
        self.config.saveConfig()
        self.close()

    def slotOpenFileDialog(self):
        out_dir = TQFileDialog.getExistingDirectory(self.config.getDirPath(), self)
        if out_dir:
            self.dirPathEdit.setText(out_dir)

    def slotClose(self):
        self.close()
    def __tr(self,s,c = None):
        return tqApp.translate(b"MainWindow",s.encode(),c)
