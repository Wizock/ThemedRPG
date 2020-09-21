from pygame_functions import *

class preWindoww:
    def __init__(self):
        #initiation of the game window
        screenSize(600,450);
        setBackgroundColour((43,43,43))
        #initiation of sprites
        self.res1 = makeSprite("images/1280720.png")
        self.res2 = makeSprite("images/1366768.png")
        self.res3 = makeSprite("images/19201080.png")
        self.curs = makeSprite("images/curs.png")
        self.cont = makeSprite("images/check.png")
        self.msg = makeLabel("Choose your resolution", 20, 10,10,fontColour='white',font='Helvetica')
        self.res = [self.res1,self.res2,self.res3]
        self.contLabel = makeLabel("Press the check to confirm resolution choice", 20, (((600-50)/4)*3)-150, 175, fontColour='white',font='Helvetica')
        self.highlight = [False, False, False]
        self.done = False
        self.run = True
        self.resolutionSett = [(1280, 720), (1366,768),(1920,1080)]
        showLabel(self.msg)
        #resolution selection
        moveSprite(self.res1, 25,60)
        showSprite(self.res1)
        moveSprite(self.res2, 25,159)
        showSprite(self.res2)
        moveSprite(self.res3, 25,258)
        showSprite(self.res3) 
        moveSprite(self.cont,((600-50)/4)*3,325,1)

# function to show the confirming button
    def buttonReact(self,highlight, res):
        for i in range(len(self.highlight)):
                if self.highlight[i]:
                    transformSprite(self.res[i],0,0.909090909090909)
                    
        return self.highlight, self.res

    def preWinRun(self):
        while self.run:
            moveSprite(self.curs, mouseX(),mouseY())
            if spriteClicked(self.res1) and not self.highlight[0]:
                (self.highlight, self.res) = self.buttonReact(self.highlight, self.res)
                self.highlight[0] = True
                self.highlight[1] = False
                self.highlight[2] = False
            if spriteClicked(self.res2) and not self.highlight[1]:
                (self.highlight, self.res) = self.buttonReact(self.highlight, self.res)
                self.highlight[0] = False
                self.highlight[1] = True
                self.highlight[2] = False
            if spriteClicked(self.res3) and not self.highlight[2]:
                (self.highlight, self.res) = self.buttonReact(self.highlight, self.res)
                self.highlight[0] = False;
                self.highlight[1] = False;
                self.highlight[2] = True
            if spriteClicked(self.cont):
                for i in range(len(self.res)):
                    if self.highlight[i]:
                        self.resolution = self.resolutionSett[i]
                        self.done = True
                        break
                if self.done:
                    break
            if mousePressed():
                for i in range(len(self.highlight)):
                    resolution  = self.highlight[i]
                    if resolution:
                        transformSprite(self.res[i], 0, 1.1)
                        showSprite(self.cont)
                        showLabel(self.contLabel)
                        print(f"you have chosen{self.resolutionSett[i]}")
                        break
            if keyPressed('esc'):
                run = False

