array=[7,10,4,20,15]


# T=input()
# no=int(input())
# #array = [int(x) for x in input().split()]
# k=int(input())
def kthSmallest(array,kth):
    array.sort()
    print(array[kth-1])


kthSmallest(array,4)

