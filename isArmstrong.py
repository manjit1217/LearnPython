import math

def isArmstrong(n):
    sum=0
    length=int(math.log10(n))+1
    temp=n
    while(int(temp)!=0):
        r=int(temp)%10
        sum=sum+r**length
        temp=temp/10
    print( sum==n)

isArmstrong(153)
