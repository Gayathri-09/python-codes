# number of digits in given number

class Demo:
    def __init__(self):
        self.c=0
    def accept(self):
        self.n=int(input("enter n value"))
        self.num=self.n
    def process(self):
        while self.n>0:
            self.c=self.c+1
            self.n=self.n//10
        print("no of digits of {} is {}".format(self.num,self.c))
d=Demo()
d.accept()
d.process()
