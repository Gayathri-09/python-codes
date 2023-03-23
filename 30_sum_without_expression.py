# sum without using expression

class Demo():
    def __init__(self):
        pass
    def accept(self):
        self.a=int(input("enter a value"))
        self.b=int(input("enter b value"))
    def process(self):
        while self.b!=0:
            self.a=self.a+1
            self.b=self.b-1
        print(self.a)
d=Demo()
d.accept()
d.process()
