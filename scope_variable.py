a=10
class A:
    def __init__(self,name):
        self.name=name

    def fun(self):
        print('A'+self.name)
class B:
    def __init__(self, name):
        self.name = name

    def fun2(self):
        print('B'+self.name)
class C(B,A):
    print('manjit')

obj_c=C('manjitc')
obj_c.fun()
print(C.mro())








#
# def nonlocal_scope_variable1():
#     a='local'
#     def scope_variable2():
#         nonlocal a
#         a='nonlocal'
#         print(a)
#     scope_variable2()
#     print(a)
#
# scope_variable1()