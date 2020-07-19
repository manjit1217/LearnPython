# def bubble_sort(l):
#     for i in range(0,len(l)):
#         for j in range(i,len(l)):
#             if l[i]>l[j]:
#                 l[i], l[j] = l[j], l[i]
#     print(l)

# In bubble sort first we will compare the consicutive element, in the first loop we will get the
# heighest no that will be placed in the last of the list..

def bubble_sort(l):
    while True:
        swap=False
        for i in range(0,len(l)-1):
            if l[i]>l[i+1]:
                l[i],l[i+1]=l[i+1],l[i]
                swap=True
        if not swap:
            break
        print (l)




l=[3,38,5,44,47,15,36,26,27,2,46,4,19]
print(bubble_sort(l))