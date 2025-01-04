
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
                      
                        break
                    

                except ValueError:
                    print("Invalid input. Enter only integer scores")


        student_scores.append(scores)       

    student_records[count + 1] = student_scores





 
for students, scores in student_records.items():

    print(f"student: {students}\t", end = " ")


    print("".join(f"{i}\t" for i in scores))




def get_studentgrade(student_records:list)->int:
    total = 0

    for students, scores in student_records.items():

        for score in scores:

            total += score
    return total
   

def get_studenttotal(student_records:list)->list:

    student_total = [sum(i) for i in student_records.values()]

    return student_total

  

print(get_studenttotal(student_records))


def get_studentaverage(student_records:list, number_of_subjects:int)->float:

    student_averages = []

    for score in student_records.values():

        student_average_score = sum(score)/number_of_subjects

        student_averages.append(float(format(student_average_score, ".2f")))

   

    return student_averages



def get_studentposition(student_records:dict):


    total_lists = get_studenttotal(student_records)
    positions = []
    
    for count, student in enumerate(student_records.values()):
        total_score = (sum(student))

        position = 1

        for counter, students in enumerate(total_lists):

            if count != counter and students > total_score:
                position += 1
        positions.append(position)
    

        

        
    
    return positions


print(get_studentposition(student_records))



    

#position_lists = get_studentposition(student_records)




    
    
        




















     
