height = float(input("Enter your height in meter: "))
weight = float(input("Enter your weight in KG: "))
BMI = round((weight/ (height**2)),2)
print("Your BMI is: ", BMI, "kg/m²")
