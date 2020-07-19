row,col=3,3
val=[1,2,3,4,5,6,7,8,9]
def generateMatrix(r,c):
    arr=[]
    for i in range(r):
        col=[]
        for j in range(c):
            col.append(0)
        arr.append(col)

def assignValuetoMatrix(r,c,val):
    arr=[]
    count=0
    for i in range(r):
        col=[]
        for j in range(c):
            col.append(val[count])
            count = count + 1
        arr.append(col)
    print(arr)
    return (arr)
def sumOfDigonal():
     mat=assignValuetoMatrix(3,3,val)
     x=0
     y=0
     for i in range(0,len(mat)):
         for j in range(0,len(mat)):
            if( j==i):
             x=x+mat[i][j]
            if(i==len(mat)-j-1):
                y=y+mat[i][j]
     print(x)


print(sumOfDigonal())