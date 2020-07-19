def utopian_tree(n):
    n1=0
    h1=1
    for i in range(1,n+1):
        if i%2!=0:
            n1=i
            h1=h1*2
        elif i %2==0:
            n1=i
            h1=h1+1
    return(h1)
utopian_tree(4)





