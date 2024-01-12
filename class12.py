a = int(input('Enter the number'))

b = int(input('Enter the another number'))
if a %2 == 0 and b%2 == 0:
    print('the given numbers are even numbers and sum of the two numbers is: ', a+b)
elif a%2 == 1 and b%2 == 1:
    print('the given two numbers are odd numbers and sum of the two numbers are: ', a+b)
else :
    print('the two given numbers are either even or odd numbers So, we cant add the two numbers ')

