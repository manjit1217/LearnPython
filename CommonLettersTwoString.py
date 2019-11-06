from collections import Counter
str1='Manjit'
str2='Milan'

def CommonLetters(str1,str2):
    x=set(str1)
    y=set(str2)

    print((x&y))


CommonLetters(str1,str2)