l=[0,1]

def fibo(n):
    s=[0,1]
    if(n==0):
        print('invalid')
    elif(n==1):
        return 0
    elif(n==2):
        return 1
    else:

        x= fibo(n-1)+fibo(n-2)
        l.append(x)
        print(l,x)
        return x
    print(s)

print(fibo(9))