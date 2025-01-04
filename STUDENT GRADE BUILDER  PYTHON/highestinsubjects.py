

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

                    if scores < 0 or scores > 100:
                        print("Enter a non-negative integer not greater than 100")
                        
                    else:
                      
                        break
                    

                except ValueError:
                    print("Invalid input. Enter only integer scores")


        student_scores.append(scores)       

    student_records[count + 1] = student_scores



print()
print("STUDENT\t\t", end = " ")
print("".join(f"SUB{i}\t" for i in range(1, len(student_scores)+ 1)), end = " ")
print("".join(f"TOTAL\tAVERAGE\tPOSITION"))








def get_studentgrade(student_records:list)->int:
    total = 0

    for students, scores in student_records.items():

        for score in scores:

            total += score
    return total



   

def get_studenttotal(student_records:list)->list:

    
    student_total = [sum(i) for i in student_records.values()]

    return student_total





    
def get_studentaverage(student_records:list, number_of_subjects:int)->float:

    student_averages = []
    for score in student_records.values():



        student_average_score = sum(score)/number_of_subjects
        student_averages.append(float(format(student_average_score, ".2f")))


    return student_averages






for students, scores in student_records.items():

    print(f"student: {students}\t", end = " ")
    print("".join(f"{i}\t" for i in scores), end = " ")



    total_score_display = sum(scores)
    average_score_display = total_score_display/len(scores)
    print(f"{total_score_display}\t{average_score_display: .2f}")







def get_studentposition(student_score_list:list):

    position = 1
    sorted_score_list = sorted(student_score_list, reverse = True)
    rank_dict = {}
    position = 1


    for score in sorted_score_list:



        if score not in rank_dict:
            rank_dict[score] = position
            position += 1

        else:
            position += 1



    return rank_dict

student_score_list = get_studenttotal(student_records)



def get_highestinsubjects(student_records:dict):
    
    subject_score_lists1 = list(map(list, zip(*student_records.values())))

    highest_list = []
  
    for count, scores in enumerate(subject_score_lists1):

        highest_score = max(scores)
        highest_list.append(highest_score)
       
        
        


    return highest_list 
print(get_highestinsubjects(student_records))




