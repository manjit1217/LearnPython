list = [0, 2, 3, 5, 8,9]

key=0

def binarySearch(list,key):
    high=len(list)-1
    low=0

    got=False
    while(low<=high  and not got):
        mid = (high + low) // 2
        if (list[mid]==key):
            got=True
        elif(list[mid]<key):
            low=mid+1
        else:high=mid-1
    if(got==True):
        print("Found")
    else:
        print("Not Found")


binarySearch(list,key)