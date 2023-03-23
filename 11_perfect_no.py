# program to find perfect number

class Demo:
    def __init__(self):
        self.c=1
        self.sum=0
    def accept(self):
        self.n=int(input("enter n value"))
    def process(self):
        while self.c<=self.n//2:
            if self.n%self.c==0:
                print(self.c)
                self.sum=self.c+self.sum
            self.c=self.c+1
    def output(self):
        print("sum=",self.sum)
        if self.sum==self.n:
            print("perfect")
        else:
            print("not perfect")
d=Demo()
d.accept()
d.process()
d.output()
