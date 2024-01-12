#multilevel inheritance
class Grandfather():
    def outputg(self):
        print('Iam the Grandfather')
class parent(Grandfather):
    def output(self):
        print('Iam the parent')
class child(parent):
    def outputc(self):
        print('Iam the child')

c=child()
c.output()  #parent method
c.outputc()  #child method
c.outputg()  #grandfather method