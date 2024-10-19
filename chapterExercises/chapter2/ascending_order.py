number1 = float(input("Enter first number: "))
number2 = float(input("Enter second number: "))
number3 = float(input("Enter third number: "))
if(number1 > number2 and number2 > number3):
 print(number3, number2, number1)
if(number1 > number3 and number3 > number2):
 print(number2, number3, number1)
if(number2 > number1 and number1 > number3):
 print(number3, number1, number2)
if(number2 > number3 and number3 > number1):
 print(number1, number3, number2)
if(number3 > number1 and number1 > number2):
 print(number2, number1, number3)
if(number3 > number2 and number2 > number1):
 print(number1, number2, number3)