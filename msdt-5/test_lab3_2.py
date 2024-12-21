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

def test_shifr():
    assert shifr("gkass")=="g1k1a1s2"
    assert shifr("oaisjdopflll  2009039^(03209)"+\
                 "((356))foi++-12-==-0==12=-@####p25")==\
                "o1a1i1s1j1d1o1p1f1l3 2210291013191^1(10"+\
                "131210191)1(2315161)2f1o1i1+2-11121-1=2-1"+\
                "01=21121=1-1@1#4p12151"
    assert shifr("HHHHHHHyyyyyyyyyBBBBBBB")=="H7y9B7"
    

def test_deshifr():
    assert deshifr("g1k1a1s2")=="gkass"
    assert deshifr("o1a1i1s1j1d1o1p1f1l3 2210291013191^1(10"+\
                "131210191)1(2315161)2f1o1i1+2-11121-1=2-1"+\
                "01=21121=1-1@1#4p12151")=="oaisjdopflll  2009039^(03209)"+\
                 "((356))foi++-12-==-0==12=-@####p25"
    assert deshifr("H7y9B7")=="HHHHHHHyyyyyyyyyBBBBBBB"