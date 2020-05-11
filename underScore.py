class Test:
    def __init__(self):
        self.x=5
        self.__y=6

obj=Test()

print(obj.x)
print(obj.__y)
