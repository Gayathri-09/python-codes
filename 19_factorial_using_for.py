# factorial of a number

class Demo:
    def __init__(self):
        self.c=1
        self.fact=1
    def accept(self):
        self.n=int(input("enter n value"))
    def process(self):
        for i in range(1,self.n+1):
            self.fact=self.fact*i
            print("factorial of {} is {}".format(i,self.fact))
d=Demo()
d.accept()
d.process()
