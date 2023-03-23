# number divisible by 2 and 5

class Display:
    def accept(self):
        self.n=int(input("enter n value"))
    def process(self):
        if self.n%2==0 and self.n%5==0:
            print("divisible")
        else:
            print("not divisible")
d=Display()
d.accept()
d.process()
