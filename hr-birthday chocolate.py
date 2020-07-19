s=[4]
def birthday(s, d, m):
    count=0
    for i in range(0,len(s)):
        if sum(s[i:m+i])==d:
            count=count+1
    print(count)


birthday(s,4,1)