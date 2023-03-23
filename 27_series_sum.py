# 1-(1/2)+(1/3)----

class Demo:
    def __init__(self):
        self.sum=0
        self.i=1
    def accept(self):
        self.n=int(input("enter n value"))
    def process(self):
        
        while self.i<=self.n:
            if self.i%2==0:
                self.sum=self.sum-(1/self.i)
                print('-','1/',self.i,end=' ')
            else:
                self.sum=self.sum+(1/self.i)
                print('+','1/',self.i,end=' ')
            self.i=self.i+1
        print(self.sum)
d=Demo()
d.accept()
d.process()
