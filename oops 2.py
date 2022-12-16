class person:
    def __init__(self) :
        self.name="anisha"
        self.age="18"
    def updateName(self):
        self.name="soum"
    def compareAge(self,other):
        if self.age == other.age:
            return True
        else:
            return False
person1=person()
person2=person()
person1.age= 22
if person1.compareAge(person2):
    print("they are of same age ")
else:
    print("they are of different age")
# person2.name="Atul"
# person1.updateName()
print(person1.name,person1.age)
print(person2.name,person2.age)

