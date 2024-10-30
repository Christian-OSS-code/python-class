decision = "yes"
number1 = int(input("Enter first number: "))
number2 = int(input("Enter second number: "))
sum = number1 + number2
print("The sum is ", sum)
more_trials = str(input("Would you like to continue? enter yes to continue or no to stop: "))
while decision == "yes":
 if decision == "yes": 
  number1 = int(input("Enter first number: "))
  number2 = int(input("Enter second number: "))
  sum = number1 + number2
  print("The sum is ", sum)
 else:
  print("Your program has been aborted")
  print("The sum is ", sum)
  more_trials = str(input("Would you like to continue? enter yes to continue or no to  stop: "))
 
 

