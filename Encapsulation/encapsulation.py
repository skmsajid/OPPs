# Encapsulation Means wrapping data and methods together into a single unit class
#  and restricting direct access to the data to protect it from unauthorized modification
#using setter and getters only, we can access data
#Python achieves encapsulation using access modifiers via naming conventions (underscores).

class Employee:
    def __init__(self, name, salary):
        self.name = name          # Public: Access from anywhere
        self.__salary = salary    # Private: Double underscore restricts direct access

    # Getter method to read private data safely
    def get_salary(self):
        return self.__salary

    # Setter method to modify private data with validation
    def set_salary(self, amount):
        if amount > 0:
            self.__salary = amount

emp = Employee("Alice", 50000)

print(emp.name)               # Works: Prints "Alice"
# print(emp.__salary)         # Error: AttributeError (Hidden)

print(emp.get_salary())       # Works: Prints 50000
emp.set_salary(60000)         # Updates safely
