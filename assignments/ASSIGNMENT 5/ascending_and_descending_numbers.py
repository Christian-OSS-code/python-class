number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))
number3 = int(input("Enter second number: "))
if number1 > number2 and number2 > number3:
 print("numbers are entered in descending order")

elif number1 < number2 and number2 < number3:
 print("numbers are entered in ascending order")
else:
 print("numbers are entered in random order")