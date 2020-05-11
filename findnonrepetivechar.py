from collections import Counter
#find the longest NOn repetive character in string
string="youasomez"
nonRepetiveString={}
i=0
maxlen=0
def allString(str):
    for i in range(0,len(str)+1):
        for j in range(0,len(str)+1):
         x=(str[i:j])
         print(x)
         checkNonrepetiveString(x)


def checkNonrepetiveString(singleString):
    x=Counter(singleString)
    global maxlen
    if((list(x.values()).__contains__(0 or 2 or 3)) ):
        pass
    else:
        if ((x.__len__())>maxlen ):

            maxlen=x.__len__()

            print(maxlen)


allString(string)


