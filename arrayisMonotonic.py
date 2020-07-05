
def monotonic(arr):
    im=None
    dm=None
    for i in range(0,len(arr)-1):
        if(arr[i]>arr[i+1]):
            dm=True
        elif(arr[i]<arr[i+1]):
            im=True
    if(im==True or False and  dm==True or False):
        print('Non')
    elif(im==True):
        print('increase')
    elif(dm==True):
        print('decrease')


def monotonic2(arr):
    x=all(arr[i]<=arr[i+1] for i in range(0,len(arr)-1)) or  all(arr[i]>=arr[i+1] for i in range(0,len(arr)-1))
    print( x)



arr=[5,15,20,10]
monotonic2(arr)