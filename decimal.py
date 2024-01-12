import math
def calpi(num):
    a=round(math.pi,num)
    b=str(a)
    c=list(b)
    return a
d=int(input('Enter the number: '))
try:
    e=int(d)
    print('Entered number is',d,'and decimals is:', calpi(e))
except:
    print('You did not entered any number ')
