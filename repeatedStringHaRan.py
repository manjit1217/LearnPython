# from collections import Counter
# s = "a"
# n = 1000000000000
# newString=[]
# i=0
# while(len(newString) <= n):
#     if(i>=len(s)):
#         i=0
#     newString.append(s[i])
#     i=i+1
#
# print(Counter(newString).get('a'))
#
import repeatedString


def repeatedtring(s, n):
    print(s[2:])
    a_cnt = s.count('a')
    num = n//len(s)
    mod = n%len(s)
    count = a_cnt*num + s[:mod].count('a')
    return count


print(repeatedtring('aba',15))
