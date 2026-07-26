# It comes from a famous saying:

# If it walks like a duck, swims like a duck, and quacks like a duck, then treat it like a duck
"""
Polymorphism
│
├── Meaning
│      ├── Poly = Many
│      └── Morph = Forms
│
├── Why
│      ├── One interface
│      ├── Different behavior
│      └── Cleaner reusable code
│
├── Compile-Time (Static)
│      ├── Early Binding
│      ├── Function Overloading
│      └── Not truly supported in Python
│
└── Runtime (Dynamic)
       ├── Late Binding
       ├── Method Overriding
       ├── Dynamic Dispatch
       ├── MRO used for lookup
       └── Fully supported in Python

Python-specific extension
│
└── Duck Typing
       ├── Doesn't require inheritance
       └── Requires compatible behavior
"""
class Pycharm:
    def execute(self):
        print("Compile...")
        print("execute...")
class MyEditor:
    def execute(self):
        print("spell chell...")
        print("Grammer...")
        print("Compile...")
        print("execute...")
class Laptop:
    def code(self,ide):
        ide.execute()

pycharm=Pycharm()
myedutor=MyEditor()

lap=Laptop()

lap.code(pycharm)
print("#same code function behaves differently!")
lap.code(myedutor)


