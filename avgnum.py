#To Find the average of the numbers 

a= int(input('Enter number of numbers to find average: '))
i=0
sum=0
for i in range(a):
    sum1=int(input('Enter the number: '))
    sum=sum+sum1
j=sum/a
print('The Sum of the given numbers is: ',sum)
print('The average of given numbers is: ',j)



count=0
sum=0
while(count<10):
    b=int(input('Enter the number: '))
    count=count+1
    sum=sum+b
avg=sum/10
print('The sum of numbers is: ',sum)
print('The average of numbers is: ',avg)
    