#x=[5,4,6,7,3,2,1,4,8]
x=[5,4,10,1,6,2]

# print("Balu kahithila google asiba mate jota asuchi seita hin pachariki neba")
# for i in range(0,len(x)):
#     for j in range(i+1,len(x)):
#         if(x[i])>x[j]:
#             x.insert(i, x.pop(j))
for i in range(1,len(x)):
    temp = x[i]
    j=i-1
    while(j>=0 and x[j]>temp):
        x[j+1]=x[j]
        j=j-1
    x[j+1]=temp
    # #
    # # if(x[i]>temp):
    # #     x[j] = x[i]
    # #     for y in range(0,i+1):
    # #         if( temp < x[y]):
    # #             x[y]=temp
    # #         break
    #
    # else:x[j]=temp




print(x)