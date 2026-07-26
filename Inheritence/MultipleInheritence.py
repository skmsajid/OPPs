#Mother     Father
#    \      /
#     \    /
#      \  /
#      Son

class Father:
    def fatherFeature(self):
        print("father feature")
class Mother:
    def motherFeature(self):
        print("mother feature")
class Son(Father,Mother):
    def sonFeature(self):
        print("son feature")
child=Son()
child.sonFeature()
child.motherFeature()
child.fatherFeature()