class Computer:
    def __init__(self, cpu,ram):
        self.cpu=cpu
        self.ram=ram

    def config(self):
        print("Config is having ", self.cpu ,self.ram)


obj1=Computer("i5",10)
obj2=Computer("3 generation",13)

obj1.config()
obj2.config()