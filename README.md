# PyXgrab
**PyXgrab** is a program designed to capture video from the screen using the ffmpeg program. This program is written in Python using the PyTQt and PyTDE packages.

This program uses the following programs as dependencies:

**xwininfo** - to obtain information about the current position and resolution of the selected window when `Window` mode is selected in the settings;

**xrectsel** - to select an area of the screen and obtain information about the selected area if the Size mode is selected.

In the video capture option settings, strings are used in place of which the script substitutes variable values:

**$SCR_SIZE** - a value of the form 1366x768 is substituted, indicating the resolution of the capture area.

**$DISPLAY** - this line is replaced by the value of the DISPLAY system variable and the offset of the position of the captured area.

In the compression option settings, strings are used in place of which the variable values are substituted, these are:

**TARGET_WIDTH** — width of the compressed video;

**TARGET_HEIGHT** — height of the compressed video.

By default, the capture in the settings is registered through pulseaudio; the sound parameters must be edited when you first start it so that there are no crashes due to a missing device. 
Args:
```
-f pulse -i alsa_output.pci-0000_00_1b.0.analog-stereo.monitor -acodec pcm_s16le
```
The audio output device string (example: `alsa_output.pci-0000_00_1b.0.analog-stereo.monitor`) is taken from the output:
```
$ pactl list short sources
```
As a result, at a resolution of 1366x768, the full capture command is:
```
$ ffmpeg -f pulse -i alsa_output.pci-0000_00_1b.0.analog-stereo.monitor -acodec pcm_s16le -f x11grab -s 1366x768 -r 10 -i $DISPLAY -vcodec mpeg4 -q:v 0 /home/USER/screenshot/53572030.mp4
```
By running the command in the console, you can test the functionality of the selected options for **ffmpeg**.

When the compress checkbox is checked in the settings, at the end of the capture the file is converted to a more compressed format, displaying in the progress indicator how many percent of the conversion has already been completed.
Upon completion of compression, in the specified recording directory there will be a file of the form `VID_xxxxxxxx.mp4`, created(converted) based on the file `xxxxxxxx.mp4`, which in turn will be deleted.

-----
### Recommendations for translation

There is a ready-made example in the file `pyxgrab.pro`.
According to the example, add the name of the new translation file with a `.ts` extension to this file, and run the command:
```
$ pytqlupdate pyxgrab.pro
```
If everything is done correctly, then a new file with a .ts extension should appear in the `locale` directory, which can be edited in `tqlinguist`.

----
All installed capture settings are already working; if you uncheck the `Sound` box, you can immediately use the program without editing the parameters. Since everyone’s sound device is different, its parameters must be set manually in the settings.