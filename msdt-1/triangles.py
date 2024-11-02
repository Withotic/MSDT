import pygame
import pandas

dots=[]
lines=[]
side=90
clock = pygame.time.Clock()
mousepos=(0,0)
def dotsgen():
    for y in range(13):
        for x in range(25):
            dots.append((int(x*side*(3**0.5)/2),y*side+(x%2==0)*side//2))
def dotsdraw():
    for dot in dots:
        pygame.draw.circle(screen,(200,0,0),dot,10)
def linesdraw():
    for line in lines:
        pygame.draw.line(screen, (100, 100, 100), line[0], line[1], 5)
def rast(d1,d2):
    return ((d1[0]-d2[0])**2+(d1[1]-d2[1])**2)**0.5
def corrpos(pos,begpos):
    mindot=dots[0]
    minrast=rast(pos,dots[0])
    for dot in dots:
        if rast(pos,dot)<minrast:
            mindot=dot
            minrast=rast(pos,dot)
    return mindot
def corrpos(pos):
    mindot=dots[0]
    minrast=rast(pos,dots[0])
    for dot in dots:
        if rast(pos,dot)<minrast:
            mindot=dot
            minrast=rast(pos,dot)
    return mindot
def linedotrast(dot,line):
    a=rast(dot,line[0])
    b=rast(dot,line[1])
    c=rast(line[0],line[1])
    h=(((a+b+c)*(a+b-c)*(a-b+c)*(-a+b+c))**0.5/4)*2//c
    am = (a ** 2 - h ** 2) ** 0.5
    bm = (b ** 2 - h ** 2) ** 0.5
    if am<=c and bm<=c:
        return h
    else:
        return min(am,bm)
def minlinerastdel(pos):
    minrast=999999
    minline=None
    for line in lines:
        if not(minline) or minrast>linedotrast(pos,line):
            minline=line
            minrast=linedotrast(pos,line)
    if minline:
        lines.remove(minline)

pygame.init()
dotsgen()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
dot1=(0,0)
dot2=None
drag=False


while True:
    screen.fill((200,200,200))
    for event in pygame.event.get():
        if event.type == pygame.QUIT: exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button==1:
                drag=True
                dot1 = corrpos(event.pos)
                dot2 = None
            if event.button==3:
                minlinerastdel(event.pos)
        if drag:
            mousepos = corrpos(event.pos)
        if event.type == pygame.MOUSEBUTTONUP and event.button==1:
            drag = False
            if dot1!=corrpos(mousepos) and (dot1,mousepos) not in lines:
                lines.append((dot1,mousepos))
    if drag:
        pygame.draw.line(screen, (100, 100, 100), dot1, mousepos, 5)
    linesdraw()
    dotsdraw()
    pygame.display.flip()
    clock.tick(60)

