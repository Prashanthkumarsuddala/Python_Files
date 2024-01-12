#multiple inheritance

class father():
    def outputf(self):
        print('Iam the father')
class mother():
    def outputm(self):
        print('Iam the mother')
class child(father,mother):
    def output(self):
        print('Iam the child')

c=child()
c.outputf()
c.outputm()
c.output()