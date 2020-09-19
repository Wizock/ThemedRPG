from pygame_functions import *

#initiation of the game window
screenSize(600,450)
setBackgroundColour((43,43,43))

#initiation of sprites
res1 = makeSprite("images/1280720.png")
res2 = makeSprite("images/1366768.png")
res3 = makeSprite("images/19201080.png")
curs = makeSprite("images/curs.png")
cont = makeSprite("images/check.png")

msg = makeLabel("Choose your resolution", 20, 10,10,fontColour='white',font='Helvetica')
showLabel(msg)
#resolution selection

res = [res1,res2,res3]
resolutionSett = [(1280, 720), (1366,768),(1920,1080)]
moveSprite(res1, 25,60)
showSprite(res1)

moveSprite(res2, 25,159)
showSprite(res2)

moveSprite(res3, 25,258)
showSprite(res3) 

moveSprite(cont,((600-50)/4)*3,325,1)

contLabel = makeLabel("Press the check to confirm resolution choice", 20, (((600-50)/4)*3)-150, 175, fontColour='white',font='Helvetica')

highlight = [False, False, False]

done = False
run = True

def buttonReact(highlight, res):
    for i in range(len(highlight)):
            if highlight[i]:
                transformSprite(res[i],0,0.909090909090909)
    return highlight, res

while run:
    moveSprite(curs, mouseX(),mouseY())
    if spriteClicked(res1) and not highlight[0]:
        (highlight, res) = buttonReact(highlight, res)
        highlight[0] = True
        highlight[1] = False
        highlight[2] = False

    if spriteClicked(res2) and not highlight[1]:
        (highlight, res) = buttonReact(highlight, res)
        highlight[0] = False
        highlight[1] = True
        highlight[2] = False

    if spriteClicked(res3) and not highlight[2]:
        (highlight, res) = buttonReact(highlight, res)
        highlight[0] = False
        highlight[1] = False
        highlight[2] = True

    if spriteClicked(cont):
        for i in range(len(res)):
            if highlight[i]:
                resolution = resolutionSett[i]
                done = True
                break
        if done:
            break

    if mousePressed():
        for i in range(len(highlight)):
            if highlight[i]:
                transformSprite(res[i], 0, 1.1)
                showSprite(cont)
                showLabel(contLabel)
                break

    if keyPressed('esc'):
        run = False

endWait()