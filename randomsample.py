import random

x=random.randint(1,9)
y=random.random()

mylist=['pen','pencil','book','sktech','paper']
z=random.choice(mylist)

cards=[1,2,3,4,5,6,7,8,9,0,'K','Q',"M",'N',"S"]
print(z)

c=random.shuffle(cards)
print(c)
print(cards)