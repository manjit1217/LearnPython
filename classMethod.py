class Student:

    school="NIST"
    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3
    @staticmethod
    def totalMarks(m1,m2,m3):
        return (m1+m2+m3)
    @classmethod
    def schoolName(cls):
        return cls.school
    @staticmethod
    def collegeName():
        return 'Manjit'




print(Student.schoolName())
obj1=Student(1,2,3)
print(Student.collegeName)
print(Student.totalMarks(1,2,3))
# print(s1.totalMarks())
#
# print(s1.school)
