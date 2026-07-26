
# What is Inheritance?

Inheritance allows one class to **reuse** the properties and methods of another class.

Think of it like this:

```text
Parent (Father)
    ↓
Child (Son)
```

If a father owns a house, the child inherits it. Similarly, if a parent class has methods and variables, the child class automatically gets access to them.

Example:

```python
class Animal:

    def eat(self):
        print("Eating...")

class Dog(Animal):
    pass

d = Dog()
d.eat()
```

Output:

```
Eating...
```

`Dog` doesn't define `eat()`, but it inherits it from `Animal`.

---

# Memory Representation

```text
            Animal
        ----------------
        eat()
        sleep()
        ----------------
               ▲
               |
            Dog
        ----------------
        bark()
        ----------------
```

Python first looks in `Dog`. If it doesn't find the method, it looks in `Animal`.

---

# Types of Inheritance

Python supports **5 types** of inheritance.

---

# 1. Single Inheritance

One child inherits from one parent.

```text
Animal
   ▲
   |
 Dog
```

Implementation:

```python
class Animal:

    def eat(self):
        print("Eating")

class Dog(Animal):

    def bark(self):
        print("Barking")

d = Dog()

d.eat()
d.bark()
```

Output

```
Eating
Barking
```

---

# 2. Multiple Inheritance

One child inherits from multiple parents.

```text
 Father1    Father2
     ▲         ▲
      \       /
       \     /
        Child
```

Example

```python
class Father:

    def money(self):
        print("Money")

class Mother:

    def love(self):
        print("Love")

class Child(Father, Mother):
    pass

c = Child()

c.money()
c.love()
```

Output

```
Money
Love
```

The child inherits from both classes.

---

# 3. Multilevel Inheritance

Inheritance continues in levels.

```text
GrandFather
      ▲
      |
   Father
      ▲
      |
    Child
```

Example

```python
class GrandFather:

    def land(self):
        print("Land")

class Father(GrandFather):

    def house(self):
        print("House")

class Child(Father):

    def bike(self):
        print("Bike")

c = Child()

c.land()
c.house()
c.bike()
```

Output

```
Land
House
Bike
```

The child inherits from both `Father` and `GrandFather`.

---

# 4. Hierarchical Inheritance

One parent has multiple children.

```text
        Animal
       /      \
     Dog      Cat
```

Example

```python
class Animal:

    def eat(self):
        print("Eating")

class Dog(Animal):

    def bark(self):
        print("Bark")

class Cat(Animal):

    def meow(self):
        print("Meow")
```

Usage

```python
d = Dog()
c = Cat()

d.eat()
c.eat()
```

Both inherit `eat()`.

---

# 5. Hybrid Inheritance

Combination of two or more inheritance types.

Example

```text
        A
      /   \
     B     C
      \   /
        D
```

Implementation

```python
class A:

    def a(self):
        print("A")

class B(A):

    def b(self):
        print("B")

class C(A):

    def c(self):
        print("C")

class D(B, C):

    def d(self):
        print("D")
```

Now

```python
obj = D()

obj.a()
obj.b()
obj.c()
obj.d()
```

Output

```
A
B
C
D
```

This is called **hybrid inheritance** because it combines hierarchical and multiple inheritance.

---

# How does Python find methods?

Suppose

```python
class A:

    def show(self):
        print("A")

class B(A):
    pass

obj = B()

obj.show()
```

Python searches like this

```
B
↓
A
↓
object
```

If it finds `show()` in `A`, it stops.

---

# What if both parent and child have the same method?

```python
class A:

    def show(self):
        print("A")

class B(A):

    def show(self):
        print("B")
```

Now

```python
obj = B()
obj.show()
```

Output

```
B
```

This is **Method Overriding**.

Python always gives preference to the child class.

---

# Multiple Inheritance and Method Resolution Order (MRO)

Suppose

```python
class A:

    def show(self):
        print("A")

class B:

    def show(self):
        print("B")

class C(A, B):
    pass

obj = C()
obj.show()
```

Output

```
A
```

Why?

Because `A` is listed before `B`.

Search order

