a = []
while True:
    b = input('enter the number or q to quit')
    if b == str('q'):
        break
    else:
        a.append(int(b))
print(a)
print('the sum of the numbers is: ',sum(a))
print('average of the numbers is: ',(sum(a)/len(a)))