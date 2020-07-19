from collections import Counter,OrderedDict
from collections import OrderedDict
from operator import itemgetter
# class Car :
#     def __init__(self, color, speed):
#         self.color = color
#         self.speed = speed
#
# sppedcar=Car('red','100mph')
# print(sppedcar.speed)



# class a:
#     def instance(self):
#         print('Hello')
#     @staticmethod
#     def staticMethod():
#         print('STatic Method')
#     def classMethod(cls):
#         print('Class Method')
#
# obj=a()
#
# obj.classMethod()


# dict={'name':'Manjit','roll':'roll2018'}
#
# x=int(input())
# l=[]
# for i in range(0,x):
#     ele=(input())
#     l.append(ele)
# x=Counter(l)
# print(len(x))
# print(*x.values())
#
# no=[4 ,3 ,2 ,1 ,3, 4]
# l=len(no)-1
# x=False
#
# sideLength=[]
# from collections import deque
# for _ in (range(int(input()))):
#     input()
#     sideLength = deque(map(int, input().strip().split()))
#     for i in range(0, int(len(sideLength) / 2)):
#         if sideLength[i] >= sideLength[l]:
#             x = True
#         else:
#             x = False
#         l = l - 1
#     if x is True:
#         print('Yes')
#     else:
#         print('No')
#
#

# s='qwertyuiopasdfghjklzxcvbnm'
# newDict={}
# x=Counter(list(s))
# print(x.most_common(3))
# for k,v in x.items():
#     if v!=1:
#         newDict[k]=v
#     else:
#         newDict[k]=v
#
#
# # {k:v for k,v in sorted(newDict.items(),key=lambda item:item[1])}
# a=OrderedDict(sorted(newDict.items(),key=itemgetter(1),reverse=True))
#
# print(a)
# for k,v in a.items():
#     print(k,v)
#
#
# input = 'qwertyuiopasdfghjklzxcvbnm'
# c=Counter(sorted(list(input)))
# k = c.most_common(3)
# OrderedDict()
# for (a,b) in k:
#     print(a,b)
# class OrderedCounter(Counter, OrderedDict):
#     pass
# [print(*c) for c in OrderedCounter(sorted(input)).most_common(3)]

x=(1,2,3,4)
x[3]=4


{
    []:[]
}