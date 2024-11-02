import pygame as pg


screen = pg.display.set_mode((800, 800))
playerpos = (30, 30)
playerrad = 20
playerspeed = 10
lines = []
bld = None  #buildlinedot
isdebug = False


#-----------------------------------------------------------------------------------------------------EVENTSHANDLE(done)
def eventshandle():
    global playerpos, bld, lines, isdebug
    keys = pg.key.get_pressed()
    dx = 0
    dy = 0
    if keys[pg.K_UP]:dy -= 1
    if keys[pg.K_DOWN]:dy += 1
    if keys[pg.K_LEFT]:dx -= 1
    if keys[pg.K_RIGHT]:dx += 1
    if dx!=0 and dy!=0:
        playerpos = (playerpos[0] + playerspeed*dx/(2**0.5), playerpos[1] + playerspeed*dy/(2**0.5))
    else:
        playerpos = (playerpos[0] + playerspeed*dx, playerpos[1] + playerspeed*dy)
    for i in pg.event.get():
        if i.type == pg.QUIT:exit()
        elif i.type == pg.KEYDOWN:
            if i.key == pg.K_e:
                if not (bld):
                    bld = playerpos
                elif bld:
                    lines.append((bld, playerpos))
                    if not isdebug: playerpos = (playerpos[0] + playerrad, playerpos[1] + playerrad)
                    bld = None
            if i.key == pg.K_r:
                bld = None
            if i.key == pg.K_k:
                lines = []
            if i.key == pg.K_c:isdebug=not isdebug
            if i.key == pg.K_q:exit()


#--------------------------------------------------------------------------------------------------COLLISION(almostdone)
def linelen(line):
    return ( (line[0][0]-line[1][0])**2 + (line[0][1]-line[1][1])**2 ) ** 0.5


def setlinelen(line, len, multiply):
    if linelen(line) > 0:
        if multiply:
            return (line[0], (line[0][0] + (line[1][0]-line[0][0])*len, line[0][1] + (line[1][1]-line[0][1])*len))
        else:
            return (line[0], (line[0][0] + (line[1][0]-line[0][0])*len / linelen(line), line[0][1] + (line[1][1] - line[0][1]) * len / linelen(line)))
    else:
        return line


def dagtoline(line):
    global playerpos
    a = linelen((line[0], playerpos))
    b = linelen((line[1], playerpos))
    c = linelen(line)
    if c==0: return (line[0], playerpos)
    h = abs( (a+b+c) * (a+b-c) * (a-b+c) * (-a+b+c) ) ** 0.5 / 2 / c
    am = (abs(a**2 - h**2)) ** 0.5
    bm = (abs(b**2 - h**2)) ** 0.5
    if am<=c and bm<=c:
        return ((playerpos[0] + h * (line[1][1]-line[0][1]) / c, playerpos[1] + h * (line[0][0]-line[1][0]) / c), playerpos)
    else:
        if linelen((line[0], playerpos)) == min(linelen((line[0], playerpos)), linelen((line[1], playerpos))):
            return (line[0], playerpos)
        else:
            return (line[1], playerpos)


def collision():
    global playerpos, playerrad
    scr = pg.display.get_window_size()
    if playerpos[0] - playerrad < 0: playerpos = (playerrad, playerpos[1])
    if playerpos[1] - playerrad < 0: playerpos = (playerpos[0], playerrad)
    if playerpos[0] + playerrad > scr[0]: playerpos = (scr[0] - playerrad, playerpos[1])
    if playerpos[1] + playerrad > scr[1]: playerpos = (playerpos[0], scr[1] - playerrad)

    for line in lines:
        dagline = dagtoline(line)
        if(linelen(dagline) < playerrad):
            playerpos = setlinelen(dagline, playerrad, False)[1]
#------------------------------------------------------------------------------------------------------RENDER(linesplit)


def drawwall(line):
    pg.draw.line(screen, (255, 255, 255), line[0], line[1])
    pg.draw.line(screen, (255, 0, 0), line[0], setlinelen((line[0], (line[0][0] + (line[1][1]-line[0][1]), line[0][1] + (line[0][0]-line[1][0]))), 10, False)[1])
    pg.draw.line(screen, (255, 0, 0), line[1], setlinelen((line[1], (line[1][0] + (line[1][1]-line[0][1]), line[1][1] + (line[0][0]-line[1][0]))), 10, False)[1])


def sign(n):
    if n < 0:return -1
    if n == 0:return 0
    return 1


def dotintriag(a, b, c, D):
    z1 = sign((a[0]-D[0]) * (b[1]-a[1]) - (b[0]-a[0]) * (a[1]-D[1]))
    z2 = sign((b[0]-D[0]) * (c[1]-b[1]) - (c[0]-b[0]) * (b[1]-D[1]))
    z3 = sign((c[0]-D[0]) * (a[1]-c[1]) - (a[0]-c[0]) * (c[1]-D[1]))
    return z1==z2 and z2==z3 and z1!=0


