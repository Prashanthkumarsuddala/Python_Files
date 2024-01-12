def adding(num):
    sum=0
    for i in num:
        sum+=i
    return sum
num=[25,42,63,45,69,74,56,11,25,36,41,26]
a=adding(num)
print('The addition of input is: ',a)
print('The average of input is: ',a/len(num))

def grade(marks):
    line=[]
    for x in marks:
        if x>90:
            b=print('You got O grade',x,'Marks')
        elif 90>x>80:
            b=print('You got A+ grade',x,'Marks')
        elif 80>x>70:
            b=print('You got A grade',x,'Marks')
        elif 70>x>60:
            b=print('You got B+ grade',x,'Marks')
        elif 60>x>50:
            b=print('You got B grade',x,'Marks')
        elif 50>x>40:
            b=print('You got C grade',x,'Marks')
        else:
            print('You got F grade',x,'Marks')
grades=[5,42,63,45,69,74,56,11,25,36,41,26]
d=grade(grades)
print(d)