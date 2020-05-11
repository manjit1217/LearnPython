x='cab'
print(x[0:1])
#
# print(["q".join(sorted(x[1:3]))] for j in range(len(x)-2))
# h_letters = [ letter for letter in 'human' ]
#
# for j in range(len(s)-i+1):
#     a.append("q".join(sorted(x[1:3])))

#
# x='aaaa'
# a=[]
# i=1
# for i in range(1,len(x)+1):
#     for j in range(len(x)-i+1):
#         a.append("".join(sorted(x[j:j+i])))
#     print(a)
#     a.clear()
    # b=["".join(sorted(x[j:j+i])) for j in range(len(x)-i+1)]
    # print(b)

#
#
# #
#
from collections import Counter

def sherlockAndAnagrams(s):
    count=0
    a=[]
    for i in range(1,len(s)+1):
        #a = ["".join(sorted(s[j:j+i])) for j in range(len(s)-i+1)]
        for j in range(len(s) - i + 1):
            a.append("".join((s[j:j + i])))
        print(a)
        b = Counter(a)
        print(b)
        for j in b:
            count+=b[j]*(b[j]-1)/2
        a.clear()
        print(int(count))

sherlockAndAnagrams('cdcdcd')