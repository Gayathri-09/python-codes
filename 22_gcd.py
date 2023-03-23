class Demo:
    def __init__(self):
        pass
    def accept(self):
        self.a=int(input("enter a value"))
        self.b=int(input("enter b value"))
    def process(self):
        while self.a!=self.b:
            if self.a>self.b:
                self.a=self.a-self.b
            else:
                self.b=self.b-self.a
        print(self.a)
d=Demo()
d.accept()
d.process()
