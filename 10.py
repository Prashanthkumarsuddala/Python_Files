#A company decided to give bonus of 5% to employee if his/her year of service is more than 5 years.
#Ask user for their salary and year of service and print the net bonus amount.

a=int(input("Enter the salary: "))
b=float(input("Enter the year of service: "))
if b>=5 :
    c=(0.05*a)
    print('You bonus is: ',c)
    print('Your total salary after adding bonus is: ',a+c)
else:
    print("The salary remain unchanged ",a)