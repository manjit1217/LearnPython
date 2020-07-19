
def binary(n):
    bin=[]
    reminder=None
    q=n
    while q>1:
        n=q
        q = int(n / 2)
        reminder = n % 2
        bin.append(reminder)
        if q == 1:
            bin.append(q)
    else:

        count=0
        big=0
        x=(''.join(map(str,bin[::-1])))
        print(x)
        rev=bin[::-1]
        for i in range(0,len(bin)):

            if(rev[i]==1):
                count+=1
                if (count > big):
                    big = count
            else:
                count=0
        print(1,big)


binary(13)

n = int(input().strip())
binary = []
while n > 0:
    remainder = n%2
    binary.append(remainder)
    n = n//2
print(binary)