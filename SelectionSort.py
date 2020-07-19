unsorted_array=[5,15,3,12,17,0]
sorted_array=[]

# x=[8,9,5,3,4,2,1]
# for i in range(0,len(x)):
#     min=i
#     for j in range(i+1,len(x)):
#         if (x[min]>x[j]):
#             min=j
#
#     x[i],x[min]=x[min],x[i]
#     print(x)


def min(array):
    minval=array[0]
    for i in range(len(array)):
        if(array[i]<minval):
            minval=array[i]
    return minval

def swap(list,i,j):
    list[i],list[j]=list[j],list[i]
    return list

def selectionsort(unsorted):
    for i in range(len(unsorted)):
        min_index = i
        for j in range(i+1,len(unsorted)):
            if(unsorted[min_index]>unsorted[j]):
                min_index=j
            unsorted[i],unsorted[min_index]=unsorted[min_index],unsorted[i]
    return unsorted


print(selectionsort(unsorted_array))

