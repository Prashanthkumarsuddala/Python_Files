from datetime import date

year = int(input('Enter the your of birth year: '))
month = int(input('Enter the your of birth month: '))
dates = int(input('Enter the your date of birth: '))

dateofbirth= date( year,month,dates )
print('The day of the your date of birth is: ',dateofbirth.strftime('%A'))
