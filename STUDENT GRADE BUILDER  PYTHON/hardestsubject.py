

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



    

position_lists = get_studentposition(student_records)

student_score_list = get_studenttotal(student_records)


print()
print("="*80)
print("STUDENT\t\t", end = " ")
print("".join(f"SUB{i}\t" for i in range(1, len(student_scores)+ 1)), end = " ")
print("".join(f"TOTAL\tAVERAGE\tPOSITION"))
print("="*80)


for (students, scores), position in zip(student_records.items(), position_lists):

    print(f"student: {students}\t", end = " ")
    print("".join(f"{i}\t" for i in scores), end = " ")



    total_score_display = sum(scores)
    average_score_display = total_score_display/len(scores)
    print(f"{total_score_display}\t{average_score_display: .2f}\t{position}")
    
 


print("="*80)
print()



def get_highestinsubjects(student_records:dict):
    
    subject_score_lists1 = list(map(list, zip(*student_records.values())))

    highest_list = []
  
    for count, scores in enumerate(subject_score_lists1):

        highest_score = max(scores)
        highest_list.append(highest_score)
       
        
        


    return highest_list 



def get_lowestinsubjects(student_records:dict):
    subject_score_list2 = list(map(list, zip(*student_records.values())))


    lowest_list = []
    for count, scores in enumerate(subject_score_list2):
        lowest_score = min(scores)
        lowest_list.append(lowest_score)
        


    return lowest_list




def get_totalscoreinsubjects(student_records:dict):
    subject_score_lists = list(map(list, zip(*student_records.values())))



    total_list = []  
    for count, scores in enumerate(subject_score_lists):
        total_subject_scores = sum(scores)
        total_list.append(total_subject_scores )
        


    return total_list




def get_averagescoreinsubjects(student_records:dict):
    
    total_grade = get_totalscoreinsubjects(student_records)
    subject_average = 0
    subject_average_lists = []


    for count in total_grade:
        subject_average = count/len(total_grade)
        subject_average_lists.append(subject_average) 

 

    return [f"{average:.2f}" for average in subject_average_lists]



   




def get_numberofpasses(student_records:dict):
    subject_score_lists3 = list(map(list, zip(*student_records.values())))

    
    pass_list = []
   
    for count, scores in enumerate(subject_score_lists3):
        pass_list.append([i for i, score in enumerate(scores) if score >= 50])
    number_of_passes_lists = []
    for values in pass_list:
        number_of_passes_lists.append(len(values))
        
            

    return number_of_passes_lists





def get_numberoffailures(student_records:dict):

    subject_score_list = list(map(list, zip(*student_records.values())))


    failed_list = []
    for count, scores in enumerate(subject_score_list):
        failed_list.append([counter + 1 for counter, score in enumerate(scores) if score < 50])
    
    number_of_failed_list = []
    for number in failed_list:
       number_of_failed_list.append(len(number)) 

    return number_of_failed_list

            





def get_higheststudentinsubject(student_records:dict):


    maximum_score_list = get_highestinsubjects(student_records)
    subject_score_lists = list(map(list, zip(*student_records.values())))



    highest_students = []
    for count, scores in enumerate(subject_score_lists):
        

        highest_students.append([counter + 1 for counter, score in enumerate(scores) if score == maximum_score_list[count]])



    return highest_students





def get_loweststudentinsubject(student_records:dict):


    minimum_score_list = get_lowestinsubjects(student_records)
    subject_score_lists = list(map(list, zip(*student_records.values())))



    lowest_students = []
    for count, scores in enumerate(subject_score_lists):


        
        lowest_students.append([counter + 1 for counter, score in enumerate(scores) if score == minimum_score_list[count]])



    return lowest_students






def get_subjectsummary(student_records):


    subjects_offered = len(list(student_records.values())[0])

    maximum_score = get_highestinsubjects(student_records)

    maximum_student = get_higheststudentinsubject(student_records)

    minimum_score = get_lowestinsubjects(student_records)

    minimum_student = get_loweststudentinsubject(student_records)

    total_subject_score = get_totalscoreinsubjects(student_records)

    average_subject_score = get_averagescoreinsubjects(student_records)

    passed_students = get_numberofpasses(student_records)

    failed_students = get_numberoffailures(student_records)


    
    for index in range(subjects_offered):
        subject_title = f"The highest in SUB{index + 1}"



        if index < len(maximum_score):
    
            max_scores = maximum_score[index]

            max_student = maximum_student[index]

            max_scores_display = f" is student: {max_student} scoring: {max_scores}"

        if index < len(minimum_score):

            min_score = minimum_score[index]

            min_student = minimum_student[index]

            min_scores_display = f"The lowest score in SUB{index + 1} is student{min_student} scoring {min_score}"

        total_score = f"The subject total score is {total_subject_score[index]}"

        average_score = f"The subject average is {average_subject_score[index]}"

        passes = f"The number of passes is {passed_students[index]}"
        failures = f"The number of failures is {failed_students[index]}"

        
        print("="*80)
        print(f"Subject: {index + 1} Summary")
        print("="*80)

        print(f"{subject_title} {max_scores_display}\n{min_scores_display}\n{total_score}\n{average_score}\n{passes}\n{failures}")
       


get_subjectsummary(student_records)




def get_hardestsubject(student_records:dict):
    list_of_failures = get_numberoffailures(student_records)
    list_of_passes = get_numberofpasses(student_records)
    
    failures = max(list_of_failures)
    passes = len(student_records) - failures
   
    #for count, score in enumerate(list_of_failures):
    hardest_subject = [count + 1 for count, score in enumerate(list_of_failures) if score == failures]
            
   
    
    print("="*80)
    print(f"The hardest subject is SUB: {hardest_subject} with {failures} fails, {passes} passes")

    return hardest_subject 
  
print("hardest subject", get_hardestsubject(student_records))
        

list_of_failures = get_numberoffailures(student_records)
list_of_passes = get_numberofpasses(student_records)

get_hardestsubject(student_records)




            
    
    



















