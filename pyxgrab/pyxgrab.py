#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Distributed under dual license GPL-2 and GPL-3
# You can choose any of these licenses.

import sys, os
from PyTQt.tqt import *
from tdeui import *
from tdecore import i18n, TDEApplication
from widget.systray import *
import signal

locale_dir = './locale/'
tFile = 'pyxgrab_'

def get_translate(lang):
    global  locale_dir, tFile
    language = tFile + lang + ".qm"
    translator = TQTranslator(None)
    translator.load(language,os.path.abspath(locale_dir))
    return translator

if __name__ == "__main__":
    appName = b'PyXgrab'
    a = TDEApplication (sys.argv, appName)
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    TQObject.connect(a,TQ_SIGNAL("lastWindowClosed()"),a,TQ_SLOT("quit()"))
    lang = str(TQLocale(TQTextCodec.locale()).name())
    if os.path.isfile(os.path.join(locale_dir , tFile + lang + '.qm')):
        translator = get_translate(lang)
        tqApp.installTranslator(translator)
    systray = SysTray()
    systray.show()
    a.exec_loop()
