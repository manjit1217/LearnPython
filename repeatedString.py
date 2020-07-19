# from collections import Counter
# n=10
# s="aba"
# x=[]
# def repeatedString(s,n):
#     newList=[]
#     if(n==len(s)):
#         coll=max(Counter(s).values())
#         print(coll)
#     else:
#         for i in range(0,n):
#             if(i>len(s)-1):
#                 i=0
#                 newList.append(s[i])
#             else:
#                 newList.append(s[i])
#     print(newList)
#
# repeatedString(s,n)
#
string = input("Enter a string: ")
lst1 = []
cnt=[]
for char in string:
    if char not in lst1:
        lst1.append(char)
for item in lst1:
    print(item,string.count(item), sep = ",")
