# nested while loop

class Demo():
    def __init__(self):
        self.i=1
    def process(self):
        while self.i<=5:
            self.j=1
            while self.j<=6:
                print(self.j,end=' ')
                self.j=self.j+1
            self.i=self.i+1
            print()
d=Demo()
d.process()
    
