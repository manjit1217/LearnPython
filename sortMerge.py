#this i
#this function will give the sum of two sorted array.
def merge(arr,arr1):
    empty=[]
    i=0
    j=0

    while(i < len(arr) and j<len(arr1)):
            if arr[i]<arr1[j]:
                empty.append(arr[i])
                arr.remove(arr[i])
            else:
                print('else')
                empty.append(arr1[j])
                arr1.remove(arr1[j])
    return (empty+arr+arr1)
    #
    # for i in range(0,len(arr)):
    #     for j in range(i,len(arr1)):
    #         if arr[i]<arr1[j]:
    #             empty.append(arr[i])
    #             i=i+1
    #         else:
    #             empty.append(arr1[j])
    #             j=j+1

#here we will devide the full array to single element by doing recurssion, then send that value to merge
def mergeSort(arr):
    length=len(arr)
    if len(arr)==1:return arr
    mid=length/2
    left=(arr[0:int(mid)])
    right=arr[int(mid):length]
    left = mergeSort(left)
    right = mergeSort(right)
    # if len(left)>=2 and len(right)>=2:
    #     left=mergeSort(left)
    #     right=mergeSort(right)
    return merge(left,right)


arr=[5,6,7,8,1]
print(mergeSort(arr))


