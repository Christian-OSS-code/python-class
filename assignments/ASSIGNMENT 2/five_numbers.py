negative_counter = 0
positive_counter = 0
zero_counter = 0
for counter in range (1, 6):
 number = int(input("Enter number: "))
 if number > 0:
  positive_counter +=1
 if number == 0:
  zero_counter +=1
 if number < 0:
  negative_counter +=1
 counter +=1
print("number of positive count is ", positive_counter)
print("number of positive count is ", zero_counter)
print("number of positive count is ", negative_counter)

