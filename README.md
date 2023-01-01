# Fall Guys 16:10 Patcher
Automatic UnityPlayer.dll patcher that forces 16:10 resolutions, written in Python. **Place this script in the directory that includes UnityPlayer.dll before running.**

# How it works
This script dumps the contents of UnityPlayer.dll into a bytearray, then checks for the byte sequence `b'9\x8e\xe3?'`, or `39 8E E3 3F` when converted to hexadecimal. This value is commonly used to display 16:9 resolutions in Unity. The 16:10 counterpart for this is `CD CC CC 3F`, which is represented with `b'\xcd\xcc\xcc?'`. If the script finds the 16:9 byte sequence in the bytearray, it will replace it with the 16:10 byte sequence, and finally write the patched bytearray to UnityPlayer.dll. This script should theoretically work with other Unity games, but was made with Fall Guys in mind.

*Tested working on Steam Deck with SteamOS Holo 3.4.4*
