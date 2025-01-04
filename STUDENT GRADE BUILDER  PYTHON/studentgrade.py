
student_count_check = True
while student_count_check:


    try:
        number_of_students = int(input("Enter number of students: "))


        if (number_of_students <= 0):
            print("Enter a non-zero or non-negative integer")


        else:
            break


    except ValueError:
        print("Invalid input. Enter only integers")



subject_count_check = True
while subject_count_check:

    try: 
        number_of_subjects = int(input("Enter number of subjects: "))



        if (number_of_subjects <= 0):
            print("Enter a non-zero or non-negative integer")        
    

        else:
            break
    

    except ValueError:
        print("Invalid input. Enter only integers")




student_records = {}
student_input_check = True


for count in range(number_of_students):
    print("student ", (count + 1))




    student_scores = []
    for counter in range(number_of_subjects):

        while (student_input_check):


                

                try:
                    scores = int(input(f"Enter score in subject{counter + 1}:"))

                    if (scores < 0):
                        print("Enter a non-negative integer")

                    else:
                        student_scores.append(scores)
                        break
                    

                except ValueError:
                    print("Invalid input. Enter only integer scores")


      

    student_records[count + 1] = student_scores

for x, score in student_records.items():
    print(f"{x}:{score}") 


 
for students, scores in student_records.items():

    print(f"student: {students}\t", end = " ")


    print("".join(f"{i}\t" for i in scores))




def get_studentgrade(student_records:list)->int:
    total = 0

    for students, scores in student_records.items():

        for score in scores:

            total += score
    return total
   

def get_studenttotal(student_scores:list)->int:

    student_total = 0
    
    total_list = []

    for scores in student_scores:

        student_total += scores

        total_list.append(student_total)

    return total_list


print(get_studenttotal(student_scores))



















     
