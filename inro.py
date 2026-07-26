class Computer:
    def config(self):
        print("hello")
obj1=Computer()
obj2=Computer()
x=2
print(type(x))
Computer.config(obj1) #another way 
Computer.config(obj2)

obj1.config()
obj2.config()