str="D"
count=0
valleyCount=0
flag=0
for i in range(0,len(str)):
    if str[i] == "U":
        count=count+1
    elif str[i] == "D":
        count = count-1
    if(count<0):
        flag=1
    if(count==0 and flag==1):
        valleyCount=valleyCount+1
        flag=0
    #print(valleyCount,count,flag)



print(valleyCount)


