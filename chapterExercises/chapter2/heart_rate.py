age = int(input("Enter your age: "))
maximum_heart_rate = 220 - age
target_heart_initial = 0.5*(maximum_heart_rate)
target_heart_final = 0.85*(maximum_heart_rate)
print("Your maximum heart rate is", maximum_heart_rate, "beats per minute")
print("The range of your target heart rate is from", target_heart_initial, "-", target_heart_final)