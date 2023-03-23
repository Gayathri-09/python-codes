# armstrong

class Demo:
    def __init__(self):
        self.count=0
        self.sum=0
    def accept(self):
        self.n=int(input("enter to check armstrong or not"))
    def finddigitcount(self):
        num=self.n
        while num>0:
            self.count=self.count+1
            num=num//10
        print("power=",self.count)
        return self.count
    def power(self,b,p):
        res=1
        c=1
        while c<=p:
            res=res*b
            c=c+1
        return res
    def process(self):
        num=self.n
        p=self.finddigitcount()
        while num>0:
            r=num%10
            self.sum=self.sum+self.power(r,p)
            num=num//10
        if self.n==self.sum:
            print("armstrong")
        else:
            print("not armstrong")
        
d=Demo()
d.accept()
d.process()
