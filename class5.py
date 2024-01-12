#Take two int values from user and print greatest among them.
num1 = int(input('enter the first value: '))
num2 = int(input('enter the second value: '))
if num1>num2:
    print('First value is greater than second value')
elif num2>num1:
    print('Second value is greater than first value')
else:
    print('Both values are equal')