def dotonline(d, l):
    if l[0][0] == l[1][0]:
        return ((l[0][1]<=d[1] and d[1]<=l[1][1]) or (l[0][1]>=d[1] and d[1]>=l[1][1])) and (linelen((l[0], d))+linelen((l[1], d)) < linelen(l)*1.001)
    if l[0][1] == l[1][1]:
        return ((l[0][0]<=d[0] and d[0]<=l[1][0]) or (l[0][0]>=d[0] and d[0]>=l[1][0])) and (linelen((l[0], d))+linelen((l[1], d)) < linelen(l)*1.001)
    return ((l[0][0]<=d[0] and d[0]<=l[1][0]) or (l[0][0]>=d[0] and d[0]>=l[1][0])) and\
           ((l[0][1]<=d[1] and d[1]<=l[1][1]) or (l[0][1]>=d[1] and d[1]>=l[1][1]))


def linecross(l1, l2):
    A = l1[1][0] - l1[0][0]
    B = l2[1][0] - l2[0][0]
    C = l1[1][1] - l1[0][1]
    D = l2[1][1] - l2[0][1]
    if (A*D - C*B) == 0: return None
    q = ( C*(l2[0][0]-l1[0][0]) - A*(l2[0][1]-l1[0][1]) ) / (A*D - C*B)
    d = (l2[0][0] + B*q, l2[0][1] + D*q)
    return (d, dotonline(d, l1), dotonline(d, l2))


def fullblock(dl, bl):
    global playerpos
    n1 = linecross((playerpos, dl[0]), bl)
    n2 = linecross((playerpos, dl[1]), bl)
    n3 = linecross(dl, bl)
    return n1 and n2 and n1[1] and n1[2] and n2[1] and n2[2]


def doubsplit(l, d1, d2):
    a = linelen((l[0], d1))
    b = linelen((l[0], d2))
    if a == b:
        return [l]
    if a < b:
        return [(l[0], d1), (d2, l[1])]
    else:
        return [(l[0], d2), (d1, l[1])]


def partblock(dl, bl):
    global playerpos
    if (dotintriag(playerpos, dl[0], dl[1], bl[0]) and dotintriag(playerpos, dl[0], dl[1], bl[1])):
        print('hi')
        return doubsplit(dl, linecross(dl, (playerpos, bl[0]))[0], linecross(dl, (playerpos, bl[1]))[0])
    if (linecross((playerpos, dl[0]), bl) and linecross((playerpos, dl[0]), bl)[1] and linecross((playerpos, dl[0]), bl)[2]):
        print('hi1')
        if dotintriag(playerpos, dl[0], dl[1], bl[0]):
            return [(linecross((playerpos, bl[0]), dl)[0], dl[1])]
        else:
            return [(linecross((playerpos, bl[1]), dl)[0], dl[1])]
    if (linecross((playerpos, dl[1]), bl) and linecross((playerpos, dl[1]), bl)[1] and linecross((playerpos, dl[1]), bl)[2]):
        print('hi2')
        if dotintriag(playerpos, dl[0], dl[1], bl[0]):
            return [(linecross((playerpos, bl[0]), dl)[0], dl[0])]
        else:
            return [(linecross((playerpos, bl[1]), dl)[0], dl[0])]
    return None


def fullvis(dl, bl):
    global playerpos
    n1 = linecross((playerpos, dl[0]), bl)
    n2 = linecross((playerpos, dl[1]), bl)
    n3 = linecross(dl, bl)
    return (not(n3) or (not(n3[1]) and not(n3[2]))) and (not(n2) or (not(n2[1]) and not(n2[2]))) and (not(n1) or (not(n1[1]) and not(n1[2]))) and not(dotintriag(playerpos, dl[0], dl[1], bl[0])) and not(dotintriag(playerpos, dl[0], dl[1], bl[1]))


def splitisline():#должен вернуть массив из разрезанной стены
    global playerpos,lines
    dls = lines.copy()
    i = 0
    while i < len(dls):
        bls = dls.copy()
        bls.remove(dls[i])
        while len(bls) > 0:
            if fullblock(dls[i], bls[0]):
                dls.pop(i)
                i -= 1
                bls.pop(0)
                break
            pb = partblock(dls[i], bls[0])
            if pb:
                dls.pop(i)
                dls += pb
            bls.pop(0)
        i += 1
    return dls


def render():
    if bld:
        drawwall((bld, playerpos))
    if isdebug:
        for line in lines:
            drawwall(line)
    else:
        for line in splitisline():
            pg.draw.line(screen, (255, 255, 255), line[0], line[1])


#-------------------------------------------------------------------------------------------------------------MAIN(done)
clock = pg.time.Clock()
pg.init()
while True:
    screen.fill((0, 0, 0))
    eventshandle()
    if not isdebug: collision()
    render()
    pg.draw.circle(screen, (255, 255, 255), playerpos, playerrad)
    pg.display.flip()
    clock.tick(60)
    pg.display.set_caption(f'FPS: {clock.get_fps() :.2f}')
