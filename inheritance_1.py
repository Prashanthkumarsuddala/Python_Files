class parent():
    def output(self):
        print('Iam the parent')
class child(parent):
    def outputc(self):
        print('Iam the child')

c=child()
c.output()  #parent method
c.outputc()  #child method

"""class Parent():
    def output(self):
        print('I am the parent')

class Child(Parent):
    def output(self):
        super().output()  # Call the output method of the parent class
        print('I am the child')

c = Child()
c.output()"""

