#Take 20 integer inputs from user and print the following:
#number of positive numbers
#number of negative numbers
#number of odd numbers
#number of even numbers
#number of 0s.
i = 10
a = []
while i>0:
    c = int(input('Enter the number: '))
    a.append(c)
    i = i-1
odd = 0
even =0
positive = 0
negative =0
zero = 0
i =19

while i >= 0:
    if a[i] == 0:
        zero = zero + 1
    elif a[i] > 0:
        positive = positive + 1
        if a[i] % 2 == 0:
            even = even + 1
        else:
            odd = odd + 1
    else:
        negative = negative + 1
        if a[i] % 2 == 0:
            even = even + 1
        else:
            odd = odd + 1
    i = i - 1
print("EVEN :", even, "ODD :", odd, "ZERO :", zero, "POSITIVE :", positive, "NEGATIVE :", negative)