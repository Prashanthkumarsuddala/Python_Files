a=int(input('Enter lower number: '))
b=int(input('Enter higher number: '))

for i in range(a,b+1):
    if i>1:
        for j in range(2,i):
            if(i%j==0):
                break
        else:
            print(i)