s1="manjit"
s2="nij"
i=0
j=0
result=None
print(len(s1)-1)
while(j<len(s1)):
    if(s1[i]==s2[j]):
        i=i+1
        j=j+1
        result=True
    if(i==len(s1)):
        print("F")
        result=False
        break
    else:
        j = j + 1
print(result)