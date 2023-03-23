# b power p (b**p)

class Demo:
    def __init__(self):
        self.res=1
        self.c=1
    def accept(self):
        self.b=int(input("enter b value"))
        self.p=int(input("enter p value"))
    def process(self):
        while self.c<=self.p:
            self.res=self.res*self.b
            self.c=self.c+1
        print(self.res)
d=Demo()
d.accept()
d.process()
            
