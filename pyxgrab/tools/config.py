# -*- coding: utf-8 -*-

# Distributed under dual license GPL-2 and GPL-3
# You can choose any of these licenses.

import os
import configparser
from pathlib import Path

class SettingConf:
    def __init__(self):
        self.confdir = Path.joinpath(Path.home(), '.pyxgrab')
        self.configfile = Path.joinpath(self.confdir, 'pyxgrab.ini')
        self.getconfig()

    def cerate_settings_file(self):
        self.config['capture'] = {'video': '-f x11grab -s $SCR_SIZE -r 10 -i $DISPLAY -vcodec mpeg4 -q:v 0',
                            'sound': '-f pulse -i bluez_output.E7_50_5B_0B_9C_43.1.monitor -acodec pcm_s16le',
                            'sound_check': 'yes',
                            'capture': '1',
                            'dir_path': str(Path.home()) + '/screenshot'}
        self.config['compress'] = {'video': '-acodec libmp3lame -ab 192k -ac 2 -vcodec libx264 -vf scale=TARGET_WIDTH:TARGET_HEIGHT',
                                   'compress_check': 'yes'}
        with open(self.configfile, 'w') as w_configfile:
            self.config.write(w_configfile)

    def getconfig(self):
        self.config = configparser.ConfigParser()
        if not Path.is_dir(self.confdir):
            Path.mkdir(self.confdir)
        if not Path.is_file(self.configfile):
            self.cerate_settings_file()
        else:
            self.config.read(self.configfile)

    def getVoptions(self):
        return self.config['capture']['video']

    def getSoundOptions(self):
        return self.config['capture']['sound']

    def getSoundCheck(self):
        return self.config['capture']['sound_check']

    def getCaptureSelection(self):
        return self.config['capture']['capture']

    def getDirPath(self):
        return self.config['capture']['dir_path']

    def getCompressVoptions(self):
        return self.config['compress']['video']

    def getCompressCheck(self):
        return self.config['compress']['compress_check']

    def setVoptions(self, x):
        self.config['capture']['video'] = x

    def setSoundOptions(self, x):
        self.config['capture']['sound'] = x

    def setSoundCheck(self, x):
        self.config['capture']['sound_check'] = x

    def setCaptureSelection(self, x):
        self.config['capture']['capture'] = x

    def setDirPath(self, x):
        self.config['capture']['dir_path'] = x

    def setCompressVoptions(self, x):
        self.config['compress']['video'] = x

    def setCompressCheck(self, x):
        self.config['compress']['compress_check'] = x

    def saveConfig(self):
        with open(self.configfile, 'w') as w_configfile:
            self.config.write(w_configfile)
