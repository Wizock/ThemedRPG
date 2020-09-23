from preWindow import *
from mainWindow import *

class lvlOne:
    mainWindow()
    def __init__(self):
        self.hero = makeSprite("H:\python\Themed RPG\ThemedRPG\sprites\hero\straght.png")
    def DisplayLvl(self):
        hideAll()
        hideLabel(pre.msg)
        hideLabel(pre.contLabel)
        self.a = list((1920,1080))
        self.b = list(pre.resolution)
        transformSprite(self.hero,(self.b[0]/self.a[0])+(self.b[1]/self.a[1]),0)
        showSprite(self.hero)

    