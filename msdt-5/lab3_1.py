import pytest
import time
import math
import numpy


def revers(s):
    trt=''
    for i in range(len(s)-1,-1,-1):
        trt+=s[i]
    return trt
#n^2


def fastrev(s):
    return fastrevers(s,0,len(s))
def fastrevers(s,i,e):
    if(e-i>=4):
        return (fastrevers(s,i+(e-i)//2*2,e)+
                fastrevers(s,i+(e-i)//2,i+(e-i)//2*2)+
                fastrevers(s,i,i+(e-i)//2))
    elif (e-i==3):
        return s[i+2]+s[i+1]+s[i]
    elif (e-i==2):
        return s[i+1]+s[i]
    elif (e-i==1):
        return s[i]
    else:
        return ''
#nlog(n)?


def lolrev(s):
    l=[]
    for i in range(len(s)):
        l.append(s[-1-i])
    return ''.join(l)
#n

razm = 600000
q=time.time()
revers('i want aboba'*razm)
print(revers('i want aboba'))
print(time.time()-q)
q=time.time()
fastrev('i want aboba'*razm)
print(fastrev('i want aboba'))
print(time.time() - q)