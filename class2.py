#Ask user to enter age, sex ( M or F ), marital status ( Y or N ) and then using following rules print their place of service.
#if employee is female, then she will work only in urban areas.

#if employee is a male and age is in between 20 to 40 then he may work in anywhere

#if employee is male and age is in between 40 t0 60 then he will work in urban areas only.

#And any other input of age should print "ERROR".


a = int(input('Enter the age: '))
b = str(input('enter the sex (M/F) '))
c = str(input('martial status (Y/N) '))
if b == 'M' and 20<= a <=40:
    print('He may work in anywhere')
elif b== 'M' and 40<= a <=60:
    print('He wii work in urban areas only')
elif b == "F":
    print('She will work in urban areas only')
else:
    print("ERROR")



