import pytest
from random import random
class stack:
    data=[]
    mins=[]
    def __init__(self,q):
        self.data.append(q)
        self.mins.append(q)
    def __init__(self):
        pass
    def min(self):
        if len(self.mins)>0:
            return self.mins[-1]
        return None
    def push(self,q):
        self.data.append(q)
        if len(self.mins)>0:
            if q<self.mins[-1]:
                self.mins.append(q)
            else:
                self.mins.append(self.mins[-1])
        else:
            self.mins.append(q)
    def pop(self):
        self.data.pop()
        self.mins.pop()

q=stack()
for i in range(10):
    q.push(int(random()*10))
print(q.data)
print(q.mins)