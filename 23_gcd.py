#GCD

class Demo:
    def __init__(self):
        pass
    def accept(self):
        self.a=int(input("enter a value"))
        self.b=int(input("enter b value"))
    def process(self):
        while self.b!=0:
            self.r=self.a%self.b
            self.a=self.b
            self.b=self.r
        print(self.a)
d=Demo()
d.accept()
d.process()
        
