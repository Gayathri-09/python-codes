# reverse of a number

class Demo:
    def __init__(self):
        self.rev=0
    def accept(self):
        self.n=int(input("enter n value"))
    def process(self):
        while self.n>0:
            self.r=self.n%10
            self.rev=self.rev*10+self.r
            self.n=self.n//10
        print(self.rev)
d=Demo()
d.accept()
d.process()
    
