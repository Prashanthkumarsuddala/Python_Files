i = 10
a=[]
while i>10:
    print('enter the number')
    n = input()
    a.append(n)
    i = i-1
print('enter the number')
num = input()
i = 9
count = 0
while i>=0:
    if num == a[i]:
       print('yes')
       count = count+1
    i=i-1
if count == 0:
    print('no')
if num in a:
    print('yes')
else:
    print('no')
