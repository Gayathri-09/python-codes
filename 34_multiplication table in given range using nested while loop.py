# multiplication table in given range using nested while loop

'''class Demo():
    def __init__(self):
        pass
    def accept(self):
        self.i=int(input("enter inital value"))
        self.f=int(input("enter final value"))
    def process(self):
        while self.i<=self.f:
            self.c=1
            while self.c<=10:
                self.p=self.i*self.c
                print(self.i,'*',self.c,'=',self.p)
                self.c=self.c+1
            self.i=self.i+1
            print()
d=Demo()
d.accept()
d.process()'''

class Demo():
    def __init__(self,i,f):
        self.i=i
        self.f=f
    def process(self):
        while self.i<=self.f:
            self.c=1
            while self.c<=10:
                self.p=self.i*self.c
                print(self.i,'*',self.c,'=',self.p)
                self.c=self.c+1
            self.i=self.i+1
            print()
i=int(input("enter inital value"))
f=int(input("enter final value"))
d=Demo(i,f)
d.process()
