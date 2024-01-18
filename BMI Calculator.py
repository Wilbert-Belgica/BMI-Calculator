print("BMI CALCULATOR:")
height = input("Enter your height in meters: ")
weight = input("Enter your weight in kilograms: ")
weight_as_int = int(weight)
height_as_float = float(height)
bmi = weight_as_int / height_as_float ** 2
bmi = weight_as_int / (height_as_float * height_as_float)
bmi_as_int = int(bmi)
bmi = int(bmi)
if bmi < 18.5:
  print(f"Your BMI is {bmi}, you are underweight.")
elif bmi < 25:
  print(f"Your BMI is {bmi}, you have a normal weight.")
elif bmi < 30:
  print(f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi < 35:
  print(f"Your BMI is {bmi}, you are obese.")
else:
  print(f"Your BMI is {bmi}, you are clinically obese.")
