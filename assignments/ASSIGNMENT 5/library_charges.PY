number_of_days = int(input("Enter number of days: "))

if number_of_days == 5:
  print("Your fine is ", 50, " paise" + " which is equivalent to ", 0.5, " rupees")

elif number_of_days >= 6 and number_of_days <= 10:
  print("Your fine is ", 1, " rupee")

elif number_of_days > 10 and number_of_days <= 30:
  print("Your fine is ", 5, " rupees")

elif number_of_days > 30:
  print("Your membership has been cancelled")
