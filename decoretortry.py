
def deco_fun(fun):
    print('deco fun')
    def upper():
        print('hii')
        # s.capitalize()
        fun()
    return upper



def display():
    print('manjit')


x=deco_fun(display())
x()
