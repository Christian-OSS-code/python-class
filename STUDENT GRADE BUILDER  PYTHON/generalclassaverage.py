

print("\nWELCOME TO LAGBAJA INTERNATIONAL SCHOOL\n\nMOTTO:\tEDUCATION IS LIGHT🔥️💥️\n")



teacher_name = ""
teacher_name_check = True

while teacher_name_check:

        teacher_name = input("Enter tutor's name: MR/MRS/MISS \n")

        stripped_name = teacher_name.strip()

        if stripped_name.replace(" ", "").isalpha():

            arranged_name = "".join(stripped_name.split())

            break

        else:

            print("Invalid input!. Enter only alphabets\n")

            


print("\nWhat class do you teach?")



while True:

    try:

        class_name = int(input("\n1. Emerald:\n \n2. Marble:\n \n3. Gold:\n "))

        if class_name < 1 or class_name > 3:

                print("Input out of bound!")

        else: 
                                
            match class_name:

                                   
                case 1: 


                    print ("\nWelcome to Emerald Class\n\nMOTTO: We are Sensational!💥️👏️\n")
                                        

                    break

                                    

                case 2: 

        
                    print("\nWelcome to Marble Class\n\nMOTTO: We are Visionaries!🌏️💡️\n")
                                        

                    break
    
                                   

                case 3: 


                    print("\nWelcome to Gold Class\n\nMOTTO: We are the Architech of our dreams!🛠️📉️\n")
                                        


                    break


    except ValueError:

                              
        print("Invalid input!")




term_checker = True

while term_checker:

    
    try:

        term = int(input("Select the term\n\n1. AUTUM TERM: \n\n2. SPRING TERM: \n\n3. SUMMER TERM\n\n"))

        if term < 1 or term > 3:

            print("input is out of bound!\n")

        
        else:

            match term:

                case 1:

                    print("Welcome to Autum Term🍊️\n")

                    break

                case 2:

                    print("Welcome to Spring Term🌹️🌸️\n")

                    break

                case 3:

                    print("Welcome to Summer Term☀️🌝️\n")

                    break

    except ValueError:

        print("Invalid input!")
                               



student_count_check = True
while student_count_check:


    try:
        number_of_students = int(input("\nEnter number of students:\n"))


        if (number_of_students <= 0):
            print(f"Oops {teacher_name}! Enter a non-zero or non-negative integer\n")


        else:
            break


    except ValueError:
        print(f"Oops {teacher_name}! Enter only integers")





subject_count_check = True
while subject_count_check:

    try: 
        number_of_subjects = int(input("Enter number of subjects:\n"))



        if (number_of_subjects <= 0):
            print("\nOops {teacher_name}! Enter a non-zero or non-negative integer")        
    

        else:
            break
    

    except ValueError:
        print("\nOops {teacher_name}! Invalid input. Enter only integers")






student_records = {}
student_input_check = True


print("\nEnter score in subjects\n")
for count in range(number_of_students):
    print("\nstudent ", (count + 1))




    student_scores = []
    for counter in range(number_of_subjects):

        while (student_input_check):


                

                try:
                    scores = int(input(f"subject{counter + 1} score: "))

                    if scores < 0 or scores > 100:
                        print("\nEnter a non-negative integer not greater than 100")
                        
                    else:
                      
                        break
                    

                except ValueError:
                    print("\nInvalid input.\nEnter only integer scores")


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
print("\nLAGBAJA INTERNATIONAL SCHOOL RESULT ANALYSIS ")
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
print("="*80)

print("Examination cut-off mark is ", 50)



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

            max_scores_display = f" is student{max_student} scoring{max_scores}\n"

        if index < len(minimum_score):

            min_score = minimum_score[index]

            min_student = minimum_student[index]

            min_scores_display = f"The lowest score in SUB{index + 1} is student{min_student} scoring {min_score}\n"

        total_score = f"The subject total score is {total_subject_score[index]}\n"

        average_score = f"The subject average is {average_subject_score[index]}\n"

        passes = f"The number of passes is {passed_students[index]}\n"
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
   
    
    hardest_subject = [count + 1 for count, score in enumerate(list_of_failures) if score == failures]
            
   
    
    print("="*80)
    print(f"The hardest subject is SUB: {hardest_subject} with {failures} fails, {passes} passes\n")

    return hardest_subject 
  
        

list_of_failures = get_numberoffailures(student_records)
list_of_passes = get_numberofpasses(student_records)

get_hardestsubject(student_records)



def get_easiestsubject(student_records:dict):
    list_of_failures = get_numberoffailures(student_records)
    list_of_passes = get_numberofpasses(student_records)


    maximum_passes = max(list_of_passes)
    minimum_failures = len(student_records) - maximum_passes 

   
    
    easiest_subject = [count + 1 for count, score in enumerate(list_of_passes) if score == maximum_passes]
        


    print(f"The easiest subject is SUB: {easiest_subject} with {minimum_failures} fails, {maximum_passes} passes\n")


    return easiest_subject


get_easiestsubject(student_records)



def get_overallhighestsubjectscore(student_records:dict):
    subject_score_lists = list(map(list, zip(*student_records.values())))

    highest_lists = []
    highest_student_list = []
    subject_index_lists = []
    
    for index, score in enumerate(student_records.values()):
        highest_lists.append(max(score))
        if score == max(score):
            subject_index_lists.append(index)


            

    overall_highest_score = max(highest_lists)
    overall_highest_student = [count + 1 for count, grade in enumerate(highest_lists) if grade == overall_highest_score]




    for counter, scores in enumerate(highest_lists):
        if scores == max(highest_lists):
            highest_student_list.append(1 + counter)

   

    print(f"The overall highest score is scored by student {highest_student_list}")
        

    return  overall_highest_score


