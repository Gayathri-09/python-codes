# perfect no in given range using nested while loop

class Demo():
    def __init__(self):
        pass
    def accept(self):
        self.i=int(input("enter inital value"))
        self.f=int(input("enter final value"))
    def process(self):
        while self.i<=self.f:
            self.c=1
            self.sum=0
            while self.c<=self.i/2:
                self.r=self.i%self.c
                if self.r==0:
                    self.sum=self.sum+self.c
                self.c=self.c+1
            if self.i==self.sum:
                print(self.i)
            self.i=self.i+1
           
            
d=Demo()
d.accept()
d.process()

                
               
