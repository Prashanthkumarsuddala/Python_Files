a = []
while True:
    b = input('Enter the value or press q to quit: ')
    if b == 'q':
        break
    else:
        a.append(int(b))
print(a)
print('the sum of numbers: ',sum(a))
print('the average of numbers: ',(sum(a)/len(a)))