```
C
↓
A
↓
B
↓
object
```

---

Now reverse the order

```python
class C(B, A):
    pass
```

Output

```
B
```

The inheritance order matters.

You can see Python's Method Resolution Order (MRO):

```python
print(C.mro())
```

Output

```text
[<class '__main__.C'>,
 <class '__main__.A'>,
 <class '__main__.B'>,
 <class 'object'>]
```

---

# `super()` in Inheritance

Suppose

```python
class Animal:

    def __init__(self):
        print("Animal Constructor")

class Dog(Animal):

    def __init__(self):
        super().__init__()
        print("Dog Constructor")

d = Dog()
```

Output

```
Animal Constructor
Dog Constructor
```

`super()` calls the parent class's method according to the MRO.

---

# Constructor Inheritance

```python
class A:

    def __init__(self):
        print("A")

class B(A):
    pass

obj = B()
```

Output

```
A
```

Since `B` doesn't define its own constructor, it inherits `A`'s constructor.

---

Now

```python
class B(A):

    def __init__(self):
        print("B")
```

Output

```
B
```

The parent constructor is **not** called automatically.

If you want both constructors:

```python
class B(A):

    def __init__(self):
        super().__init__()
        print("B")
```

Output

```
A
B
```

---

# Summary

| Type         | Structure                      |
| ------------ | ------------------------------ |
| Single       | One parent → One child         |
| Multiple     | Multiple parents → One child   |
| Multilevel   | Grandparent → Parent → Child   |
| Hierarchical | One parent → Multiple children |
| Hybrid       | Combination of the above       |

---

## Key rules to remember

1. A child class automatically inherits accessible methods and variables from its parent.
2. If the child defines a method with the same name, it overrides the parent's version.
3. In multiple inheritance, Python follows the **Method Resolution Order (MRO)** to decide which parent's method to use.
4. `super()` calls the next method in the MRO, which is commonly used to invoke parent constructors or methods.
5. All Python classes ultimately inherit from the built-in `object` class, even if you don't mention it explicitly.

Mastering inheritance also means understanding **method overriding**, **MRO**, and **`super()`**, because they determine how inherited methods are actually found and executed. These are the topics that interviewers often focus on after asking about the basic inheritance types.



That's an excellent question. Most tutorials show how methods are inherited, but they don't explain **what happens to attributes**. Once you understand this, inheritance becomes much clearer.

---

# First remember one important rule

There are **two kinds of attributes**:

1. **Instance attributes** (stored inside each object)
2. **Class attributes** (stored inside the class)

They are inherited differently.

---

# Case 1: Class Attributes

Example

```python
class Animal:
    kingdom = "Animalia"      # Class attribute

class Dog(Animal):
    pass

d = Dog()
```

Memory:

```
Animal
----------------
kingdom = "Animalia"
----------------
        ▲
        |
      Dog
        ▲
        |
        d
```

Now,

```python
print(d.kingdom)
```

Output

```
Animalia
```

How?

Python searches like this:

```
d object
   ↓
Dog class
   ↓
Animal class   ✅ Found kingdom
```

So `d.kingdom` works even though `kingdom` is defined in `Animal`.

You can also do:

```python
print(Dog.kingdom)
```

Output:

```
Animalia
```

---

# Case 2: Instance Attributes

Now suppose:

```python
class Animal:

    def __init__(self):
        self.age = 5
```

The attribute `age` is **not stored in the class**.

It is stored in the object.

---

## If the child does not define `__init__`

```python
class Dog(Animal):
    pass

d = Dog()
```

Python automatically calls `Animal.__init__()`.

Memory:

```
d
----------
age = 5
----------
```

Now

```python
print(d.age)
```

Output

```
5
```

The object has the attribute because the parent's constructor initialized it.

---

# What if the child has its own constructor?

```python
class Animal:

    def __init__(self):
        self.age = 5

class Dog(Animal):

    def __init__(self):
        self.color = "Black"
```

Now

```python
d = Dog()
```

Memory:

```
d
---------
color = Black
---------
```

Notice something important.

There is **no `age`**.

Because the parent's constructor was never called.

So

