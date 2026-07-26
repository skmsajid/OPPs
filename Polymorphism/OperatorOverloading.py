"""
Operator overloading
we can not use operator between different type of objects(custom objects we create) like 2+4
so we overload the opeartor using some magic methods in python as bellow 
Operator    Magic Method
+   __add__(self,other)
-   __sub__(self,other)
*   __mul__(self,other)
/   __div__(self,other)
<   __lt__(self,other)
>   __gt__(self,other)
>=  __ge__(self,other)
..,etc
"""
class Student:
    def __init__(self,m):
        self.m=m
    def __add__(self,other):
        return Student(self.m+other.m)
    def __sub__(self, other):
        return Student(abs(self.m-other.m))
    def __mul__(self, other):
        return Student(self.m*other.m)
    def __abs__(self):
        return Student(abs(self.m)) 
    
s1=Student(23)
s2=Student(34)

s3=s1+s2
print(type(s3),s3.m)
s4=s1-s3
print(s4.m)
s5=s1*s3
print(s5.m)
s6=abs(s1)
print(s6.m)