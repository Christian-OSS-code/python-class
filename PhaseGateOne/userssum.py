
import random

integer1 = random.randint(1, 100)

integer2 = random.randint(1, 100)

print(f"what is {integer1} + {integer2}?")

user_sum = int(input("Enter your result: "))

if user_sum == integer1 + integer2:
    print("true")
else:
    print("false")

    print(f"The correct answer is {integer1} + {integer2}")



 



