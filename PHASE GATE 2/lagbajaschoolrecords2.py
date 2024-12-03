print("You are welcome to Lagbaja School")
while True:

    student_record = {"name": [], "subject": [], "score": [], "total_score": [], "average": [], "position": []}

    name = input("Enter student name: ")
    if name.isalpha():
        print("Your name has been collected")
    else:
        print("invalid input, youn can only enter alphabets")



    subject = input("Enter student subject: ")
    if subject.isalpha():
        print("Your subject has been collected")

    else:
        print("Invalid input. You can only enter an alphabet")


    score = int(input("Enter student score from 1 to 100: "))
    if score < 0 and score > 100:
        print("Invalid input. You must enter a score between the range of 1 to 100")
    else:
        print("Your score has been collected")
        total_score = 0:
        while True:
            

     total_score = sum(student_record["score"])
        keys = ["name", "subject", "score", "total_score"]

        for key in keys:
            if key in student_record and key == "name":
                student_record[key].append(name)
            if key in student_record and key == "subject":
                student_record[key].append(subject)
            if key in student_record and key == "score":
                student_record[key].append(score)
            if key in student_record and key == "total_score":
            
                student_record[key].append(total_score)
        #if key in student_record and key == "position":
            #student_record[key].append(position)


    teacher_decision = input("Would you like to enter more students score")
    if teacher_decision != 'yes':
        print(student_record)
        break

    
     
    
    







