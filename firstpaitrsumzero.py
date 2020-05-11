no=[-3, -2, 0, 1, 2, 4]
l = 0
r = len(no) - 1
while(no[l]+no[r]!=0):
    if(no[l]+no[r])== 0:
        print(no[l], no[r])
    if(no[l]+no[r])<0:
        l = l+1
    elif(no[l]+no[r])>0:
        r = r-1
print(no[l], no[r])

