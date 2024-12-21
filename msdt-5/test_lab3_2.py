import pytest
#3_3

def shifr(ss):
    trt=""
    pc=ss[0]
    k=0
    for c in ss:
        if c==pc:
            k+=1
        else:
            trt+=pc+str(k)
            k=1
            pc=c
    trt+=pc+str(k)
    return trt

def deshifr(trt):
    res=""
    for i in range(len(trt)//2):
        res+=trt[i*2]*int(trt[i*2+1])
    return res

def test_q():
    assert shifr("gkass")=="g1k1a1s2"

ss = input()
q = shifr(ss)
print(q)
print(deshifr(q))