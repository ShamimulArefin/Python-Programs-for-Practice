# Write a Python program to list all files in a directory in Python

import os
path = "D://Python Programs for Practice"
dir_list = os.listdir(path)
 
print("Files and directories in '", path, "' :")
print(dir_list)