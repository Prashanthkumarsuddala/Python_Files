#Print the following patterns using loop :
#a.
#*
#**
#***
#****

count=0
count +=1
count=count+1

count1=4
count1 -=1
count1=count1-1

print('The Value of Count is',count)
count = 5
count1 = 4


a = print()
for i in range(count):
    for j in range(i):
        print('*', end='')

    print('')

b= print()
for i in range(count1):
    for j in range(i):
        print('*', end= '')
    print('')

