#encapsulation

#wraping of variables and methods into single unit

#private __
#protected _

class demo():
    def __init__(self,a,b):
        self.__a=2  #private
        self._b=3   #protected
class demo2(demo):
    def output(self):
        print(self._b)
        #print(self.__a)

d=demo2(2,3)
d.output()

