from collections import Counter
# s='KYQYTWXTDQXWDLKIXNWIITFBLIHRNGDZGVYCRXVWNUVSFFACUXMCSTFFBNWQVBQCWOEPNBOAVJUCOUGITSMNLSUOFRFAUXETNIKAJYCEJWIXSOHMGUBTOWKVPPXJOCEBKPDWNFCXDLWVZEJIALBOJLLYCIJQKOTXDWTSDVRIGOEIUPQUCRKLFVLHFXASNVPSUKKXHCGOSMYMDOIGHUTMPHWWEYORTFJNPVNXZVNTJNFMBPSIJOXAVTXZRNSKTDAKANJAKYTTLBFMSAXCOUCJNBKGPESKHSWJHGJREFKSISGASDCIZHTOKFUBJNLSFIBPQNGWSROCLVCDAHNAQGOALJCUYPOFZPUPEDMYWAAHXDKAMXACFQCQBGMZWAHVRBNYEZWABXJBCVBOSDQZTSPVZDWXFDSZHFXNGTQISZLUVMKPPAPIVGFWKCTRHNQQVPEBJULDVYA'
#
# k=26
# n=len(s)
#
# def findFirstNonDuplicate(l):
#     for i in l:
#         i
#
# 
#
# def merge(s,k):
#     for i in range(0,len(s),k):
#         a=s[i:i+k]
#         final=''
#         for i in a:
#             if i not in final:
#                 final=final+i
#
#         print(final)
#


l=[1,2,2,3,3,]
print(type(set(l)))
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        i=0
        v_len=len(nums)
        while i < v_len:
            if nums[i] in nums[i+1:]:
                del nums[i]
                v_len-=1
            else:
                i+=1
        print (nums)
        return len(nums)

# l=[1,2,1,2]
# newl=[]
# newl=Counter(l).keys()
# l=list(newl)
#
# for i in l:
#     print (i)


# name='manjit kumar patro'
# x=name.split(' ')
# a=[i.capitalize() for i in x ]
# print(' '.join(a))




# i=0
#
# l=[1,2,3,4,56]
#
# l.insert(1,3)
#
# print(l)
#
# while(i<3):
#     x=int(input("Guess"))
#     print(x)
#     if(x==9):
#         print("you are correct")
#         exit()
#     else:    i=i+1
#
