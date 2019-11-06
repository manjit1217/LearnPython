from collections import Counter
str="pwwkew"

def get_all_substrings(input_string):
  length = len(input_string)
  return [input_string[i:j+1] for i in range(length) for j in range(i,length)]

x= get_all_substrings(str)
for i in range(0,len(x)):
    shortstr=Counter(x[i])
    if( shortstr.values().__contains__(2 or 3)):
        pass
    else: print(shortstr.items())
#
# def string2Short(str):
#     for i in range(0,len(str)):
#         x=str[:len(str)-i]
#         print('----------'+x)
#         shortstr=Counter(list(x))
#         print(shortstr)
#         # print(list(shortstr.values()).__contains__(2 or 3))
#         for j in shortstr.values():
#             if j==1:
#                 print(list(shortstr.keys()))
# string2Short(str)
#     short_str=Counter(list(string2Short(str)))
#     for i in short_str.values():
#         if i==1:
#             print(short_str.keys())
# #
# # print(x)
# x=''
# for i in range(0,len(str)):
#     x=str[:len(str)-i]
#     dict=Counter(x)
#     if dict.values()
#
# if "2" in dict.values():



