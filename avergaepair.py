no=[3,4,6]
avg=5
i=0
j=len(no)-1
result=False
s=0
oc=2

while(i<j):
    s=sum(no[i:i+oc])
    if((s/2)==avg):
        result=True
        break
    elif((no[i]+no[j])>3):
        i=i+1
    else:
        j=j-1

print(result)


