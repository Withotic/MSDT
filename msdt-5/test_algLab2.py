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
    return len(m)==0

def test_krugskobs_true():
    assert krugskobs("gkja (asd) fas(df)asdf(ff(dd+fd)sdf)")==True
    assert krugskobs("( (q) (b) (t) )    (=(-)(=-)2)")==True

def test_krugskobs_false():
    assert krugskobs(":))))))))")==False
    assert krugskobs("(()()))")==False
    assert krugskobs("SD()B<S()<>(BSD)))0dlsf0ls()())))")==False

def test_skobs_true():
    assert skobs("[{aja+(qq)}-mojojoq](dd)")==True
    assert skobs("[++(-- )234{52}]  {[]{}({})} sdf ([]{})")==True

def test_skobs_false():
    assert skobs("{}()[")==False
    assert skobs("{})[](")==False
    assert skobs("}jkl()")==False
    assert skobs("[{]}")==False