    
    #so it like combination 
# eg:
    #     A
    #   /   \
    #  B     C
    #  |     |
    #  D     E
    #   \   /
    #     F
 
class A:
    def show(self):
        print("A")


class B(A):
    pass


class C(A):
    pass


class D(B, C):
    pass


d = D()

d.show()