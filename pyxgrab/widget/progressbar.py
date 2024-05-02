# -*- coding: utf-8 -*-

# Distributed under dual license GPL-2 and GPL-3
# You can choose any of these licenses.

from PyTQt.tqt import *


class Form1(TQDialog):
    def __init__(self,parent = None,name = None,modal = 0,fl = 0):
        TQDialog.__init__(self,parent,name,modal,fl)

        if not name:
            self.setName("Form1")


        Form1Layout = TQVBoxLayout(self,11,6,"Form1Layout")

        self.ProgressBar = TQProgressBar(self,"ProgressBar")
        Form1Layout.addWidget(self.ProgressBar)

        self.languageChange()

        self.resize(TQSize(386,74).expandedTo(self.minimumSizeHint()))
        self.clearWState(TQt.WState_Polished)


    def languageChange(self):
        self.setCaption(self.__tr("Compress dialog"))


    def __tr(self,s,c = None):
        return tqApp.translate(b"Form1",s.encode(),c)
