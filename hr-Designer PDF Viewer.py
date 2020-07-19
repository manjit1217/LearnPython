x='zaba'
size = [1 ,3, 1, 3, 1, 4, 1, 3, 2, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 7]
word = [size[ord(c)-ord('a')] for c in x]
print(word)
print(max(word)*len(word))
#
# no=[1 ,3, 1, 3, 1, 4, 1, 3, 2, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 7]
#
# atoz=[chr(i) for i in range(ord('a'),ord('z')+1) ]
# zip=dict(zip(atoz,no))
# print(zip)
#
# maxi=0
# for i in x:
#     print(i)
#     y="'{}'".format(i)
#     print(y)
#     if any(s in mystring for s in mykeys):
#         print(mydict[s])
#     a=zip.get(y)
#     print(a)
#     if(int(a)>maxi):
#         maxi=a
# print(maxi*len(x))
#
# print(zip)
# print(no[5])
# print(ord(x))
