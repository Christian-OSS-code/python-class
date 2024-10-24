
weight_in_kilograms = float(input("Enter the weight in kilograms: "))

height = float(input("Enter the height in meters: "))

body_mass_index = (weight_in_kilograms)/(height**2)
print("your body mass index is ", body_mass_index, "kilogram per meter square")

if body_mass_index < 18.5:
	print("You are underweight")

if body_mass_index >= 18.5 and body_mass_index <= 24.9:
	print("Your weight is normal")

if body_mass_index >= 25 and body_mass_index <= 29.9:
	print("You are overweight")

if body_mass_index >= 30 and body_mass_index <= 34.9:
	print("You are obesity class", 1)
if body_mass_index > 34.9:
	print("Your weight cannot be categorized. You may visit the hospital")

