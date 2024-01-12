#A student will not be allowed to sit in exam if his/her attendence is less than 75%.
#Take following input from user
#Number of classes held
#Number of classes attended.
#And print
#percentage of class attended
#Is student is allowed to sit in exam or not.
held = int(input('Enter the Classes held: '))
attend= int(input('Enter the class attend: '))
a = (attend/held)*100
print(float(a))
if a>=75:
    print('You got required attendence percentage. You are eligible sit in the class')
else:
    print('You not got required attendence percentage. So, You are not eligible to sit in class')
