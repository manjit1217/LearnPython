def divisibleSumPairs(n, k, ar):
    count=0
    ar_cpy=ar
    i=0
    for j in range(i,n):
        if (ar[i]+ar[j]) % k == 0:
            count=count+1
            i=i+1
    return (count)

l=[1, 3, 2, 6, 1, 2]
print(divisibleSumPairs(len(l),3,l))


