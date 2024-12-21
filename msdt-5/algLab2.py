import pytest
def krugskobs(s):
    k = 0
    for q in s:
        if q == '(':
            k += 1
        elif q == ')':
            k -= 1
    assert k==0
    if k==0: return 'скобки расставленны правильно'
    else: return 'скобки расставленны НЕПРАВИЛЬНО'

def skobs(s):
    m=[]
    for q in s:
        if q=='(':
            m.append(0)
        elif q=='{':
            m.append(1)
        elif q=='[':
            m.append(2)
        elif q==')':
            if not(m) or m.pop()!=0:
                return 'скобки расставленны НЕПРАВИЛЬНО'
        elif q == '}':
            if not(m) or m.pop() != 1:
                return 'скобки расставленны НЕПРАВИЛЬНО'
        elif q == ']':
            if not(m) or m.pop() != 2:
                return 'скобки расставленны НЕПРАВИЛЬНО'
    return 'скобки расставленны правильно'
s=input()
while s!='':
    print(krugskobs(list(s)))
    s=input()
while s!='':
    print(skobs(list(s)))
    s=input()