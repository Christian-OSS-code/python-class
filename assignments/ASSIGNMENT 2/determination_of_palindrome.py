#determination_of_palindrome

number = int(input("Enter a three digit number: "))

digit1 = number//100

digit2 = (number//10)%10

digit3 = number%10

if digit1 == digit3:
	print("The integer ", number, "is a palindrome") 
else:
	print("The integer ", number, "is not a palindrome")