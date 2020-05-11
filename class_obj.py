# Class is like a Blueprint,but what does this exactly mean ? It means that the Class holds a Description of a particular Category
# variables are attribute
# methods are behaviour
# creating an object by instanciating the class.
# An instance is a virtual copy (but not a real copy) of the object.


class Myclass:
    def method(self):
        print('instance Method of',self)
    def classMethod(self):
        print('class method')

    def staticMethod(self):
        print('static method')






Myclass().classMethod()
My
obj=Myclass()
obj.classMethod()
















# # flip = lambda f: lambda *a: f(*reversed(a))
# #
# # def divide(a, b):
# #     return a / b
# #
# # print (flip(divide)(3.0, 1.0))
#
# def reversed_args(f):
#     return f
#
# int_func_map = {
#     'pow': pow,
#     'cmp': lambda a, b: 0 if a == b else [1, -1][a < b],
# }
#
# string_func_map = {
#     'join_with': lambda separator, *args: separator.join(args),
#     'capitalize_first_and_join': lambda first, *args: ''.join([first.upper()] + list(args)),
# }
#
# queries = int(input())
# for _ in range(queries):
#     line = input().split()
#     func_name, args = line[0], line[1:]
#     if func_name in int_func_map:
#         args = list(map(int, args))
#         print(reversed_args(int_func_map[func_name])(*args))
#     else:
#         print(reversed_args(string_func_map[func_name])(*args))
