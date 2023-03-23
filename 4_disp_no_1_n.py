# display numbers from 1 to n

class DisplayNo:
    def __init__(self):
        self.c=1
    def accept(self):
        self.n=int(input("enter n value"))
    def process(self):
        while self.c<=self.n:
            print(self.c)
            self.c=self.c+1
d=DisplayNo()
d.accept()
d.process()
