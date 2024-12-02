

import random
count = 0
correct_answer_count = 0
total_score = 0
user_response = 0

while count < 10:

    number1 = random.randint(1, 100)

    number2 = random.randint(1, 100)

    if number2 > number1:

        temporary_number = number1
        number2 = number1
        number1 = temporary_number
        print(f"what is {temporary_number} minus {number2}")
        user_response = int(input("Enter your response: "))
        if user_response == temporary_number - number2:
            correct_answer_count += 1
        count += 1
    else:
        print(f"what is {number1} minus {number2}")
        user_response = int(input("Enter your response: "))
        if user_response == number1- number2:
            correct_answer_count += 1
        count += 1
        
print(f"You got {correct_answer_count} questions")
print(f"You scored {correct_answer_count}/{count}")
     
        

