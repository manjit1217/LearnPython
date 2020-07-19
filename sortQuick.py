def helper(numbers,h,l):
    pivotLast=numbers[h]
    i=l
    for j in range(l,h):
        if(numbers[j]<=pivotLast):
            numbers[i],numbers[j]=numbers[j],numbers[i]
            i=i+1
    numbers[i],numbers[h]=numbers[h],numbers[i]
    print(numbers,i)
    return i

def quickSort(numbers,h,l):
    if l<h:
        x=helper(numbers,h,l)
        left = helper(numbers,x-1,l)
        right = helper(numbers,h,x+1)
    print(numbers)













numbers=[1,5,7,9,10,14,16]
print(quickSort(numbers,len(numbers)-1,0))
