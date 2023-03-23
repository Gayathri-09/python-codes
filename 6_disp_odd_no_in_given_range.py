# display odd number in given range

class DisplayOddNo:
    def __init__(self):
        self.c=1
    def accept(self):
        self.n=int(input("enter n value"))
    def process(self):
        while self.c<=self.n:
            self.r=self.c%2
            if(self.r!=0):
                print(self.c)
            self.c=self.c+1
d=DisplayOddNo()
d.accept()
d.process()
