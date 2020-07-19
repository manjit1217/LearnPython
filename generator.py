import itertools
x=[1,2,3,4]
def fun():
    print('b4 1')
    yield 1
    print(1)
    yield 2
    print(2)
    yield 3


a=fun()
print(next(a))
print(next(a))


def fib(limit):
    # Initialize first two Fibonacci Numbers
    a, b = 0, 1
    # One by one yield next Fibonacci Number
    while a < limit:
        yield a
        a, b = b, a + b
for i in fib(5):
    print(i)
print(list(fib(5)))
#
# def gen():
#     yield 1
#     yield 2
#     yield 3
#
#
#
#
#
# print(list(gen()))


# def factorial_recursive(n):
#     # Base case: 1! = 1
#     if n == 1:
#         return 1
#
#     # Recursive case: n! = n * (n-1)!
#     else:
#         return n * factorial_recursive(n-1)
#
# print(factorial_recursive(5))
# #
# def rev_str(my_str):
#     rev=[]
#     length = len(my_str)
#     for i in range(length - 1, -1, -1):
#         rev.append(my_str[i])
#     return rev
#
#
# For loop to reverse the string
for char in rev_str("hello"):
    print(char)
x=lambda a,b,c,d:a+b+c+d
print(x(1,2,3,4))
a='dfgcvhg'

#
# a=[1,2,3]
# x=iter(a)
# print((a.)
# itertools.permutations()