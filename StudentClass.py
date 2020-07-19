class Student:
    def __init__(self,first_name,last_name,id,scores):
        self.first_name=first_name
        self.last_name=last_name
        self.id=id
        self.scores=scores
    def calculate(self):
        avg=sum(self.scores)/len(self.scores)
        if avg>=90 and avg<=100:
            return 'O'
        elif avg>=80 and avg<=90:
            return 'E'
        elif avg>=70 and avg<=80:
            return 'A'
        elif avg>=55 and avg<=70:
            return 'P'
        elif avg>=40 and avg<=50:
            return 'D'
        elif avg<40:
            return 'T'
    def output(self):
        print(f'Name:{self.first_name},{self.last_name}')
        print(f'Id:{self.id}')
        print(f'Grade:{self.calculate()}')

a,b,c=map(str,input().split())
no_of_scores=int(input())
scores=list(map(int,input().strip().split()))[:no_of_scores]
obj=Student(a,b,c,scores)
obj.output()

