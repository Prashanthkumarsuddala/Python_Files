#Print multiplication table of 12 using recursion.


def table(n,i):
    print(n*i)
    i=i+1
    if i<=10:
        table(n,i)
table(12,1)
