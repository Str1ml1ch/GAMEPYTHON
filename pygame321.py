import pygame, sys
from pygame.locals import *

window = pygame.display.set_mode((1400,700))
pygame.display.set_caption(('Snowboarder GO!!!'))
screen = pygame.Surface((1400,700))
pygame.display.set_icon(pygame.image.load("asd.png"))
clock = pygame.time.Clock()
pygame.mouse.set_visible(False)

class Sprite:
    def __init__(self,xpos,ypos,filename):
        self.x = xpos
        self.y = ypos
        self.bitmap = pygame.image.load(filename)
        self.bitmap.set_colorkey((0,0,0))
    def render(self):
        screen.blit(self.bitmap,(self.x,self.y))

def Connect(x1,x2,y1,y2):
    if(x1 > x2-50) and (x1 < x2+50) and (y1>y2 -150) and (y1 < y2+150):
        return 1
    else:
        return 0
hero = Sprite(0,503,'asd.png')#255x197
zet = Sprite(0,0,'jb.png')#200x200

hero.go_right = True
hero.go_down = True

zet.go_right = True
zet.go_down = True



# main cicle
done = True
while done:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            done = False

    if Connect(zet.x,hero.x,zet.y,hero.y) == True:
        print "HELLO"
    else:
        print "BYBYBY"
    if e.type == pygame.KEYDOWN:
        if e.key == pygame.K_RIGHT:
            if hero.x < 1200:
                hero.x +=3
        if e.key == pygame.K_LEFT:
            if hero.x >0:
                hero.x -=3
        if e.key == pygame.K_UP:
            if hero.y >0:
                hero.y -=3
        if e.key == pygame.K_DOWN:
            if hero.y <503:
                hero.y +=3
    screen.fill((50,70,50))
    hero.render()
    zet.render()
    window.blit(screen,(0,0))
    pygame.display.flip()
    clock.tick(60)
