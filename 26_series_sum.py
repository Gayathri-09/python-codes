# sum of fractions

class Demo:
    def __init__(self):
        self.sum=0
        self.i=1
    def accept(self):
        self.n=int(input("enter n value"))
    def process(self):
        while self.i<=self.n:
            self.sum=self.sum+(1/self.i)
            self.i=self.i+1
        print(self.sum)
d=Demo()
d.accept()
d.process()
        