```python
print(d.age)
```

Output

```
AttributeError
```

---

# Solution: `super()`

```python
class Animal:

    def __init__(self):
        self.age = 5

class Dog(Animal):

    def __init__(self):
        super().__init__()
        self.color = "Black"
```

Now

```
Dog() created
        ↓
Dog.__init__()
        ↓
super().__init__()
        ↓
Animal.__init__()
        ↓
age created
        ↓
Back to Dog.__init__()
        ↓
color created
```

Memory:

```
d
-------------
age = 5
color = Black
-------------
```

Now

```python
print(d.age)
print(d.color)
```

Outputs

```
5
Black
```

---

# Accessing Parent Attributes Inside Child Methods

Example

```python
class Animal:

    def __init__(self):
        self.age = 5

class Dog(Animal):

    def display(self):
        print(self.age)
```

Now

```python
d = Dog()
d.display()
```

Output

```
5
```

Why?

Because `self` refers to the `Dog` object, and that object contains `age`.

---

# Child Can Add More Attributes

```python
class Animal:

    def __init__(self):
        self.age = 5

class Dog(Animal):

    def __init__(self):
        super().__init__()
        self.color = "Black"
```

Memory

```
Dog Object
-----------------
age = 5
color = Black
-----------------
```

The child object simply has **both** attributes.

---

# Can the Child Modify Parent Attributes?

Yes.

```python
class Animal:

    def __init__(self):
        self.age = 5

class Dog(Animal):

    def change(self):
        self.age = 10
```

Now

```python
d = Dog()

print(d.age)
```

```
5
```

After

```python
d.change()

print(d.age)
```

```
10
```

The child method changed the inherited instance attribute.

---

# Class Attributes Are Also Accessible

```python
class Animal:

    kingdom = "Animalia"

class Dog(Animal):

    def show(self):
        print(self.kingdom)
```

Output

```
Animalia
```

Python searches:

```
Object
   ↓
Dog
   ↓
Animal
```

---

# What if Child Creates Same Class Attribute?

```python
class Animal:
    kingdom = "Animalia"

class Dog(Animal):
    kingdom = "Dogs"
```

Now

```python
print(Dog.kingdom)
```

```
Dogs
```

```python
print(Animal.kingdom)
```

```
Animalia
```

The child's class attribute **shadows** the parent's.

---

# What if Child Creates Same Instance Attribute?

```python
class Animal:

    def __init__(self):
        self.age = 5

class Dog(Animal):

    def __init__(self):
        super().__init__()
        self.age = 10
```

Memory

```
Dog Object
------------
age = 10
------------
```

The value from the parent was created first, then immediately replaced by the child.

---

# Can We Access Parent Attribute Directly?

Yes, through the object.

```python
class Animal:

    def __init__(self):
        self.age = 5

class Dog(Animal):
    pass

d = Dog()

print(d.age)
```

Output

```
5
```

There is **no special syntax** like

```python
Animal.age
```

because `age` is **not in the class**.

It exists only inside the object.

---

# Complete Picture

```python
class Animal:
    kingdom = "Animalia"

    def __init__(self):
        self.age = 5


class Dog(Animal):

    def __init__(self):
        super().__init__()
        self.color = "Black"

    def show(self):
        print(self.age)
        print(self.color)
        print(self.kingdom)


d = Dog()
d.show()
```

Memory:

```
Animal Class
------------------------
kingdom = Animalia
------------------------

Dog Class
------------------------
(show method)
------------------------

Dog Object
------------------------
age = 5
color = Black
------------------------
```

Output

```
5
Black
Animalia
```

---

# The key idea

Methods are **looked up** through the inheritance chain, but instance attributes are **not inherited by copying**. Instead:

* Class attributes live in the class and are found by attribute lookup (`object → child class → parent class → ...`).
* Instance attributes live inside the object itself. The parent class's `__init__()` creates them. If the child doesn't call the parent's constructor (directly or indirectly via `super()`), those attributes are never created.

This distinction—**methods are inherited through lookup, while instance attributes exist only if some constructor initializes them**—is one of the most important concepts in Python inheritance.
