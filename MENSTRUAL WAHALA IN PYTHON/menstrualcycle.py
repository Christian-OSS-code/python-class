
from datetime import datetime, timedelta
from datetime import date
 
print("You are welcome to Christian's menstrual application test");

menstral_dict = []
            
def collect_user_name():
    user_name = input("Enter Your name:\n");
    if user_name.isalpha:
        print("Successful\n\n")
            
    else:
        print("Invalid input. Enter alphabets only\n")
     
        return user_name






def collect_day():
        day = int(input("Enter the day you had your last menstrual period\n"))
        if day < 0:
            print("Invalid input. Day must be greater than zero\n\n")
            
        else:
            print("Collected successful\n\n")
            return day







def collect_month():
        month = int(input("Enter the month: \n"))
        if month < 0:
            print("Invalid input. Enter a number greater than 0\n\n")
        else:
            print("Collected successfully\n\n")
            return month

    




def collect_year():
        year = int(input("Enter the year:\n"))
        if year < 0:
            print("Invalid input. Year must be greater than zero\n\n")
        else:
            print("Collected successfully\n\n")
            return year






def calculate_cycle_date():
        cycle_date = date(year, month, day)
        return cycle_date

        
day = collect_day()
month = collect_month()
year = collect_year()






def collect_cycle_length():
            cycle_length = int(input("Enter your cycle length: You may want to enter between the range (26 - 29):\n"))
            return cycle_length
        
        



 
def get_evaluatedmenstrual_cycle():
    next_period = cycle_date + timedelta(days = cycle_length)
    ovulation_date = next_period - timedelta(days = cycle_length/2)
    fertile_start = ovulation_date - timedelta(days = 2)
    fertile_end = ovulation_date + timedelta(days = 2)
    safe_start = fertile_end + timedelta(days = 1)
    safe_end = fertile_start - timedelta(days = 1)
    

    menstral_dict.append({"Date of Next Period": next_period.isoformat(),
            "Date of Fertile Start": fertile_start.isoformat(),
            "Date of Fertile End": fertile_end.isoformat(),
            "Date of Safe Start": safe_start.isoformat(),
            "Date of Safe End": safe_start.isoformat()})

    return menstral_dict

           

collect_user_name()
cycle_date = calculate_cycle_date()
cycle_length = collect_cycle_length()





def print_cycle():
    for record in menstral_dict:
        for key, value in record.items():
            print(f"{key}:\t{value}")
        print()

get_evaluatedmenstrual_cycle()




def print_header():
    for i in range (80):
        print("=", end = "")
    print()





def print_title_header():
    print("CYCLES\t\t\tCYCLE DATE")

    



def print_medical_tips_for_menstrual_cycle():

    print("\n\nYou are adviced to:\n1. Stay hydrated\n\n2. Maintain a good diet habit\n\n3. Engage in exercise\n\n4. Consult a medical practional when you notice any unsual symptons\n\n Thank you\n\n stay safe!")






def display_function():

    print_header()
    print_title_header()
    print_header()
    print_cycle()
    print_header()
    print_header()
    print_medical_tips_for_menstrual_cycle()

display_function()


    

    

        
        
        




        
        

                



                
                   

            
        











        
