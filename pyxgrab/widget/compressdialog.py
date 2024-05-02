# -*- coding: utf-8 -*-

# Distributed under dual license GPL-2 and GPL-3
# You can choose any of these licenses.

import os, sys, re, subprocess, pathlib, time
from PyTQt.tqt import *
from widget.progressdialog import *

class CompDialog(ProgDialog):
    def __init__(self,parent = None,name = None):
        ProgDialog.__init__(self,parent,name)
        self.ProgressBar.setProgress(0)

    def setFullFilePath(self, x):
        self.full_file = x

    def setCommand(self, command):
        self.ffmpeg_command = command

    def start_ffmpeg_compress(self):
        self.show()
        pipe = subprocess.PIPE
        self.proc = subprocess.Popen(self.ffmpeg_command.split(), stderr=pipe, encoding="utf-8")
        while True:
            time.sleep(0.08)
            line = self.proc.stderr.readline()
            if 'Duration' in line:
                time_list = re.search('(\d{2})\:(\d{2})\:(\d{2})', line)[0].split(':')
                d_sec = int(time_list[0])*3600+int(time_list[1])*60+int(time_list[2])
            elif 'time=' in line:
                time_list = list = re.search('(\d{2})\:(\d{2})\:(\d{2})', line)[0].split(':')
                t_sec = int(time_list[0])*3600+int(time_list[1])*60+int(time_list[2])
                percent = int(t_sec*100/d_sec)
                self.ProgressBar.setProgress(percent)
            if not line:
                break;
        os.remove(self.full_file)
        self.hide()
        self.ProgressBar.setProgress(0)
