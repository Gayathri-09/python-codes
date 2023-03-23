# display numbers in given range

class DisplayNo:
    def accept(self):
        self.i=int(input("enter initial value"))
        self.f=int(input("enter final value"))
    def process(self):
        while self.f>=self.i:
            print(self.f,end=' ')
            self.f=self.f-1
d=DisplayNo()
d.accept()
d.process()
