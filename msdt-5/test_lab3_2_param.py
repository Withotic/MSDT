import pytest
#3_3
@pytest.mark.parametrize("ss", ["gkassb oneqqgo.//3365"])
def test_shifr(ss):
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
    assert trt=="g1k1a1s2b1 1o1n1e1q2g1o1.1/2326151"

def deshifr(trt):
    res=""
    for i in range(len(trt)//2):
        res+=trt[i*2]*int(trt[i*2+1])
    return res

#ss = input()
#q = shifr(ss)
#print(q)
#print(deshifr(q))