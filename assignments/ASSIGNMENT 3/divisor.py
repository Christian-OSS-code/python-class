counter = 0
min_number = int(input("Enter min_number: "))
max_number = int(input("Enter max-number: "))
skip_number = int(input("Enter skip_number: "))
for number in range (min_number, max_number + min_number, skip_number):
 		counter +=1
print(counter)
		