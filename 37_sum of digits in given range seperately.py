# sum of digits in given range seperately

class Demo():
    def __init__(self):
        pass
    def accept(self):
        self.i=int(input("enter inital value"))
        self.f=int(input("enter final value"))
    def process(self):
        while self.i<=self.f:
            n=self.i
            self.sum=0
            while n>0:
                self.r=n%10
                self.sum=self.sum+self.r
                n=n//10
            print(self.i,'--------->',self.sum)
            self.i=self.i+1
d=Demo()
d.accept()
d.process()
