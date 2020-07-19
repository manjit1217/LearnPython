# decorator function to capitalize names
def names_decorator(function):
    def wrapper(arg1, arg2):
        arg1 = arg1.capitalize()
        arg2 = arg2.capitalize()
        string_hello = function(arg1, arg2)
        return string_hello
    return wrapper

@names_decorator
def say_hello(name1, name2):
    return 'Hello ' + name1 + '! Hello ' + name2 + '!'
@names_decorator
def say_hi(name1,name2):
    return f'Hi {name1} heelo {name2}'

print(say_hello('sara', 'ansh')) 	 # ou
print(say_hi('milu','milan2'))



def fun1(fun):
    print(fun)
    def fun2():
        print('fun2',fun)
    fun2()

print(fun1('m'))

# def make_pretty(func):
#     def inner():
#         print("I got decorated")
#         # func()
#     return inner
#
# def ordinary():
#     print("I am ordinary")
#
# pretty=make_pretty(ordinary())
# pretty()