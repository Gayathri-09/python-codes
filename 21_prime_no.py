# prime or not

class Demo:
    def __init__(self):
        self.c=2
        self.r=1
    def accept(self):
        self.n=int(input("enter n value"))
    def process(self):
        while self.c<=self.n/2 and self.r!=0:
            self.r=self.n%self.c
            self.c=self.c+1
    def output(self):
        if self.r!=0:
            print("prime")
        else:
            print("not prime")
d=Demo()
d.accept()
d.process()
d.output()
