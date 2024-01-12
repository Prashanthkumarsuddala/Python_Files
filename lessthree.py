def num(a,b,c):
    if a>b and a>c:
        print(a,'is greater than two numbers')
    elif b>a and b>c:
        print(b,'is greater than two numbers')
    else:
        print(c,'is greater than two numbers')
if __name__=="__main__":
    a=int(input('Enter the number 1: '))
    b=int(input('Enter the number 2: '))
    c=int(input('Enter the number 3: '))
    print(num(a,b,c))
