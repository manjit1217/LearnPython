def bubbleSort(numbers):
    for j in range(0,len(numbers)-1):
        for i in range(0,len(numbers)-1):
            if(numbers[i]>numbers[i+1]):
                numbers[i],numbers[i+1]=numbers[i+1],numbers[i]

    print(numbers)


numbers=[5,6,3,4,5,2,1]
bubbleSort(numbers)