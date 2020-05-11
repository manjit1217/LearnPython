arr=[
    [1, 1, 1, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [1, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0 ,0],]
hourglass=[]
print(arr[0][2])
x=[]
for i in range(len(arr[0])-1):
    for j in range(len(arr)-2):
        x.append(sum(arr[j][i:i+3])+arr[j+1][i+1]+sum(arr[j+2][i:i+3]))
print(max(x))
#
# #
# print(max([sum(arr[j][i:i+3]) + arr[j+1][i+1] + sum(arr[j+2][i:i+3])
#         for j in range(len(arr)-2) for i in range(len(arr[0])-1)]))
