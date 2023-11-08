# Music-GUI-Volume-Saver
Very basic program to remember and set the volume for the KH2 Music_GUI tool by Xaddgx, for the Nobody May Cry mod.

## Usage
Put music_gui_volume.exe in the Music Tool folder, run music_gui_volume.exe. That's it.<br>

## How it works
Uses Pymem to read and write the memory address of the volume control.<br>
When you change the volume a volume.ini file will store the last volume level that was set.<br>
Each time you open music_gui_volume.exe it will automatically open and set Music_GUI's volume to the that level.<br>

## Known Issues
- Volume slider does not visually reflect the stored volume level when opening the Music_GUI tool.<br>
- Closing the console window leaves Music_GUI.exe hanging for a couple seconds before closing. Type Ctrl+C in the console window to close everything immediately.
