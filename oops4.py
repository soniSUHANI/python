class students:
    numberOfSubjects = 5
    def __init__(self,marks1,marks2,marks3):
        self.web = marks1
        self.python=marks2
        self.maths=marks3
    # def averageCalc(self):
    #     print((self.web+self.python+self.maths)/3)
    
    # def getMarks(self):
    #     return self.maths  #acessors

    # def setMarks(self,marks):
    #     self.math=marks   #mutators
    @classmethod
    def classMethodExample(cls):
        return cls.numberOfSubjects
    @staticmethod
    def staticMethodExample():
        print("this is an examplle of static method")
student1=students(5,4,3)
student2=students(7,8,9)
student3=students(1,6,9)
print(students.classMethodExample())
students.staticMethodExample()
# print(student1.averageCalc())
# print(student2.averageCalc())
# print(student3.averageCalc())






        