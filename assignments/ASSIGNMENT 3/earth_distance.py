import math
first_lattitude = float(input("Enter first latitude: "))
first_longitude = float(input("Enter first longitude: "))
second_lattitude = float(input("Enter second latitude: "))
second_longitude = float(input("Enter second latitude: "))
EARTH_RADIUS = 6371.01
first_term_sinx1 = math.sin(math.radians(first_lattitude))
second_term_sinx2 = math.sin(math.radians(second_lattitude))
third_term_cosx1 = math.cos(math.radians(first_lattitude))
fourth_term_cosx2 = math.cos(math.radians(second_lattitude))
last_term = math.cos(math.radians(first_longitude) - math.radians(second_longitude)) 


distance = (EARTH_RADIUS)*math.acos((first_term_sinx1)*(second_term_sinx2) + (third_term_cosx1)*(fourth_term_cosx2)*last_term)
print(distance)
