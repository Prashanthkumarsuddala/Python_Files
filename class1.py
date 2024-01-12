students_marks=[98,75,68,55,42,61,53,64,32,20,88,74]
c=len(students_marks)
print('The numbers of students: ',c)
b=max(students_marks)
d=min(students_marks)
print("The lower marks is: ",d)
print("The highest Marks is: ",b)
e=sum(students_marks)
print("The total marks of students: ",e)
f=round(e/c)
print("The average marks: ",f)

for x in students_marks:
    if x>90:
        print("Grade A, Marks is,x")
    elif 90>x>70:
        print("Grade B, Marks is",x)
    elif 70>x>50:
        print("Grade C, Marks is",x)
    elif 50>x>35:
        print("Grade D, Marks is",x)
    elif x<35:
        print("Fail","You got ",x)
    else:
        print("Try Again!")



