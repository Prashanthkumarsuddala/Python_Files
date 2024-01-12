class grandfather(): #father class
    def output(self):
        print('This is grand father class')
class father(grandfather): #child class
    def outputc1(self):
        print('This is father')
class child(father):  #child class
    def outputc2(self):
        print('This is child')
a= child()

a.outputc1()
a.output()
a.outputc2()
