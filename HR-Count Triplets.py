import itertools

a=(1,2,3)
print(a*2)
def combination(l):
    new_list=[]
    for i in range(0,len(l)):
        new_list.append([i])
#
# def count_triplet(l,n):
#     x=list(itertools.combinations(l,3))
#     s=0
#     newl=[]
#     for i in x:
#         for x in range(0,len(i)-1):
#             if(i[x+1]==n*i[x]):
#                 s=s+1
#             else:s=0
#         if (s>=2):
#             newl.append(i)
#     print(len(newl))




def count_triplet(l,n):
    dict1={}
    dict3={}
    count=0
    for a in l:
        if a in dict3:
            count=count+dict3[a]
        if a in dict2:
            
            


        for i in range(a+1,len(l)):
            if m in l:
                mi=l.index(m)
                m=l[mi]*m
                print(m,mi)





            if (l[i] == n * l[i]):
                    s=s+1
            else: s=0
        if (s>=2):
            newl.append(i)


from collections import Counter
l=[1, 3, 9, 9, 27, 81]
print((Counter(l))')
l1=[1,2,2,4]
count_triplet(l,3)

# def combo2(lst,n):
#     if n==0:
#         return [[]]
#     l=[]
#     for i in range(0,len(lst)):
#         m=lst[i]
#         remLst=lst[i+1:]
#         for p in combo2(remLst,n-1):
#             l.append([m]+p)
#     return l
# print(combo2('ABC',3))
#
# # def permutaiont(l,n):
# #     l=list(l)
# #     mix=[]
# #     if n==0:
# #         return  [[]]
# #     else:
# #         for i in range(0,len(l)):
# #             x=l[i]
# #             rem_list=l[i+1:]
# #             for p in permutaiont(rem_list,n-1):
# #                 mix.append([x]+p)
# #     return (mix)
#
# print(permutaiont('abc',3))
# def all_perms(elements):
#     if len(elements) <=1:
#         yield elements
#     else:
#         for perm in all_perms(elements[1:]):
#             for i in range(len(elements)):
#                 # nb elements[0:1] works in both string and list contexts
#                 yield perm[:i] + elements[0:1] + perm[i:]
# print(list(all_perms('abcd')))
#
