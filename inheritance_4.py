# Hiertical Inheritance

class parent():
    def outputf(self):
        print('Iam the parent')
class child1(parent):
    def output(self):
        print('Iam the child 1')
class child2(parent):
    def output(self):
        print('Iam the child 2')

c=child1()
d=child2()
c.outputf() #child1 parent
c.output()  #child1

d.outputf() #child2 parent
d.output()  #child2
