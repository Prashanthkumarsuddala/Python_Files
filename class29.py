a = []
while True:
    b = input('enter the number: ')
    if b == str('q'):
          break
    else:
          a.append(int(b))
print(a)
print('the sum of the numbers: ',sum(a))
print('average of numbers',(sum(a)/len(a)))
