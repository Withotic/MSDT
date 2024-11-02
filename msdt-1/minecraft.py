import anvil
import shutil
import os
import math
import numpy

t=0
x1=16
y1=16
x2=16
y2=16
x3=16
y3=16
def getblock(x,y,z):
    chunk = anvil.Chunk.from_region(region, x//16, z//16)
    block = chunk.get_block(x%16, y, z%16)
    return block.id

def addframe(g,ems):
    global t
    func = open('C:/Users/nikipa/AppData/Roaming/.tlauncher/legacy/Minecraft/game/saves/qs (1)/datapacks/build/data/minecraft/functions/pf' + str(t) + '.mcfunction', "w")
    for q in g:
        func.write('setblock ' + str(q[0]) + ' ' + str(q[1]) + ' ' + str(q[2]) + ' netherrack' + '\n')
    for q in ems:
        func.write('setblock ' + str(q[0]) + ' ' + str(q[1]) + ' ' + str(q[2]) + ' emerald_block' + '\n')
    func.write('schedule function pf'+str(t+1)+' 0.2s')
    t+=1

def bigfunc(x,y,c):
    if c!=2:
        return 0.5<=math.e**(-0.06*((x-x1)**2+(y-y1)**2))+math.e**(-0.06*((x-x2)**2+(y-y2)**2))+math.e**(-0.06*((x-x3)**2+(y-y3)**2))
    else:
        return 0.5<=math.e**(-0.06*((x-x1)**2+(y-y1)**2))+math.e**(-0.06*((x-x2)**2+(y-y2)**2))+math.e**(-0.06*((x-x3)**2+(y-y3)**2))+math.e**(y-24)

def addframe(c):
    global t
    print(t,x1,y1,x2,y2,x3,y3)
    func = open('C:/Users/nikipa/AppData/Roaming/.tlauncher/legacy/Minecraft/game/saves/qs (1)/datapacks/build/data/minecraft/functions/pf' + str(t) + '.mcfunction', "w")
    func.write('fill 0 0 0 63 63 0 '+('white' if c!=2 else 'purple')+'_concrete\n')
    for x in range(64):
        for y in range(64):
            if(bigfunc((x+0.5)/2,(y+0.5)/2,c)):
                func.write('setblock '+str(x)+' '+str(y)+' 0 '+('blue'if c==0 else 'lime' if c==1 else 'white')+'_concrete\n')
    func.write('schedule function pf' + str(t + 1) + ' 1')

def grow():
    global sorces
    global paths
    builded = []
    while len(sorces)>0:
        growcords = []
        for sorce in sorces:
            begx = sorce[0]
            begy = sorce[1]
            begz = sorce[2]
            q = (begx + 1, begy, begz)
            if q not in growcords:
                growcords.append(q)
            q = (begx-1,begy,begz)
            if q not in growcords:
                growcords.append(q)
            q = (begx,begy+1,begz)
            if q not in growcords:
                growcords.append(q)
            q = (begx,begy-1,begz)
            if q not in growcords:
                growcords.append(q)
            q = (begx,begy,begz+1)
            if q not in growcords:
                growcords.append(q)
            q = (begx,begy,begz-1)
            if q not in growcords:
                growcords.append(q)
        print(t,'start',len(paths),len(builded))
        q=[x for x in growcords if x not in paths and x not in builded]
        print(t,'finish')
        addframe(sorces,q)
        builded+=sorces
        sorces=q



region = anvil.Region.from_file('C:/Users/nikipa/AppData/Roaming/.tlauncher/legacy/Minecraft/game/saves/qs (1)/region/r.0.0.mca')
path = 'C:/Users/nikipa/AppData/Roaming/.tlauncher/legacy/Minecraft/game/saves/qs (1)/datapacks/build/data/minecraft/functions/'
shutil.rmtree(path)
os.makedirs(path)
c=0
for t in range(20):
    addframe(c)
for t in range(20*1,20//2*13):
    if t ==20*3:
        c=1
    if t>=20*1 and t<20*2:
        y1=5*(1-math.cos(math.pi*(t/20-1)))+16
    if t>=20*1.5 and t<20*2.5:
        x2=5*(1-math.cos(math.pi*(t/20-1.5)))+16
        y2=-5*(1-math.cos(math.pi*(t/20-1.5)))+16
    if t>=20*2 and t<20*3:
        x3=-5*(1-math.cos(math.pi*(t/20-2)))+16
        y3=-5*(1-math.cos(math.pi*(t/20-2)))+16
    if t>=20*3.5 and t<20*4.5:
        x2 = -5 * (1 - math.cos(math.pi * (t / 20 - 3.5))) + 26
        x3 = 5 * (1 - math.cos(math.pi * (t / 20 - 3.5))) + 6
    if t>=20*4.5 and t<20*5.5:
        y2=5*(1-math.cos(math.pi*(t/20-4.5)))+6
        y3=5*(1-math.cos(math.pi*(t/20-4.5)))+6
    if t>=20*5 and t<20*6:
        y1=-5*(1-math.cos(math.pi*(t/20-5)))+26
    addframe(c)
c=2
boba=2
x1=14+boba
x2=23+boba
x3=5+boba
for t in range(20*6,20*6+20//2*5+1):
    td=(t-20*6)*7/50+1
    y1=32-td**2
    y2=32-(td-1)**2
    y3=32-(td-2)**2
    addframe(c)

#paths = []
#sorces = []
#for xc in range(4):
#    for zc in range(4):
#        chunk = anvil.Chunk.from_region(region, xc, zc)
#        for x in range(16):
#            for z in range(16):
#                for y in range(2,64):
#                    qqqq = chunk.get_block(x, y, z).id
#                    if qqqq == 'glass':
#                        paths.append((x+xc*16,y,z+zc*16))
#                    elif qqqq == 'emerald_block':
#                        sorces.append((x + xc * 16, y, z + zc * 16))