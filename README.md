# Music-GUI-Volume-Saver
Very basic program to remember and set the volume for the KH2 Music_GUI tool by Xaddgx, for the Nobody May Cry mod.

## Usage
Put music_gui_volume.exe in the Music Tool folder, run music_gui_volume.exe then Music_GUI.exe. That's it.<br>
I have provided a .bat file that will open both exes for convenience.

## How it works
Uses Pymem to read and write the memory address of the volume control.<br>
When you change the volume a volume.ini file will store the last volume level that was set.<br>
Each time you open Music_GUI.exe, if you have music_gui_volume.exe running it will automatically set it to the that level.<br>
Closing Music_GUI.exe will also close music_gui_volume.exe.

## Known Issues
Volume slider does not visually reflect the stored volume level when opening the Music_GUI tool.<br>
Tested on Rev 4 of NMC mod. Will probably only work with that. I will try to keep it updated.
