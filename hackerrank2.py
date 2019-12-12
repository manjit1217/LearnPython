no=[2,3,1,1,1,3,5,4,3]
nocopy=no.copy()
del(nocopy[0])
print(no,nocopy)

for i in range(0,len(no)-1):
    nocopy = no.copy()
    del(nocopy[i],nocopy[i])
    for j in range(0, len(nocopy)):
        if (no[i] * no[i + 1] * nocopy[j]) == 15:
            print(no[i],no[i+1],nocopy[j])

