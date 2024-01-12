#Write a program to check if a year is leap year or not.
#If a year is divisible by 4 then it is leap year but if the year is century year like 2000, 1900, 2100 then it must be divisible by 400.
year = int(input('enter the year to check leap year or not: '))
num = int('123456789')
century = num*100
if year%4 == 0:
    print('the entered year is leap year')
elif (century%400) == 0:
    a= print('the entered year is leap year')

else:
    print('the entered year is not leap year')



