num=[60,48,36,24,10,78,65,80,22,11,89]
print("The Sum of the numbers is :", sum(num))
print("The average of the numbers is: ", round(sum(num)/len(num)))
print("The maximum number in list: ",max(num))
print("The minimum number in list: ",min(num))
for i in num:
    if i<=35:
        print("Your marks is : ",i,"You failed in exam")
    elif 36<=i<=50:
        print("Your marks is: ",i, "You got good marks")
    elif 50<i<80:
        print("Your marks is: ",i, "You got excellent marks")
    elif i>=80:
        print("Your marks is: ",i, "Your topper in exam")
    else:
        print("Something went wrong")

print("...ThankYou!...")

