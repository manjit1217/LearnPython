# var = {
#     {
#         'name': 'Manjit1',
#         'age': 18988
#     },
#     {
#         'name': 'Manjit2',
#         'age': 19787
#     },
#     {
#         'name': 'Manjit3',
#         'age': 7687
#     }
# }


# Python3 code here for creating class
class geeks:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def Sum(self):
        print(self.x + self.y)

list = []
list.append(geeks(2, 3))
list.append(geeks(12, 13))
list.append(geeks(22, 33))

print(list)
for obj in list:
    obj.Sum()


# We can also access instances method
# as list[0].Sum() , list[1].Sum() and so on.


class employee:
    em={}
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def add_detail(self):
        self.em['Name']=self.name
        self.em['Age']=self.age





l=[]
l.append(employee('manjit1',54))
l.append(employee('manjit2',58))
print(l[0].add_detail())
for obj in l:
    obj.add_detail()

#
# class main():
#
#     name.append()
