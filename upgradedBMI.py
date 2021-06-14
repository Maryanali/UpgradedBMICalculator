#!/usr/bin/env python3

#upgraded BMI calculator & to give the corresponding interpretation 


weight= float(input("Input your weight in kg: "))
height= float(input("Input your height please in m: "))
bmi= int(weight)/ float(height) ** 2
new_bmi= round(bmi, 2)

if bmi < 18.5:
	print("You are underweight")
elif bmi > 18.5 < 25:
	print("You weight is normal")
elif bmi > 25 < 30:
	print("Your weight is overweight")
elif bmi > 30 < 35:
	print("You are obese")
else:
	print("You are clinically obese")
	
#f string:
print(f"Your BMI is {new_bmi}, your height is {height} m, your weight is {weight} kg")