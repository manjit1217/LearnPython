from collections import Counter
from itertools import permutations
from pprint import pprint

lst=['for', 'ge', 'abc', 'ks', 'e', 'xyz']

pprint(list(permutations(lst)))
#
# def findCombination(lst):
#     for i in range(0,len(lst)):
#
#
#
#
# str = 'geeks'
# print(dict(Counter(str)))
# lst = ['for', 'ge', 'abc', 'ks', 'e', 'xyz']
# str1=''
# for i in range(0,len(lst)-1):
#     str1=lst[i]
#     for j in range(i+1,len(lst)):
#         str1=str1+lst[j]
#         if str1==str:
#             print(True)
#
