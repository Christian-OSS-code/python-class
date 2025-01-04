import numpy as np

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




def get_highestinsubjects(student_records:dict):
    
    subject_score_lists1 = list(map(list, zip(*student_records.values())))

    highest_list = []
  
    for count, scores in enumerate(subject_score_lists1):

        highest_score = max(scores)
        highest_list.append(highest_score)
       
        
        


    return highest_list 
print(get_highestinsubjects(student_records))


def get_lowestinsubjects(student_records:dict):
    subject_score_list2 = list(map(list, zip(*student_records.values())))


    lowest_list = []
    for count, scores in enumerate(subject_score_list2):
        lowest_score = min(scores)
        lowest_list.append(lowest_score)
        


    return lowest_list
print(get_lowestinsubjects(student_records))



def get_totalscoreinsubjects(student_records:dict):
    subject_score_lists = list(map(list, zip(*student_records.values())))



    total_list = []  
    for count, scores in enumerate(subject_score_lists):
        total_subject_scores = sum(scores)
        total_list.append(total_subject_scores )
        


    return total_list
print(get_totalscoreinsubjects(student_records))



def get_averagescoreinsubjects(student_records:dict):
    
    total_grade = get_totalscoreinsubjects(student_records)
    subject_average = 0
    subject_average_lists = []


    for count in total_grade:
        subject_average = count/len(total_grade)
        subject_average_lists.append(subject_average) 

 

    return [f"{average:.2f}" for average in subject_average_lists]



print(get_averagescoreinsubjects(student_records))   




def get_numberofpasses(student_records:dict):
    subject_score_lists3 = list(map(list, zip(*student_records.values())))

    
    pass_list = []
   
    for count, scores in enumerate(subject_score_lists3):
        pass_list.append([i for i, score in enumerate(scores) if score >= 50])
    number_of_passes_lists = []
    for values in pass_list:
        number_of_passes_lists.append(len(values))
        
            

    return number_of_passes_lists
print(get_numberofpasses(student_records))




def get_numberoffailures(student_records:dict):

    subject_score_list = list(map(list, zip(*student_records.values())))


    failed_list = []
    for count, scores in enumerate(subject_score_list):
        failed_list.append([counter + 1 for counter, score in enumerate(scores) if score < 50])
    
    number_of_failed_list = []
    for number in failed_list:
       number_of_failed_list.append(len(number)) 

    return number_of_failed_list

            
print(get_numberoffailures(student_records))




def get_higheststudentinsubject(student_records:dict):


    maximum_score_list = get_highestinsubjects(student_records)
    subject_score_lists = list(map(list, zip(*student_records.values())))



    highest_students = []
    for count, scores in enumerate(subject_score_lists):
        

        highest_students.append([counter + 1 for counter, score in enumerate(scores) if score == maximum_score_list[count]])



    return highest_students

print(get_higheststudentinsubject(student_records))



















