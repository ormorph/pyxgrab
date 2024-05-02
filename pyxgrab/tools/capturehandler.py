# -*- coding: utf-8 -*-

# Distributed under dual license GPL-2 and GPL-3
# You can choose any of these licenses.

import sys, os, re, time,subprocess, threading
from datetime import datetime
from PyTQt.tqt import *
from tools.config import SettingConf
from widget.compressdialog import *

class CaptureHandler(TQObject):
    def __init__(self,parent = None,name = None):
        TQObject.__init__(self, parent, name)
        self.connect(parent, PYSIGNAL('start()'), self.start)
        self.connect(parent, PYSIGNAL('stop()'), self.stop)
        self.progress = CompDialog()
        self.connect(self.progress, PYSIGNAL('stopped()'), parent.slotStopped)

    def load_settings(self):
        self.config = SettingConf()
        self.video_args = self.config.getVoptions()
        if self.config.getSoundCheck() == 'yes':
            self.video_args = self.config.getSoundOptions() + ' ' + self.video_args

        self.file_name = self.newFile()

        if self.config.getCaptureSelection() == '0':
            self.video_args = re.sub(r'\$DISPLAY', os.environ['DISPLAY'], self.video_args)
            self.video_args = re.sub(r'\$SCR_SIZE', self.getDisplayScreen(), self.video_args)
        elif self.config.getCaptureSelection() == '1':
            self.new_ffmpeg_args(self.get_xwininfo())
        elif self.config.getCaptureSelection() == '2':
            self.new_ffmpeg_args(self.get_xrectsel())

        self.ffmpeg_command = 'ffmpeg' + ' ' + self.video_args + ' ' + self.config.getDirPath() + '/' + self.file_name

    def newFile(self):
        now = datetime.now()
        file_name = now.strftime("%s-%d-%m-%Y") + '.mp4'
        return file_name

    def getDisplayScreen(self):
        width = tqApp.desktop().screen().width()
        height = tqApp.desktop().screen().height()
        self.screenCoords = [width, height]
        return str(width) + 'x' + str(height)

    def get_xwininfo(self):
        pipe = subprocess.PIPE
        time.sleep(0.5)
        proc = subprocess.Popen("xwininfo", stdout = pipe, encoding="utf-8")
        geometry = None
        while True:
            line = proc.stdout.readline()
            if 'geometry' in line:
                geometry = re.sub(r'\+|x|-|geometry', ' ', line).split()
            if 'Absolute upper-left X' in line:
                x_offset = re.search('\d{0,5}$', line)[0]
            if 'Absolute upper-left Y' in line:
                y_offset = re.search('\d{0,5}$', line)[0]
            if not line:
                break;
        geometry[2] = x_offset
        geometry[3] = y_offset
        if int(geometry[0]) % 2 != 0:
            geometry[0] = str(int(geometry[0])-1)
        if int(geometry[1]) % 2 != 0:
            geometry[1] = str(int(geometry[1])-1)

        self.screenCoords = geometry
        return geometry

    def new_ffmpeg_args(self, x):
            display = os.environ['DISPLAY'] + '+' + str(x[2]) + ',' + str(x[3])
            scrSize = str(x[0]) + 'x' + str(x[1])
            self.video_args = re.sub(r'\$DISPLAY', display, self.video_args)
            self.video_args = re.sub(r'\$SCR_SIZE', scrSize, self.video_args)

    def get_xrectsel(self):
        pipe = subprocess.PIPE
        time.sleep(0.5)
        proc = subprocess.Popen("xrectsel", stdout = pipe, encoding="utf-8")
        geometry = None
        while True:
            line = proc.stdout.readline()
            if re.search(r'\d{1,5}', line):
                screen_size = re.search(r'\d{1,5}x\d{1,5}', line)[0]
                offset = re.search(r'\+\d{1,5}\+\d{1,5}', line)[0]
            if not line:
                break;
        geometry = screen_size.split('x')
        geometry.append(offset.split('+')[1])
        geometry.append(offset.split('+')[2])
        if int(geometry[0]) % 2 != 0:
            geometry[0] = str(int(geometry[0])-1)
        if int(geometry[1]) % 2 != 0:
            geometry[1] = str(int(geometry[1])-1)
        self.screenCoords = geometry
        return geometry

    def get_compress_command(self):
        ffmpef_args = self.config.getCompressVoptions()
        ffmpef_args = re.sub(r'TARGET_WIDTH', str(self.screenCoords[0]), ffmpef_args)
        ffmpef_args = re.sub(r'TARGET_HEIGHT', str(self.screenCoords[1]), ffmpef_args)
        ffmpeg_command = "ffmpeg -i " + self.config.getDirPath() + '/' + self.file_name + ' ' \
                   + ffmpef_args + ' ' + self.config.getDirPath() + '/' + 'VID_' + self.file_name
        return ffmpeg_command

    def star_ffmpeg_process(self):
        self.pipe = subprocess.PIPE
        self.proc = subprocess.Popen(self.ffmpeg_command.split(), stdin = self.pipe, stdout = self.pipe, stderr = self.pipe)
        self.emit(PYSIGNAL('proc()'), (self.proc,))

    def start_ffmpeg_compress(self):
        ffmpeg_command = self.get_compress_command()
        full_file = self.config.getDirPath() + '/' + self.file_name
        self.progress.setFullFilePath(full_file)
        self.progress.setCommand(ffmpeg_command)
        progress_thread = threading.Thread(target=self.progress.start_ffmpeg_compress)
        progress_thread.start()

    def start(self):
        self.load_settings()
        self.star_ffmpeg_process()

    def stop(self):
        self.proc.communicate(b'q\n')
        self.proc.wait()
        if self.config.getCompressCheck() == 'yes':
            self.start_ffmpeg_compress()
