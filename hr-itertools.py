import itertools
import random
def check_itertools():
    n=input()
    l=[str(i) for i in input().split()]
    r=int(input())
    a_count=0
    iter_result=list(itertools.combinations(l,r))
    for i in iter_result:
        if(('a') in i):
            a_count+=1
    print('%.4f'%(a_count/len(iter_result)))

# l=[2,5,4]
# l1=[1,4,5]
# l2=[1,5,2]
# print(list(itertools.product(*(l,l1,l2))))
N = (list(map(int, input().split()))[1:] for _ in range(3))
print(N)
from itertools import product

K,M = map(int,input().split())
N = (list(map(int, input().split()))[1:] for _ in range(K))
results = map(lambda x: sum(i**2 for i in x)%M, product(*N))
print(max(results))

k,m=map(int,input().split())
for i in range(k):
    l1=[int(i) for i in input().split()]
    x=itertools.combinations(l1,1)
    print(x)

print(l1)
