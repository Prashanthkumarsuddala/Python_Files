class father(): #father class
    def output(self):
        print('This is father class')
class child1(father): #child class
    def outputc1(self):
        print('This is child 1')
class child2(father):  #child class
    def outputc2(self):
        print('This is child 2')
a= child1()
b= child2()
a.outputc1()
a.output()
b.outputc2()
b.output()