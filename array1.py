import array as arr
a=arr.array('i',[1,8,7,6,5,4,9,5,4,3])
a.reverse()
g=a.count(4)
print(a)
print(g)
b=[1,8,6,7,4,5,2,1,6,9,4]
b.sort()

print('The ascending order:',b)
b.sort(reverse=True)
print('The descending order: ',b)