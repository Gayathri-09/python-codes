# mathematical table

class Demo:
    def __init__(self):
        self.c=1
    def accept(self):
        self.n=int(input("enter n value"))
    def process(self):
        while self.c<=10:
            self.r=self.n*self.c
            print(self.n,"*",self.c,"=",self.r)
            self.c=self.c+1
d=Demo()
d.accept()
d.process()
