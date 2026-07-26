"""
Methods
    Instance methods
    Class methods
    static methods
INSTANCE METHODS:
    are of two types getters(accessors) which access the attributes and settors(mutators)which alter the attributes

CLASS METHOD: which works with class variables and use decorator called @classmethod before that methods
    and pass cls in that method

STATIC METHOD: Which works with neither class and instance variables
    we use decorator called @static method , and we dont pass any arg 

"""
class Student:

    college="RGUKT"

    def __init__(self,m1,m2,m3):
        self.m1=m1
        self.m2=m2
        self.m3=m3
    # getter method 
    def get_avg(self): # y this is instance methods: bcouse this works with self i.e object
        return round((self.m1+self.m2+self.m3)/3,3)
    #setter
    def update_marks(self,marks):
        self.m1=marks

    @classmethod
    def get_school(cls):
        return cls.college

    @staticmethod
    def info():
        print("It is a static method, i dont use any class and instance variables")
s1=Student(23,23,12)
s2=Student(32,33,22)

print(s1.get_avg())
s2.update_marks(56)
print(s2.m1)

print(Student.get_school())
Student.info()

