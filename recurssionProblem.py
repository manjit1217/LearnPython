# def sumof1ton(n):
#     if n == 1:
#         return n
#     else:
#         return n+sumof1ton(n-1)
#
# print(sumof1ton(3))
# s='manjit'
#
# def reverseString(s):
#     if s=='':
#         return ''
#     else:
#         l=len(s)
#         sub=s[1:l]
#         subSol=reverseString(sub)
#         return subSol+s[0]
#
# print(reverseString('manjit'))
# def check_consonant(a):
#     vowl_list=['a','e','i','o','u']
#     return a in vowl_list
#
# def count_consonant(s):
#     l=len(s)
#     vowl='aeiou'
#     if len(s)==1:
#         return check_consonant(s[0])
#     else:
#         return count_consonant(s[:l-1])+check_consonant(s[l-1])
#
# def count_consonant_recursive(s):
#     vowl='aeiou'
#     if len(s)==0:
#         return 0
#     elif s[0] in vowl:
#         return 1+count_consonant_recursive(s[1:])
#     else:
#         return 1 + count_consonant_recursive(s[1:])
#
# print(count_consonant_recursive('gyvhjaasxzzbbcc'))

        # sub=s[0]
        # if check_consonant(sub):
        #     count+=1
        #     i=i+1
        #     return count_consonant(s[i:l])
        # else:
        #     i=i+1
        #     return count_consonant(s[i:l])


#
# print(count_consonant('hjbjabc'))


#
# def len_string(s):
#     if s=='':
#         return 0
#     else:return 1+len_string(s[1:])
#
# print(len_string('bjj'))
# upper=[]
# def first_upper(s):
#     if len(s)==0:
#         return upper
#     elif s[0].isupper():
#         upper.append(s[0])
#         return first_upper(s[1:])
#     else:return first_upper(s[1:])
#
# print(first_upper('bnBAbhj'))
# l=[]
#
#
# def combination_of_strings(s,n):
#     if s=='':
#         return 0
#     elif(len(s)==n):
#         for i in range(0,len(s)):
#             l.append(s[i:i+n])
#         print(l)
#         return combination_of_strings(s[:n],n-1)
#     else:
#         return combination_of_strings(s[:n],n)+combination_of_strings(s[:n],n-1)
#
#
# print(combination_of_strings('1214',4))
# def printCombinations(input, index, output, outLength):
#     if (len(input) == index):
#         output[outLength] = '\0'
#         print(*output[:outLength], sep="")
#         return
#     output[outLength] = input[index]
#     output[outLength + 1] = ' '
#     printCombinations(input, index + 1,
#                       output, outLength + 2)
#     if (len(input) != (index + 1)):
#         printCombinations(input, index + 1,
#                           output, outLength + 1)
# input = "1214"
# output = [0] * 100
# output[0] = '\0'
#
# printCombinations(input, 0, output, 0)
import itertools
no='123'
print(list(no))

def combination():
    l=['+','-','*']
    mix=[]
    for i in range(0,len(l)):
        for j in range(0,len(l)):
            t=(l[i],l[j])
            mix.append(t)
    print(mix)

#
def sum_method(no,op):
    i=0
    x=0
    for i in range(0,len(no)-1):
        a=eval(f'{int(no[i])}{op[i]}{int(no[i+1])}')
        y=eval(f'{a}{op[i]}{a}')
    print(no, op,y)
    if x==7:
        print(no,op)

for i in mix:
    sum_method('125',i)



def posible_target(no,v):
    for i in no:
        int(i)+int()



posible_target('123',7)


