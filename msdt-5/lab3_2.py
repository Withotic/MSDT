import pytest
#3_3

ss=input()
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

print(trt)

res=""
for i in range(len(trt)//2):
    res+=trt[i*2]*int(trt[i*2+1])
print(res)