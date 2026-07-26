class Student:

    def __init__(self):
        self.__age = 20

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value >= 18:
            self.__age = value

    @age.deleter
    def age(self):
        del self.__age


s = Student()

print(s.age)

s.age = 25

print(s.age)

del s.age