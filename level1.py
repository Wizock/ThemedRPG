from preWindow import *
from mainWindow import *

class lvlOne:
    mainWindow()
    def __init__(self):

        self.hero = makeSprite("sprites/hero/straight.png")
    def DisplayLvl(self):
        hideAll()
        hideLabel(pre.msg)
        hideLabel(pre.contLabel)
        showSprite(self.hero)

    