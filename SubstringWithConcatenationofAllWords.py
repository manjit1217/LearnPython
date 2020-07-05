listOfWord=['a','b','c']
print(listOfWord[:2])

def combinationofAllWords(l):
    total_Combination=len(l)*len(l)
    data=[]

    if (total_Combination==len(data)):
        print(data)
    for i in range(0,len(l)):
        for j in range(i+1,len(l)):
            combinationofAllWords(l[i:])
            data.append(l[i]+l[j])












combinationofAllWords(listOfWord)