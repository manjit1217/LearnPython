array1=[2,7,9,10,15]
array2=[1,5,7,9,10,14,16]
array2.sort()
newarr=array1+array2
print(newarr)

flag=True
j=0
for i in range(0,len(newarr)-1):
    if newarr[i]<newarr[i+1]:
        t=newarr[i]
        newarr[i]=newarr[i+1]
        newarr[i+1]=t
        i=i-1
print(newarr)



# for i in range(0,len(array1)):
#     for j in range(0,len(array2)):
#         if array1[i]<array2[j]:
#             newarr.append(array1[i])
#         else:newarr.append(array2[j])


