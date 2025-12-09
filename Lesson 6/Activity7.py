x=float(input("Enter your height in cm"))
y=float(input("Enter your weight in kg"))
BMI=y/(x/100)**2
print (BMI)
if BMI<=18.5:
    print ("You are underweight")
elif BMI<=24.9:
    print ("You are healthy")
elif BMI<=29.9:
    print ("You are overwight")
elif BMI<=39.9:
    print ("You are obese")
else:
    print ("You are veryyyy fat")