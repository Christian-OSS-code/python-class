counter = 1
while counter <=3:
 counter +=1
 citizen_name =  str(input("Enter your name: "))
 amount = float(input("Enter your earnings: "))
 if amount <= 30000:
  PERCENTAGE1 = 15/100
  tax1 = PERCENTAGE1 * amount
  print("Hi!, your total tax is ", tax1)   
 elif amount > 30000:
  PERCENTAGE2 = 20/100
  tax2 = PERCENTAGE2*amount
  print("Hi!, your total tax is ", tax2);