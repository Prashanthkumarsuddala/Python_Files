def add(*arg):
    sum=0
    for i in arg:
        sum += i
    return sum

print(add(1,5,6,4,8))