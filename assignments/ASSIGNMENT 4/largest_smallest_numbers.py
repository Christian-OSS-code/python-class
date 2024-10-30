number = int(input("Enter number: "))

largest_number = number
smallest_number = number

while number != -1:
 
 number = int(input("Enter number: "))
 
 if number > largest_number and number != -1:
  largest_number = number
 
 elif number < smallest_number and number != -1:
  smallest_number = number

print(largest_number, " is the largest number")
print(smallest_number, " is the smalles number")

