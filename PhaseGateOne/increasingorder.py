

import math
number1 = int(input("Enter first number: "))

number2 = int(input("Enter second number: "))

number3 = int(input("Enter third number: "))



number4 = max(number1, number2, number3)

number5 = min(number1, number2, number3)


if number1 != number4 and number1 != number5:
    print(f"{number5}, {number1}, {number4}")


elif number2 != number4 and number2 != number5:
    print(f"{number5}, {number2}, {number4}")


elif number3 != number4 and number3 != number5:
    print(f"{number5}, {number3}, {number4}")



