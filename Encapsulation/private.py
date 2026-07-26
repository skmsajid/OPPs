#(Name Mangling)
#Python converts
#  __marks

#      ↓

# _Student__marks

class Student:

    def __init__(self):
        self.__marks = 95


s = Student()

# print(s.__marks)

print(s._Student__marks) # we should not do