print("".join(f"scoring {get_overallhighestsubjectscore(student_records)}\n")) 


def get_overalllowestsubjectscore(student_records:dict):
    subject_score_lists = list(map(list, zip(*student_records.values())))

    
    lowest_lists = []
    lowest_student_lists = []


    for index, score in enumerate(student_records.values()):
        lowest_lists.append(min(score))



    overall_lowest_score = min(lowest_lists)
    overall_lowest_student = [count + 1 for count, grade in enumerate(lowest_lists) if grade == overall_lowest_score]




    for counter, scores in enumerate(lowest_lists):
        if scores == min(lowest_lists):
            lowest_student_lists.append(1 + counter)

    print(f"The overall lowest score is scored by student {overall_lowest_student}")


    return overall_lowest_score
        

    

print("".join(f"scoring {get_overalllowestsubjectscore(student_records)}\n")) 




      
print("="*80)
print()
print("CLASS SUMMARY")
print("="*80)




def get_overallbeststudent(student_records:dict):
    student_total_score = get_studenttotal(student_records)

    overall_best_score = max(student_total_score)

    overall_best_student = [count + 1 for count, score in enumerate(student_total_score) if score == overall_best_score]


    
    print(f"The Best Graduating Student is: Student{overall_best_student}", end = "")

    return overall_best_score



print("".join(f" scoring {get_overallbeststudent(student_records)}"))
print("="*80)
print()
print("!"*80)




def get_overallworststudent(student_records:dict):
    student_total_score = get_studenttotal(student_records)

    worst_student_score = min(student_total_score)

    worst_student = [counter + 1 for counter, score in enumerate(student_total_score) if score == worst_student_score]

    print(f"Worst Graduating student is student{worst_student}", end = " ")



    return worst_student_score
    



print("".join(f" scoring {get_overallworststudent(student_records)}"))
print("!"*80)
print()





def get_generalclassaverage(student_records:dict):

    overall_total = get_studentgrade(student_records)

    overall_average = overall_total/len(student_records.values())

    return overall_average




print("="*80)
print(f"Class total score is: {get_studentgrade(student_records)}")
print(f"Class average score is: {get_generalclassaverage(student_records): .2f}")
print("="*80)




print("\nCLASS SCORE BARCHART\n")
print("="*80)
print("Here is your ScoreBarChart Showing Passes and Failures in Subjects\n")
print("Subjects with 5 stars and above indicates a pass\n\nWhile Subjects with 4 stars and below indicates a fail\n\n")

def get_scorebarchat(student_records:dict, number_of_subjects:int):


    total_score_lists = get_totalscoreinsubjects(student_records)


    

    
    for index1, score_list in enumerate(student_records.values(), start = 1):

        print(f"student: {index1}\n")

        

        student_passes = 0
        
        student_failures = 0

               
        for index2, score in enumerate(score_list, start = 1):

            length_of_bar = score // 10


            bar = "*"*length_of_bar


            print(f"subject: {index2}\t", end = " ")

            print("".join(f"{bar}: {score}\t"), end = " ")

            if length_of_bar >= 5:

                print("".join(f"PASS✅️"))

                

                student_passes += 1               


            else:

                print("".join(f"FAIL❌️"))

                student_failures += 1



       


        print()

       

get_scorebarchat(student_records, number_of_subjects)

print("="*80)




def student_category_based_on_scores(student_records:dict, number_of_subjects:int):

    total_score_lists = get_studenttotal(student_records)




    high_achievers = []

    average_students = []

    below_average_students = []

    for index, score in enumerate(total_score_lists, start = 1):

        if score >= (0.75) * (100*number_of_subjects):

            high_achievers.append(index)



        elif score >= (0.5) * (100*number_of_subjects) and  score < (0.75) * (100*number_of_subjects):

            average_students.append(index)



        elif score < (0.5) * (100*number_of_subjects):

           below_average_students.append(index)



    print("STUDENT PERFORMANCE CATEGORIES\n")
    print("="*80)

    print(f"High achievers category (from 75% to 100%):\n")

    if (len(high_achievers) == 0):

            print("There is no student in this category")


    else:

        for index_high_achievers in high_achievers:

            print(f"student: {index_high_achievers}💯️")

    
    print("="*80)
    print(f"Average students category (from 50% to 74%):\n")

    if (len(average_students) == 0):

            print("There is no student in this category")


    else:


        for index_average_student in average_students:

            print(f"student: {index_average_student}")



    print("="*80)
    print(f"Below average students category (from 0% to 49%):\n")


    if (len(below_average_students) == 0):

            print("There is no student in this category")


    else:


        for index_below_average in below_average_students:

            print(f"student: {index_below_average}")


    print("="*80)

    

    
     
student_category_based_on_scores(student_records, number_of_subjects)



print("TUTOR'S PERFOMANCE EVALUATION")


print(f"Dear Mr/Mrs/Miss {teacher_name}, your scholars area of weakness is in SUB {get_hardestsubject(student_records)}.\n\nYou are advised to strategize an action plan to help them do better\n\nin their forth coming final examination")
print("="*80)

print("="*80)



            
    
    



















