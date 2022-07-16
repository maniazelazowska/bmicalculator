print("enter your weight in kg")
weight = float(input("weight: "))
print("now, enter your height in centimeters")
height = float(input("height: "))
bmi = weight/(height/100)**2
print("Your BMI is:", round(bmi, 2))
if bmi <= 18.4:
    print("you are underweight! this can posess a threat to your health")
elif bmi <= 24.9:
    print("your weight is healthy! keep it up")
elif bmi <= 29.9:
    print("you are overweight! react before its too late")
else:
    print("you are obese. congratulations your health is in decay")