# Unity 16:10 Patcher
Automatic DLL patcher that can help force games to run with a 16:10 aspect ratio. **You may need to run this script multiple times, as in many cases the byte sequences occurs multiple times throughout the DLL.**

# How it works
This script dumps the contents of a selected DLL into a bytearray, then checks for the byte sequence `b'9\x8e\xe3?'`, or `39 8E E3 3F` when converted to hexadecimal. This value is commonly used to display 16:9 resolutions, at least in Unity. The 16:10 counterpart for this is `CD CC CC 3F`, which is represented with `b'\xcd\xcc\xcc?'`. If the script finds the 16:9 byte sequence in the bytearray, it will replace it with the 16:10 byte sequence, and finally write the patched bytearray to the selected DLL. This script should work with other Unity games, but was made to work with and tested on Fall Guys.

# Warning/Disclaimer
**If you didn't know, randomly replacing byte sequences in game files can make things stop working. Also, if your desired game has any sort of anticheat or validation system, this probably will not work! Worth a shot, though.**

* Tested working on Fall Guys in January 2023 (./UnityPlayer.dll)*
* *Tested working on Hollow Knight in February 2023 (./hollow_knight_Data/Managed/Assembly-CSharp.dll)*
