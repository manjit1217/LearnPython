
s="MANJIT"

# def recusrssion(s):
#     if(len(s)==0):
#         print(s)
#         return s
#     else:
#         return ( recusrssion(s[1:])+s[0])
#
# print(recusrssion(s))


def rev(s):
    if(len(s)==0):
        return s
    else:
        last_char=s[len(s)-1]
        print(last_char)
        return rev(s[:len(s)-1])

rev(s)