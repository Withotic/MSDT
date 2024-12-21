import pytest
from random import random
def randList(length,pn=None):
    trt = Node(int(random()*10))
    trt.preNode = pn
    if length>0:
        trt.nextNode = randList(length-1,trt)
    return trt
class Node:
    data = None
    preNode = None
    nextNode = None
    def __init__(self,data=0,preNode=None,nextNode=None):
        self.preNode=preNode
        self.nextNode=nextNode
        self.data=data
    def __str__(self):
        return '['+self.strRec()
    def strRec(self):
        if self.nextNode:
            return str(self.data)+' '+self.nextNode.strRec()
        return str(self.data)+']'

    def delRepeat(self,data=None):#----------------------o( D(f1,f2,f3) )
        if data!=None:                                                  #
            if data==self.data:#----------------o( D(s1,s2) )           #
                if self.nextNode:                           #           #
                    self.preNode.nextNode = self.nextNode   #           #
                    self.nextNode.preNode = self.preNode    #           #
                else:                                       #           #
                    self.preNode.nextNode=None              #           #
                #s1=o(1)                                    #           #
            if self.nextNode:                               #           #
                self.nextNode.delRepeat(data)#s2=o(n)       #           #
            #-----------------------------------------f1=o(n)           #
        else:                                                           #
            if self.nextNode:                                           #
                self.nextNode.delRepeat(self.data)#f2=o(n)              #
            if self.nextNode:                                           #
                self.nextNode.delRepeat()#f3=o(n^2)                     #
    #------------------------------------------итоговая сложность: o(n^2)
q=randList(10)
print(q)
q.delRepeat()
print(q)