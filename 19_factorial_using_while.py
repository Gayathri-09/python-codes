# factorial of a number

class Demo:
    def __init__(self):
        self.c=1
        self.fact=1
    def accept(self):
        self.n=int(input("enter n value"))
    def process(self):
        while self.c<=self.n:
            self.fact=self.fact*self.c
            print(self.c,self.fact)
            self.c=self.c+1
d=Demo()
d.accept()
d.process()
