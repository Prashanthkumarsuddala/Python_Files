#Python program to find the average of 10 numbers using while loop

count=0
sum=0

while count<=10:
    num=int(input('Enter a number: '))
    count=count+1
    sum=sum+num

avg=sum/count
print('Average of numbers is: ',avg)
