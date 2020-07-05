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
        print('------',string)




permutation(['a','b','c'])