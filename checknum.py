#check whether negative or positive number

a=int(input('Enter the number to check negative or positive: '))
if a==0:
    print(a,'it is zero')
elif a>0:
    print(a,'It is positive number')
else:
    print(a,'It is negative number')