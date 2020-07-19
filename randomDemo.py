# from collections import Counter
# from random import shuffle
# l=[1,2,3,4,5,1,2,3,4,6]
# print(shuffle(l))
# print(l)
# print(Counter(l))
# print(list(set(l)))
#
# print(('manjit')[::-1])
class SeeMee:
    def __init__(self):
        pass
    def youcanseeme(self):
        return 'you can see me'
    def __youcannotseeme(self):
        return 'you cannot see me'

# Outside class
Check = SeeMee()
print(Check.youcanseeme())
print(dir(Check))
#The below is called Name Mangling, for accessing the private method
print(Check._SeeMee__youcannotseeme())