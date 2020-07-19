import pytest


def febo(n):
    l=[]
    n1,n2=0,1
    c=0
    if n <=0:
        print('not a positive')
    elif n ==1:
        print(n1)
    else:
        while c<n:
            l.append(n1)
            nth=n1+n2
            n1=n2
            n2=nth
            c=c+1
    return l

print(febo(5))
