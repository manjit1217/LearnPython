import itertools
import operator
import math



# a=[4,5,6]
# b=[7,8,9]
#
#
# x=itertools.permutations(perm,len(perm))
#
# y=list(x)
# print(y)
#
# def check_list(n,diff):
#     perm = [i for i in range(1, n+1)]
#     x = itertools.permutations(perm, len(perm))
#     y = list(x)
#     for i in y:
#         list_no=((list(map(operator.sub,list(i),perm))))
#         x=[abs(a) for a in list_no]
#         if(len(list(set(x)))==1 and list(set(x))[0]==diff) :
#             # if (len(x) == len(perm)):
#                  print(list(i))
#     else:
#         print(-1)


        # print(list_no)

        # print(x)
        # if len(x)==len(perm):
        #     print(x)


#
#
# check_list(3,0)



from itertools import permutations

def absolutePermutation(n, k):
    if k ==0:
        print(*(range(1,n+1)))
    elif (n/k)%2 != 0.0:
        print(-1)
    else:
        perm = [i for i in range(1, n + 1)]
        x = itertools.permutations(perm, len(perm))
        y = list(x)
        for i in y:
            list_no = ((list(map(operator.sub, list(i), perm))))
            x = [abs(a) for a in list_no]
            if (len(list(set(x))) == 1 and list(set(x))[0] == k):
                a=list(i)
                return (' '.join(str(e) for e in a))

for _ in range(int(input())):
    n,k = map(int,input().split())
    absolutePermutation(n, k)

