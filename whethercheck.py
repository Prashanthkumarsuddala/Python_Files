a= int(input("What is the temperature outside: "))
if a>0 and a<30:
    print('Whether is good')
    print('You can go outside')
elif a<0 or a>30:
    print('whether is not good')
    print('You stay inside')