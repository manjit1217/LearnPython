


s='manjit'
print(s[::-1])
def reverse(s):
    if len(s)==0:
        return s
    else:
        print(s[len(s)-1:len(s)])
        reverse(s[:len(s)-1])

reverse(s)