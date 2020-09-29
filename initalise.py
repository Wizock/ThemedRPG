from wizockPreWindow import *
from pygame_functions import *
pre = preWindoww()


def mainWindow():
    pre.preWinRun()
    k = list(pre.resolution)
    screenSize(k[0],k[1],k[0]/2,k[1]/2)  

class hero:
    def __init__(self):
        #this is unnecessarily long, cant you shorten the path to sprites\hero\straight.png, this will allow the game to work on any device, not just your home/school pc
        self.hero = makeSprite("H:\python\Themed RPG\ThemedRPG\sprites\hero\straght.png")
        self.hero_x = 50
        self.hero_y = 50
    def display_player(self):
        showSprite(self.hero)
hero = hero()

class lvlOne:
    mainWindow()
    def __init__(self):
        self.a = list((1920,1080))
        self.b = list(pre.resolution)
    def DisplayLvl(self):
        hideAll()
        hideLabel(pre.msg)
        hideLabel(pre.contLabel)
        hero.display_player()
        #transformSprite(self.hero,0,int(384+(self.b[0]/self.a[0])+(self.b[1]/self.a[1])),0)
        #transformSprite()
level = lvlOne()
level.DisplayLvl()
 

