from inventory import *
from preWindow import *
pre = preWindoww()
pre.preWinRun()
k = list(pre.resolution)
screenSize(k[0],k[1],k[0]/2,k[1]/2)

while True:
    if keyPressed("space"):
        end()
endWait()

