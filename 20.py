#Python program to display the given integer in a reverse manner

num=int(input('Enter a number: '))
sum=0
while (num!=0):
    digit=num%10
    sum=(sum*10)+digit
    num=num//10
print(sum)

