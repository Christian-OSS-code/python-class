print("Welcome to Jessica's E-Store")
def get_viewproduct(product:list, price:list)->None:
    for element in range (len(product)):
        print(f"{element + 1}{product[element]} ${price[element]}")
def add_to_cart(cart:list, product:list, find_out:int)->None:
    new_cart_list = []
    if  find_out >= 0 and find_out <= len(product):
        cart.append(product[find_out - 1])
        new_cart_list.append(cart)
        print("Your selection has been stored")
        print(f"You added {product[find_out - 1]} to your cart")
    else:
        print("You have entered an invalid input! Please select from the list by entering a number")
def view_cart(cart:list)->None:
        if cart:
            print(cart)
        else:
            print("empty cart") 

def remove_product(cart:list, remove_prodcut:int)->None:
    if remove_product in cart:
        cart.remove(remove_product)
        print(f"you have removed {removed_product}")
    else:  
        print("You have entered an invalid input") 


def previous_menu(main_menu):
    response = int(input("Enter 1 to go back to the menu or 0 to stop: "))
    if response == 1:
            main_menu()
    
         
product = ["Laptop", "Phones", "Headphones"]
price = [1000, 500, 100] 
cart = []
try:
    main_menu = int(input("Menu:\n1. View product\n2. Add to cart\n3. Remove from cart\n4. View Cart\n5. Check out\n6. exit\n7. previous_menu"))
    match main_menu:
            case 1: 
                get_viewproduct(product, price)
            case 2: 
                get_viewproduct(product, price)
                decision = int(input("Would you like to add to your cart:? Enter 1 to continue or 0 to skip"))
                
                while decision == 1:
                    find_out = int(input("Input your product number to add to cart: "))
                    add_to_cart(cart, product, find_out)
                    decision = int(input("Would you like to add to your cart:? Enter 1 to continue or 0 to skip"))
            
                view_cart(cart)
            case 3:
                view_cart(new_cart_list) 
                number = input("enter product number: ")
                if number.isdigit():
                    remove_product_name = int(number)
                    remove_product_name(cart, remove_product_name)
                else:
                    print("The item you are trying to remove does not belong to the cart")
                    view_cart(cart)
            case 4:
                view_cart(cart)
            case 5:
                print("Let's check our cart")
                view_cart(cart)
                print("Thank you for your patronage!")
               
            case 6:
                print("Have fun!")
            case 7: previous_menu(main_menu)
               
            
except ValueError:
    print("invalid number")
       

     
                          
            
        
            





