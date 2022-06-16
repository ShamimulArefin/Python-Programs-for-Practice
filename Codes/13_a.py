# Write a Python program to get OS name, platform and release information.

import os
import platform

print("OS name : ",os.name)
print("Platform name : ",platform.system())
print("Release information : ", platform.release())