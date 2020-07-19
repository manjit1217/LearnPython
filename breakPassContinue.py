for i in range(0, 3):
    if (i == 0):
        print('con')
        pass# After the pass code code will run as usal, even next line wil ruuen in the same loop
        print('after pass')
    elif (i == 1):
        print('break')
        break# Break will terminate the code and no code will run after this loop
    elif (i == 2):
        print('brk')
        continue
        print('after continu')# this will not run it will end this loop and move to next loop
#Difference b/w pass and Continue pass, next line after pass will execute even in same if loop.
#but in continue next line will not execute

class demo:
    def __init__(self):
        pass


    # def pas(self):
    #     pass
    # def contin(self):
    #     continue
    # def brk(self):
    #     break