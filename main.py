from inventory import *
from preWindow import *
from level1 import *
from mainWindow import *

level = lvlOne()
level.DisplayLvl()

while True:
    if keyPressed("space"):
        end()
