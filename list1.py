list1=[21,35,40,25,36,15,28,50,45,46,42]
list1.append(100)
print(sorted(list1))
list1.sort(reverse=True)
print(list1)
list1.remove(45)
print(list1)
print(id(list1))

a=b=100
print(a is not b)
print(type(list1))