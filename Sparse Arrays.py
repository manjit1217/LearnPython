from collections import Counter
strings=['ab','ab','abc','abcd']
query=['ab','abc']

def matchstring(strings,queries):
    ocurs = Counter(strings)
    print(ocurs)
    return [ocurs[queries] for queries in queries]
    # for i in range(len(query)):
    #     count = 0
    #     for j in range(len(strings)):
    #         if(query[i]==strings[j]):
    #             count=count+1
    #     print(count)



print(matchstring(strings,query))
