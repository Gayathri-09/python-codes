# sum of odd numbers in given range

class DisplayOddSum:
    def __init__(self):
        self.sum=0
    def accept(self):
        self.i=int(input("enter inital value"))
        self.f=int(input("enter final value"))
    def process(self):
        print("the odd numbers are")
        while self.i<=self.f:
            self.r=self.i%2
            if(self.r!=0):
                print(self.i,end=' ')
                self.sum=self.sum+self.i
            self.i=self.i+1
    def output(self):
        print("\n sum=",self.sum)
d=DisplayOddSum()
d.accept()
d.process()
d.output()
    
