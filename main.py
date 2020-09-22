from inventory import *
from preWindow import *
from level1 import *
from mainWindow import *

levelone = lvlOne()
levelone.DisplayLvl()

while True:
    if keyPressed("space"):
        end()
