# GrandFather
#       ▲
#       |
#    Father
#       ▲
#       |
#     Child
class G:
    def G(self):
        print("I am a Grandfather")
class F(G):
    def F(self):
        print("I am a Father")
class C(F):

    def C(self):
        print("I am a child")

child=C()
child.C()
child.F()
child.G()


