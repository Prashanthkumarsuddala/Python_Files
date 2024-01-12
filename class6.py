#A shop will give discount of 10% if the cost of purchased quantity is more than 1000.
#Ask user for quantity
#Suppose, one unit will cost 100.
#Judge and print total cost for user.

user = int(input('Enter the quantity: '))
cost = user*100
if cost>1000:
    print('The 10% discount earned on the quantity is: ', cost*0.1)
    print('The total cost for user: ', cost*1.1)
else:
    print('Your not eligible for discount')