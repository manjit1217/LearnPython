# def param(*args):
#     print(len(args))
#
#
# param()
# no=123
a=[1,2,3,4]
a.insert(2,5)
print(a)

no=1000000
print(f'{no:,}')

def format_number(no):
    no = abs(no)
    s = list(str(no))
    s.insert(1,',')
    if(len(s)<3):
        return no
    else:
        for i in range(5, len(s), 4):
            s.insert(i,',')
        x=''.join(s)
        return (x)
print(format_number(1))