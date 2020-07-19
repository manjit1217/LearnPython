no=[1,1,2,2,4,4,5,5,5]
print(set(no))
print(max(no.count(x)+no.count(x+1) for x in set(no)))
for i in no:
    maximum=0
    c=no.count(i)
    d=no.count(i-1)
    c=c+d
    if c>maximum:
        maximum=c
print(maximum)



def pickingNumbers(no):
    occurance=0
    newlist = []
    for i in range(occurance,len(no)-1):
        if(abs(no[i]-no[i+1])==1):
           newlist.append(no[i])
        elif(no[i]-no[i+1]==0):
            newlist.append(no[i])
            # print(newlist)
        else:
            newlist.append(no[i])
            print(newlist)
            occurance=i
            newlist.clear()
    print(newlist)


pickingNumbers(no)



