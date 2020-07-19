def bubbleSort(numbers):
    for j in range(0,len(numbers)-1):
        for i in range(0,len(numbers)-1):
            if(numbers[i]>numbers[i+1]):
                numbers[i],numbers[i+1]=numbers[i+1],numbers[i]

    print(numbers)





# numbers=[5,6,3,4,5,2,1]
# bubbleSort(numbers)
#




a=[1,2,4,53,2,3]
def bubbleSort(a):
    count = 0
    for i in range(0, len(a)):
        for j in range(i+1,len(a)):
            if a[i] > a[j]:
                a[i], a[j] = a[j], a[i]
                count += 1
    print(a,count)
bubbleSort(a)








