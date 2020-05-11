s = 'My name is khan'
#
def reverse(s):
    words = s.split(' ')
    newwords = [words[::-1] for word in words]
    Newsen = " ".join(newwords)
    print(Newsen)
#
#
# reverse(s)


def reverse(s):
    rev=[]
    a=''
    words = s.split(' ')
    x=len(words)-1
    while( x>=0 ):
        rev.append(words[x])
        x=x-1
    a=' '.join(rev)
    print(a)
reverse(s)

#
#
# reverse(s)