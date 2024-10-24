#sum_of_digits_

number = int(input("Enter number: "))

digit1 = number//100

digit2 = (number//10)%10

digit3 = number%10

sum = digit1 + digit2 + digit3

print("Sum of the digits is ", sum)


