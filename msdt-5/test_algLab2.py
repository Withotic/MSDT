import pytest

#проверяет правильно ли расставленны круглые скобки
def krugskobs(s):
    k = 0
    for q in s:
        if q == '(':
            k += 1
        elif q == ')':
            k -= 1
    return k==0

#проверяет ([{}]) скобки + случаи [{]}
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
                return False
        elif q == '}':
            if not(m) or m.pop() != 1:
                return False
        elif q == ']':
            if not(m) or m.pop() != 2:
                return False
    return True

def test_krugskobs():
    assert krugskobs("gkja (asd) fas(df)asdf(ff(dd+fd)sdf)")==True
    assert krugskobs(":))))))))")==False
    assert krugskobs("(()()))")==False

def test_skobs():
    assert skobs("[{aja+(qq)}-mojojoq](dd)")==True
    assert skobs("{}()[")==False
    assert skobs("{})[](")==False
    assert skobs("}jkl()")==False
    assert skobs("[{]}")==False

