print ("BMI Calculator 2.0")
weight = int(input("your weight in kg"))
height = float(input("your height in m"))
bmi = round(weight / height**2)
# to check status
if bmi<18.5:
    print ("underweight")
elif bmi<25:
    print ("normal weight")
elif bmi<30:
    print ("overweight")
else:
    print ("clinically obese")
