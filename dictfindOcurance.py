from collections import Counter
s="aaabbccd"
print(Counter(s))
n = {  }

for i in s:
    if i in n:
        n[i]+=1
    else:
        n[i]=1



print(n)
