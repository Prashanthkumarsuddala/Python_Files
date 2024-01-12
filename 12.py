#Take two int values from user and print greatest among them

a= int(input('Enter the first number: '))
b=int(input("Enter the second number: "))

if a>b:
    print('Greater number is ',a)
elif b>a:
    print('Greater number is ',b)
else:
    print('both are equal')