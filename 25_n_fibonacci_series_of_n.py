# n fibonacci series

class Demo:
    def __init__(self):
        self.a=0
        self.b=1
        self.i=1
    def accept(self):
        self.n=int(input("enter n value"))
    def process(self):
        while self.i<=self.n:
            print(self.a)
            self.c=self.a+self.b
            self.a=self.b
            self.b=self.c
            self.i=self.i+1
d=Demo()
d.accept()
d.process()
