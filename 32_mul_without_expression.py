# mul without using expression

class Demo():
    def __init__(self):
        self.prod=0
    def accept(self):
        self.a=int(input("enter a value"))
        self.b=int(input("enter b value"))
    def process(self):
        while self.b!=0:
            self.prod=self.prod+self.a
            self.b=self.b-1
        print(self.prod)
d=Demo()
d.accept()
d.process()

