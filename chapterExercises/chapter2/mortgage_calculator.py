#mortgageCalculator
principal = float(input("Enter the principal: "))
rate = float(input("Enter the rate: "))
number_of_years = int(input("Enter the year: "))
monthly_payment = (principal)*(rate*(1 + rate)**(number_of_years))/((1 + rate)**(number_of_years) - 1)
print("The monthly payment is", monthly_payment)
 