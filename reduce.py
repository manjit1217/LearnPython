from functools import reduce
def sum(x, y):
    return x + y

def is_even(x):
    if x%2==0:
        return x

l = [1, 2, 3, 4, 5]
print(reduce(sum,l))
print(list(filter(is_even,l)))