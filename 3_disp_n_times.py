# display n number of times

#class Display:
#    def __init__(self):
#        self.n=int(input("enter n value"))
#        self.c=1
#    def process(self):
#        while self.c<=self.n:
#            print("gayathri")
#            self.c=self.c+1
#d=Display()
#d.process()

class DisplayNTimes:
    def __init__(self):
        self.c=1
    def accept(self):
        self.n=int(input("enter n value"))
    def process(self):
        while self.c<=self.n:
            print("vandhe mataram ")
            self.c=self.c+1
d=DisplayNTimes()
d.accept()
d.process()
