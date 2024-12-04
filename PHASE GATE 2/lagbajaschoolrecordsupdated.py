def get_lagbajaschoolrecords():
    student_score_sheet = []
    number_of_students = int(input("Enter the number of students in your class: "))
    

        
    number_of_subjects = int(input("How many subjects are you offering?: "))
        

    for student in range (number_of_students):

        student_name = input("Enter your name: ")

        if student_name.isalpha():
         
            print("Your name has been collected, you may proceed to the next section")
        else:
            print("invalid input. Please, enter an alphabet")

        total_score = 0


        student_score = []

        for subject in range (1, number_of_subjects + 1):
        
            subjects = input(f"Enter subject for {student_name}: ")
        
           
            while True:
                subject_score = float(input(f"Enter score in subject: {subjects}'s Scores must be from 1 to 100: "))
                if subject_score >= 0 and subject_score <= 100:
                        print("Your score has been collected")

                        student_score.append(subject_score)
                        total_score = total_score + subject_score
                       
                        print(f"{student_name}'s total score so far is {total_score}")
                        break
                        

                       
                else:
                        print("You have entered an invalid input. Please, enter a number from 1 to 100")


            
            average_score = total_score/number_of_subjects
            
            student_score_sheet.append({"name": student_name, "subjects": subjects, "student_score": subject_score, "total_score": total_score, "average_score": average_score})
                
        print(student_score_sheet)
       
    



    print(f"average score is {average_score:.2f}")
    return total_score, student_name, subjects, average_score, student_score,       student_score_sheet
        
        

def display_function():
    total_score, student_name, subjects, average_score, student_score, student_score_sheet = get_lagbajaschoolrecords()

    score_columns = 3

    for counter in range (0, len(student_score), score_columns):
        score_row = student_score[counter:counter + score_columns]
        score_row += [""] * (score_columns - len(score_row))

    print("="*83)

    print(f"STUDENT NAME\tSUBJECT1\tSUBJECT2\tSUBJECT3\tTOTAL\tAVERAGE")

    print(f"{student_name}\t\t{score_row[0]:<10}\t{score_row[1]:<10}\t{score_row[2]:<10}\t{total_score}\t{average_score: .2f}")

    print("="*83)
    print("="*83)

display_function()
                

        



















