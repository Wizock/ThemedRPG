import os
import sys

def dirConfirmer():
    workingDirectory = list(os.path.abspath(os.getcwd()))
    if workingDirectory == "c":
        pass
    else:
        os.chdir(workingDirectory[0]+":")
        os.chdir(os.path.abspath(os.getcwd()))
    print(os.getcwd()+"\n")
