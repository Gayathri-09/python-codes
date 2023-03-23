# fibanocci

class Demo:
    def __init__(self):
        self.a=0
        self.b=1
        self.c=1
    def process(self):
        while self.c<=150:
            print(self.a)
            self.c=self.a+self.b
            self.a=self.b
            self.b=self.c
        print(self.a)
d=Demo()
d.process()
