def sum(integers):
    adding=0
    for i in integers:
        adding+=i
    return adding
integers=[69,20,40,78,45,63,55]
adding=sum(integers)
print("The addition of the input numbers is: ",adding)
print("the average of the input is: ",adding/len(integers))

def grade(marks):
    grades=[]
    for i in marks:
        if i>90:
            a=print('You grade is O',i)
        elif 90>i>75:
            a=print('You are grade is A+',i)
        elif 75>i>60:
            a=print('You are grade is A',i)
        elif 60>i>50:
            a=print('You are grade is B+',i)
        elif 50>i>40:
            a=print("You are grade is B",i)
        elif 40>i>=26:
            a=print('You are grade is C',i)
        else:
            a=print('You are grade is F, you are failed',i)


b=[22,63,56,87,44,26,21,54,45,69,74,45]
d=grade(b)
print(d)




