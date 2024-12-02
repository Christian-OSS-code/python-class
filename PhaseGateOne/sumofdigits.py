integer = int(input("Enter an integer between 0 and 1000: "))

remainder = 0

total = 0


while integer > 0:
 
    remainder = integer % 10

    total = total + remainder


    integer = integer//10

print(f"The sum of the digits is: {total}")

    
    

    


