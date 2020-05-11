# x=0
# def fact(n):
#     global x
#     if(n==1):
#         return 1
#     else:
#         x=n*fact(n-1)
#         print(x)
#     return x
#
# result=fact(5)
# print(result)


a=lambda n:n*(n-1)
print(a(5))