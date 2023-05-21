# prime number

class Demo():
    def __init__(self):
        pass
    def accept(self):
        self.i=int(input("enter inital value"))
        self.f=int(input("enter final value"))
    def process(self):
        while self.i<=self.f:
            self.r=1
            self.c=2
            while self.c<=self.i/2 and self.r!=0:
                self.r=self.i%self.c
                self.c=self.c+1
            if self.r!=0:
                print(self.i)
            self.i=self.i+1
d=Demo()
d.accept()
d.process()
        
        
