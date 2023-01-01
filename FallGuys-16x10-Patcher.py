import os
import sys
import time
def quitScript():
    print("Quitting...")
    time.sleep(5)
    sys.exit()

os.chdir(sys.path[0])
if os.path.exists("./UnityPlayer.dll"):
    print("UnityPlayer.dll found")
else:
    print("ERROR: UnityPlayer.dll not found. Is this script located in the game directory?")
    quitScript()
with open('UnityPlayer.dll', 'rb') as f:
    unityDLL = bytearray(f.read())
bytes16x9 = b'9\x8e\xe3?'
bytes16x10 = b'\xcd\xcc\xcc?'

byteSequenceIndex = unityDLL.find(bytes16x9)
if byteSequenceIndex != -1:
    print("16:9 byte sequence found at index " + str(byteSequenceIndex))
else:
    print("ERROR: 16:9 index not found! Your UnityPlayer.dll might already be patched...")
    quitScript()
byteSequenceEnd = byteSequenceIndex + len(bytes16x9)
bytearrayIndex = 0
for i in range(byteSequenceIndex, byteSequenceEnd):
    unityDLL[i] = bytes16x10[bytearrayIndex]
    bytearrayIndex += 1
    print("Patching (" + str(bytearrayIndex) + "/4)")
print("Patched\nChecking patch...")
patchCheck = unityDLL.find(bytes16x10)
if patchCheck != -1:
    print("Patched sequence found at index " + str(patchCheck))
else:
    print("ERROR: Patch check failed!")
    quitScript()
print("Writing to UnityPlayer.dll")
with open("UnityPlayer.dll", "wb") as b:
    b.write(unityDLL)
print("Wrote to UnityPlayer.dll\nPatch complete! Exiting now...")
time.sleep(5)
sys.exit