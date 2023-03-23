#10 times display
#class Display:
#constructor
#    def __init__(self):
#       i=0
#         while(i<=10):
#            print("vandhe mataram")
#            i=i+1
#d=Display()


class Display:
    def __init__(self):
        self.c=1
    def process(self):
        while self.c<=10:
            print("vandhe mataram #",self.c)
            self.c=self.c+1
d=Display()
d.process()
