import pytest
q=[[1,1,1,1,1,0],
   [1,0,1,1,1,1],
   [1,1,1,1,1,1],
   [1,1,1,0,1,1],
   [1,0,1,1,1,1],
   [1,1,1,1,1,1],]
m=[]
for i in q:
    m.append(i.copy())

hor=[0]*len(q)
ver=[0]*len(q[0])
for y in range(len(q)):
    for x in range(len(q[0])):
        if q[x][y]==0:
            if hor[x]==0:
                hor[x]=1
                for yk in range(len(q)):
                    m[x][yk]=0
            if ver[y]==0:
                ver[y]=1
                for xk in range(len(q[0])):
                    m[xk][y]=0
for i in m:
    print(i)
#при размере массива n^2:
#память: 2n
#время: O(n^3)