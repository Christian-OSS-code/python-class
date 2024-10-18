number = int(input("Enter number: "))
digit1 = number//10000
digit2 = (number//1000)%10
digit3 = (number//100)%10
digit4 = (number//10)%10
digit5 = (number)%10
print(digit1, "   ", digit2, "   ", digit3, "   ", digit4, "   ", digit5)