a=int(input('Enter the number: '))
if a%2==0:
    if a%3==0:
        print(a,'is divisible with 3 and 2')
    else:
        print(a,'is not divisible with 3 but divisible with 2')
else:
    if a%3==0:
        print(a,'is divisible with 3 but not with 2')
    else:
        print(a,'is not divisible with both 3 and 2')
        