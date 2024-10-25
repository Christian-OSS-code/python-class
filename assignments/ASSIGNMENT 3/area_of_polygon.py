import math
number_of_sides = int(input("Enter number of sides: "))
length_of_sides = int(input("Enter length of sides: "))
area_of_polygon = ((number_of_sides)*(length_of_sides)**2)/(4*math.tan(3.14159/number_of_sides))
print(f"The area of the polygon is {area_of_polygon: .2f} meter square")