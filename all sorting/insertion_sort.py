def insertion_sort(l):
    sorted=0
    for i in range(1,len(l)):
        value=l[i]
        for j in range(0,i):
            if l[j]>value:
                l[j+1]=l[j]
                l[j]=value
    print( l)

l = [3, 38, 5, 44, 47, 15, 36, 26, 27, 2, 46, 4, 19]
insertion_sort(l)
