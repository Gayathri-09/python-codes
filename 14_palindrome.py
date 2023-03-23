# palindrome number

class Demo:
    def __init__(self):
        self.rev=0
    def accept(self):
        self.n=int(input("enter n value"))
        self.num=self.n
    def process(self):
        while self.num>0:
            self.r=self.num%10
            self.rev=self.rev*10+self.r
            self.num=self.num//10
        print(self.rev)
        if self.rev==self.n:
            print("palindrome")
        else:
            print("not palindrome")
d=Demo()
d.accept()
d.process()
