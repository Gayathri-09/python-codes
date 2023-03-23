# sum of digits of given number

class Demo:
    def __init__(self):
        self.sum=0
    def accept(self):
        self.n=int(input("enter n value"))
    def process(self):
        while self.n>0:
            self.r=self.n%10
            self.sum=self.sum+self.r
            self.n=self.n//10
        print("sum",self.sum)
d=Demo()
d.accept()
d.process()
