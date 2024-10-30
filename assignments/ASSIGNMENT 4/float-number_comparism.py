#comparism_of_float_numbers
first_number = float(input("Enter first number: "))
second_number = float(input("Enter second number: "))

number1 = int(first_number*1000)
number2 = int(second_number*1000)
   
if number1 == number2:
 print(first_number, " and ", second_number, " are the same up to their third decimal place")
  
else: 
 print(first_number, " and ", second_number, " are not the same up to their third decimal place")