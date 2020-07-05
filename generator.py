def factorial_recursive(n):
    # Base case: 1! = 1
    if n == 1:
        return 1

    # Recursive case: n! = n * (n-1)!
    else:
        return n * factorial_recursive(n-1)

print(factorial_recursive(5))
# l=[1,2,3,4,5]
# def sum(x):
#         yield int(x)+2
#
#
# for x in l:
#     print(list(sum(x)))