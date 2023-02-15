import os
import sys
import time
def quitScript():
    print("Quitting...")
    time.sleep(5)
    sys.exit()

confirmationPrompt = ""
print("Input the file path to the DLL you wish to patch")
#Both absolute and relative paths should work fine
filePath = input()
os.chdir(sys.path[0])
if os.path.exists(filePath):
    if filePath[-3:] == "dll":
        print("DLL Selected")
    else:
        print("File selected does not appear to be a DLL. Patch anyway?")
        confirmationPrompt = input("Y/N: ")
        if not confirmationPrompt.lower() == "y":
            quitScript()
else:
    print("ERROR: Directory '" + filePath + "' does not appear to be valid.")
    quitScript()
with open(filePath, 'rb') as f:
    unityDLL = bytearray(f.read())
bytes16x9 = b'9\x8e\xe3?'
bytes16x10 = b'\xcd\xcc\xcc?'

byteSequenceIndex = unityDLL.find(bytes16x9)
if byteSequenceIndex != -1:
    print("16:9 byte sequence found at index " + str(byteSequenceIndex))
else:
    print("ERROR: 16:9 index not found! Your DLL might already be patched, or you're selecting the wrong DLL...")
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
    print("ERROR: Patch check failed! (This really shouldn't happen, like ever. Try running again)")
    quitScript()
print("Writing to file")
with open(filePath, "wb") as b:
    b.write(unityDLL)
print("Wrote to DLL\nPatch complete! Exiting now...")
time.sleep(3)
sys.exit
