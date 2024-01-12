rows=int(input('Enter the number of rows:'))
col=int(input('Enter the number of columns'))
sym=input('Enter the symbol: ')
for i in range(rows):
    for j in range(col):
        print(sym, end="")
    print()