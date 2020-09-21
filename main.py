import os.path
from os import path
import sys

'''
#TODO 
    first figure out the path [x]
    put the path into a array [x]
    make the element of the array into a index var and then check if its c [x]
        if its c then simply cd [x]
        otherwise use the disc pre-fix as a drive cd and then cd to the actual dir {x}
        then individually add the paths {}
'''


workingDirectory = list(os.path.abspath(os.getcwd()))

if workingDirectory == "c":
    pass
else:
    os.chdir(workingDirectory[0]+":")
    os.chdir(os.path.abspath(os.getcwd()))
print(os.getcwd())

if path.exists(str(workingDirectory)):
    print("works")
else:
    print("doesnt work")

from lib import preWindow 
from lib import main_window
from lib.pygame_ import pygame_functions
