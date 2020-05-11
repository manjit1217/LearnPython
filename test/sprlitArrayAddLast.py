#Split the array and add the first part to the end

arr=[12,10,5,6,52,36]
k=2
print(arr[::-1])
# def splitAdd(arr,k):
#     i=0
#     while(i<=k-1):
#         x=arr[0]
#         arr.append(x)
#         arr.remove(arr[0])
#         i+=1
#     print(arr)
# splitAdd(arr,k)


def splitAdd(arr,k):
    for i in range(0,k):
        x=arr[0]
        for j in range(0,len(arr)-1):
            arr[j]=arr[j+1]
        arr[len(arr)-1]=x
    print(arr)

splitAdd(arr,k)