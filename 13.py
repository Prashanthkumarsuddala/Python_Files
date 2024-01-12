#A shop will give discount of 10% if the cost of purchased quantity is more than 1000.
#Ask user for quantity
#Suppose, one unit will cost 100.
#Judge and print total cost for user.

a=int(input('Enter the quantity to be purchased: '))
b=100
c=(a*100)*0.1
if a>100:
    print('The price of the quantities for 10% discount is: ',c)
    print('The total cost is after discount is: ',(a*100)+c)
else:
    print('The price of the quantities without discount is: ',(a*100))
