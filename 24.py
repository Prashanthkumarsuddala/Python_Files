#Gets all the possible coordinates that can be formed by the two lists

from itertools import product

a=[1,2]
b=[3,5]

c = list(product(a,b))

for i in c:
    print(i,end=" ")