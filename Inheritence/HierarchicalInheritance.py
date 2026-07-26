#   Parent
#   /   \
# son  Daughter
#like a Tree
class Parent:

    def house(self):
        print("House")


class Son(Parent):
    pass


class Daughter(Parent):
    pass


Son().house()
Daughter().house()