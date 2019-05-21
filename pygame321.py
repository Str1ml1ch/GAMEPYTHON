import pygame, sys
from pygame.locals import *
from time import time

window = pygame.display.set_mode((1400,700))
pygame.display.set_caption(('Snowboarder GO!!!'))
screen = pygame.Surface((1400,700))
pygame.display.set_icon(pygame.image.load("asd.png"))
clock = pygame.time.Clock()
pygame.mouse.set_visible(False)
pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 70)
class Sprite:
    def __init__(self,xpos,ypos,filename):
        self.x = xpos
        self.y = ypos
        self.bitmap = pygame.image.load(filename)
        self.bitmap.set_colorkey((0,0,0))
    def render(self):
        screen.blit(self.bitmap,(self.x,self.y))
#res_x = [0]
#res_y = [0]
incrementX = 0

def Connect(x1,x2,y1,y2):
    if(x1 > x2-40) and (x1 < x2+40) and (y1>y2 -72) and (y1 < y2+72):
        return 1
    else:
        return 0
def mytimer():
    global microsseconds,seconds,minutes
    microsseconds+=1.6667
    if microsseconds >= 100:
        seconds+=1
        microsseconds = 0
    if seconds ==60:
        minutes +=1
        seconds = 0
    res = str(minutes)+":"+str(seconds)+":"+str(microsseconds)
    return res
IsJump = False
JumpCount = 15
time =""
zet = Sprite(100,350,'jb1.png')#200x200
zet1 = Sprite(400,260,'jb1.png')#200x200
zet2 = Sprite(700,200,'jb1.png')#200x200
zet3 = Sprite(1100,240,'jb1.png')#200x200
mount = Sprite(0,400,'fff1.png')
hero = Sprite(-4,549,'as1d2.png')#110x137
hero.go_right = True
hero.go_down = True

zet.go_right = True
zet.go_down = True


minutes = 0
seconds = 0.0
microsseconds = 0.0

firstround = False
secondround = False
thirdround = False
fourthround = False


speed = 0
#resx = open('resultX.txt', 'r+')
#resy = open('resultY.txt', 'r+')
resx =open('resultX.txt')
resy =open('resultY.txt')
with open('resultX.txt') as file:
    lst = list()
    for line in file.readlines():
        lst.extend(line.rstrip().split(','))
result = [int(item) for item in lst]
print len(result)
file.close()
print "\n"

with open('resultY.txt') as fileY:
    lst1 = list()
    for lineY in fileY.readlines():
        lst1.extend(lineY.rstrip().split(','))
resultY = [int(itemY) for itemY in lst1]
print len(resultY)
fileY.close()
scor = 0
r1 = 0
r2 =0
r3 =0
r4 =0

# main cicle
done = True
while done:
    for e in pygame.event.get():
        if e.type == pygame.QUIT or hero.x>1280:
            done = False
    textsurface = myfont.render(time, False, (0, 0, 0))
    strscor = "Score: "+str(scor)
    textsurface1 = myfont.render(strscor,False,(255,0,0))
    if hero.x<309:
        speed = 1
    if hero.x >=367 and hero.x<501:
        speed = 1
    if hero.x>=501 and hero.x<647 and IsJump == False:
        speed = 2
    if hero.x >=657 and hero.x <997:
        speed = 1
    if hero.x >=997 and hero.x <=1280 and IsJump == False:
        speed = 2
    if Connect(zet.x,hero.x,zet.y,hero.y) == True:
        firstround = True
    if Connect(zet1.x,hero.x,zet1.y,hero.y) == True:
        secondround = True
    if Connect(zet2.x,hero.x,zet2.y,hero.y) == True:
        thirdround = True
    if Connect(zet3.x,hero.x,zet3.y,hero.y) == True:
        fourthround = True
    time = mytimer().replace(".0","")
    if e.type == pygame.KEYDOWN:
        if e.key == pygame.K_RIGHT:
            if hero.x < 1289:
                incrementX +=speed
                hero.x =result[incrementX]
                if IsJump == False:
                    hero.y =resultY[incrementX]
        if e.key == pygame.K_UP:
            IsJump = True
    if IsJump == True:
        if JumpCount >= -15:
            hero.y -= JumpCount * 2
            JumpCount -= 1
        else:
            IsJump = False
            hero.y = resultY[incrementX]
            JumpCount = 15
    screen.fill((50,70,50))
    if firstround == False:
        zet.render()
    else:
        r1 = 1
    if secondround ==False:
        zet1.render()
    else:
        r2 =1
    if thirdround == False:
        zet2.render()
    else:
        r3 = 1
    if fourthround == False:
        zet3.render()
    else:
        r4 = 1
    hero.render()
    mount.render()
    window.blit(screen,(0,0))
    window.blit(textsurface,(0,0))
    window.blit(textsurface1,(1150,0))
    clock.tick(60)
    scor = r1+r2+r3+r4

    print "\n X:      Y: \n"
    print str(hero.x) + "_______" + str(hero.y)
    pygame.display.update()
#    if len(res_x)>0:
#        f = len(res_x) -1
#        if(hero.x != res_x[f]):
#            res_x.append(hero.x)
#            res_y.append(hero.y)
    if(hero.x > 1280):
        break
#print "\n X: \n"
#print res_x
#print "\n Y: \n "
#print res_y
#print "\n"
#print len(res_x)
#print "\n"
#print len(res_y)
#resx.seek(0)
#resy.seek(0)
#resx.write(str(res_x))
#resy.write(str(res_y))
