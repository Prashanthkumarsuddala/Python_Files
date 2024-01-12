#Write a program to print absolute vlaue of a number entered by user. E.g.-
#INPUT: 1        OUTPUT: 1
#INPUT: -1        OUTPUT: 1

a=int(input('Enter the number: '))
if a<0:
    print('The output of the number: ',a*-1)
else:
    print('The output of the number is: ',a)