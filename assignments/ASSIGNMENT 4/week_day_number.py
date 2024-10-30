#week_day_number
number1 = int(input("Enter number: "))
number2 = number1%7

if number1%7 == 0:
 number2 = number1/7
 print(number2, " is Sunday")

elif number2 == 1:
 print(number2, " is Monday")

elif number2 == 2:
 print(number2, " is Tuesday")

elif number2 == 3:
 print(number2, " is Wednesday")
   
elif number2 == 4:
 print(number2, " is Thursday")

elif number2 == 5:
 print(number2, " is Friday")
   
elif number2 == 6:
 print(number2, " is Saturday")