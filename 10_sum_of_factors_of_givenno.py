# program to find sum of factors

class Demo:
    def __init__(self):
        self.c=1
        self.sum=0
    def accept(self):
        self.n=int(input("enter n value"))
    def process(self):
        while self.c<=self.n:
            if self.n%self.c==0:
                print(self.c)
                self.sum=self.c+self.sum
            self.c=self.c+1
    def output(self):
        print("sum=",self.sum)
d=Demo()
d.accept()
d.process()
d.output()
