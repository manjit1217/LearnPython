#Possible string from a given string.


count=0
def permutation(s,step=0):
    global count
    string=list(s)
    if (step==len(string)):
        count=count+1
        print('+++++',str(string),count)
    for i in range(step,len(string)):
        string[step],string[i]=string[i],string[step]
        permutation(string, step+1)


def permu(s,l,r):
    r=len(s)-1
    if l==r:
        print(s)
    else:
        for i in range(l,r):
            s[l],s[r]=s[r],s[l]
            permu(s,l+1,r)
            s[l], s[r] = s[r], s[l]



permu([+'a','b','c'],0,2)