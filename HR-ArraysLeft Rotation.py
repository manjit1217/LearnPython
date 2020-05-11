arr=[1,2,3,4,5]
noOfTimes=2
print(arr[4])

def array_left_rotation(a, n, k):
    alist = list(a)
    b = alist[k:]+alist[:k]
    print(b)

array_left_rotation(arr,len(arr),4)

# def rotLeft(a,d):
#     for i in range(0,d):
#         x=a[0]
#         for j in range(0,len(a)-1):
#             a[j]=a[j+1]
#         a[len(a)-1]=x
#     print(a)

