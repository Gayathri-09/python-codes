# reverse of digit of each no in given range

class Demo():
    def __init__(self):
        pass
    def accept(self):
        self.i=int(input("enter inital value"))
        self.f=int(input("enter final value"))
    def process(self):
        while self.i<=self.f:
            self.n=self.i
            self.rev=0
            while self.n>0:
                self.r=self.n%10
                self.rev=self.rev*10+self.r
                self.n=self.n//10
            print(self.i,self.rev)
            self.i=self.i+1
d=Demo()
d.accept()
d.process()
