#mortgageCalculator
principal = float(input("Enter the principal: "))
rate = float(input("Enter the rate: "))
number_of_years = int(input("Enter the year: "))
monthly_payment = (principal)*((rate/1200)*(1 + (rate/1200))**(number_of_years*12))/((1 + (rate/1200))**(number_of_years*12) - 1)
print("The monthly payment is", monthly_payment)
 