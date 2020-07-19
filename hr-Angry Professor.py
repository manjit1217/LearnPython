a=[0,-1,1,2]

def fun(x):
    return x+2

x=map(lambda i:i+2,a)

print(list((x)))
k=2
def angry_professor(k,a):
    x=[ i for i in a if i<=0 ]
    # map(lambda i: i<=0,a)
    if len(x)<k:
        return 'Yes'
    else:return 'No'

print(angry_professor(k,a))