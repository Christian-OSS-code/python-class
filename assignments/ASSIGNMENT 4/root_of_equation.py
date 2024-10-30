coefficient_a = int(input("Enter first coefficient: "))

coefficient_b = int(input("Enter second coefficient: "))

coefficient_c = int(input("Enter third coefficient: "))

discriminant = ((coefficient_b)*(coefficient_b)) - (4*(coefficient_a)*(coefficient_c))

root_discriminant = (discriminant)**(0.5)

first_parameter = -(coefficient_b)

root_equation1 = (first_parameter + root_discriminant )/(2*coefficient_a)

root_equation2 = (first_parameter - root_discriminant )/(2*coefficient_a)

if discriminant == 0:

 print("The roots are real and equal\n")
 print(f"first root is {root_equation1: .2f} and second root is {root_equation2: .2f}")

elif discriminant > 0:
 print("The roots are real and distinct\n");
 print(f"The root of the quadratic equation are {root_equation1: .2f} and {root_equation2: .2f}")
elif discriminant < 0:
 print("The quadratic equation has complex roots and solution contains imaginary part\n")
 print(f"The complex roots of the equation are {complex(root_equation1): .2f} and {complex(root_equation2): .2f}") 



