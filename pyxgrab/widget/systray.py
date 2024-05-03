# -*- coding: utf-8 -*-

# Distributed under dual license GPL-2 and GPL-3
# You can choose any of these licenses.

import sys, os, threading
from PyTQt.tqt import *
from tdeui import TDEMainWindow, KSystemTray, TDEPopupMenu, TDEActionCollection, KStdAction, TDEAction
from tdecore import i18n, TDEAboutData, TDEApplication, TDECmdLineArgs, TDEIcon, TDEIconLoader
from widget.settingwindow import *
from tools.capturehandler import *

class SysTray(KSystemTray):
    def __init__(self,parent = None,name = None, fl = 0):
        super().__init__()
        self.iconStat = False
        # Create Menu
        self.menu = self.contextMenu()
        self.menu.changeTitle(-2, "PyXgrab")
        self.start = TDEAction(self.__tr("Start"), TQIconSet(TQPixmap("./icons/start.png")))
        self.stop = TDEAction(self.__tr("Stop"))
        self.stop.setIconSet(TQIconSet(TQPixmap("./icons/stop.png")))
        self.about = TDEAction(self.__tr("About"))
        self.settings = TDEAction(self.__tr("Settings"))
        self.connect(self.start,TQ_SIGNAL("activated()"), self.slotStart)
        self.connect(self.stop,TQ_SIGNAL("activated()"), self.slotStop)
        self.connect(self.settings, TQ_SIGNAL("activated()"), self.settingWindowSow)
        self.connect(self.about,TQ_SIGNAL("activated()"), self.aboutMessage)
        self.connect(self, PYSIGNAL('clicked()'), self.slotClicked)
        self.start.plug(self.menu)
        self.stop.plug(self.menu)
        self.settings.plug(self.menu)
        self.about.plug(self.menu)
        self.start.setEnabled(True)
        self.stop.setEnabled(False)
        self.contextMenuAboutToShow(self.menu)
        self.icons = TQPixmap(os.path.join('./icons', 'start.png'))
        self.setPixmap(self.icons)
        self.captureHandler = CaptureHandler(self)
        self.connect(self.captureHandler, PYSIGNAL('proc()'), self.getProc)

    def settingWindowSow(self):
        self.settingWindow =  settingWindow()
        self.settingWindow.show()

    def aboutMessage(self):
        TQMessageBox.information(self, "About", self.__tr(
            "<h3>PyXgrab</h3><hr>"
            "<p>This is a program for capturing video "
             "from the screen.</p>"
            "<p>This application uses ffmpeg to capture the screen.</p>"
            "by Roman Popov "
            "<i>(roma251078@mail.ru)</i>"
            "<hr>"),self.__tr("Cancel"))

    def mouseReleaseEvent(self, event):
        if event.button() == TQt.LeftButton:
            self.emit(PYSIGNAL('clicked()'), ())

    def stop_click_init(self):
        self.icons = TQPixmap(os.path.join('./icons', 'start.png'))
        self.setPixmap(self.icons)
        self.start.setEnabled(True)
        self.stop.setEnabled(False)
        self.iconStat = False

    def start_click_init(self):
        self.icons = TQPixmap(os.path.join('./icons', 'stop.png'))
        self.setPixmap(self.icons)
        self.start.setEnabled(False)
        self.stop.setEnabled(True)
        self.iconStat = True

    def slotClicked(self):
        if self.iconStat:
            self.stop_click_init()
            self.emit(PYSIGNAL('stop()'), ())
        else:
            self.start_click_init()
            self.emit(PYSIGNAL('start()'), ())

    def slotStart(self):
        self.start_click_init()
        self.emit(PYSIGNAL('start()'), ())

    def slotStop(self):
        self.stop_click_init()
        self.emit(PYSIGNAL('stop()'), ())

    def getProc(self, x):
        self.proc = x
        self.connect(self, PYSIGNAL('stopProc()'), self.stop_click_init)
        thread = threading.Thread(target=self.procWait)
        thread.start()

    def procWait(self):
        self.proc.wait()
        self.emit(PYSIGNAL('stopProc()'), ())
        self.proc = None

    def closeEvent(self, e):
        try:
            if self.proc:
                self.proc.terminate()
        except:
            self.proc=None
        e.accept()

    def __tr(self,s,c = None):
        return tqApp.translate(b"MainWindow",s.encode(),c)
