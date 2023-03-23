# 1+2/2!+3/3!+4/4!+----

class Demo:
    def __init__(self,n):
        self.n=n
    def accept(self,n):
        fact=1
        for i in range(1,n+1):
            fact=fact*i
        return(fact)
    def process(self):
        sum=1
        for i in range(1,self.n+1):
            sum=sum+(i/self.accept(i))
        return(sum)
n=int(input("enter n value"))
d=Demo(n)
result=d.process()
print(result)
