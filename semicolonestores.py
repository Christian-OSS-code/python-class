print("""YOU ARE WELCOME TO SEMICOLON STORES
    MAIN BRANCH
    LOCATION: 911, HERBERT MACAULAY WAY, SABO YABA, LAGOS.
    TELEPHONE: 03293828343
    DATE: 2nd December, 2024
    OPENING AND CLOSING TIME: 8:00 am through 8 pm daily
    CASHIER'S NAME: CHRISTIAN IKWU
    CUSTOMER'S NAME: JOHN CHUKWUDI
""")
product_cart = {}

def get_semicolonstorename():
    while True:
        customer_name = input("You may enter the customer's name:\n").strip()
        if customer_name.isalpha():
            return customer_name
            
        else:
            print(f"{customer_name} is not a valid input. Pleas enter only alphabets")
def get_semicolonproduct():
    while True:
        product_purchased = input("You may enter the product purchased:\n")
        if product_purchased.isalpha():
            return product_purchased
            print(f"You have entered {product_purchased} into the cart\nYou may now proceed to enter the unit price of product")
        else:
            print(f"{product_purchased} is not a valid input. Please, enter only alphabets")

def get_semicolonprice():
    while True:
        try:
            print()
            unit_price = float(input("Enter price for unit product:\n"))
            return unit_price
            print("You have entered the cost of a unit of the product")
            
        except:
            print()
            print(f"{unit_price} is enterd incorrectly, please enter a number")

def get_semicolonquantity():
    while True:
        try:
            print("Now")
            
            quantity = int(input("Enter the quantity of product purchased:\n"))
            return quantity
        except:
            print()
            print(f"{quantity} is not a valid entery. Please, enter a number")

def get_semicoloncartstore1(): 
    customer_name = get_semicolonstorename()
    product_cart = {"product_purchased": [], "unit_price": [], "quantity": [], "product_price": []}
    while True:
        
        product_purchased = get_semicolonproduct()
        unit_price = get_semicolonprice()
        quantity = get_semicolonquantity()
        product_price = unit_price * quantity
        keys = ["product_purchased", "unit_price", "quantity", "product_price"]
        for key in keys:
            if key in product_cart and key == "product_purchased":
                product_cart[key].append(product_purchased)
            if key in product_cart and key == "unit_price":
                product_cart[key].append(unit_price)
            if key in product_cart and key == "quantity":
                product_cart[key].append(quantity) 
            if key in product_cart and key == "product_price":
                product_cart[key].append(product_price)      
       # print(product_cart)
        #product_cart["product_purchased"] = product_purchased
        #product_cart["unit_price"] = unit_price 
        #product_cart["quantity"] = quantity  
        #product_cart["price"] = price

        more_product = input("\n\nWould you like to add more product?:\n").lower()
        if more_product != 'yes':

            print()
            print(f"\n\nCustomer's name: {customer_name}\n\nHere is your product cart\n\n{product_cart}")


            sub_total_price = sum(product_cart["product_price"])

            PERCENTAGE_DISCOUNT = 0.08
            discount = (PERCENTAGE_DISCOUNT) * (sub_total_price)

            PERCENTAGE_VAT = 0.075
            valued_added_tax = (PERCENTAGE_VAT) * (sub_total_price)


            bill_total = sub_total_price - discount + valued_added_tax
            print()

            print(f"\n\nThe sub total price is #{sub_total_price: .2f}\n\nYou have a discount of #{discount: .2f}\n\nYour valued_added_tax is #{valued_added_tax: .2f}\n\nYour total bill is #{bill_total: .2f}")


            payment_type = int(input("\n\nWould you like to pay by transfer or cash:?\n\nclik 1 to pay by transfer or 0 to pay by cash:"))
        


            if payment_type == 1:

                print("\n\nHere is the account details:\nACCOUNT NAME: SEMICOLON-STORES\n\nACCOUNT NUMBER: 0034784561\n\nACCOUNT NAME: ACCESS BANK\n\nAlert well received\n\nThank you for your patronage")


            elif payment_type == 0:

                amount_paid = int(input("\n\nEnter the cash amount you want to pay: "))

                balance = amount_paid - bill_total
                    
                if balance > 0:

                    print(f"\n\nYou paid #{amount_paid}\n\nYour balance is #{balance}")


                elif balance < 0:

                        print(f"\n\nYou paid #{amount_paid} and your total bill is #{bill_total}\n\nYou are to pay a balance of #{abs(balance)} before you can take the items you purchased")
                elif balance == 0:
                

                    
                
                    print("Thank you for your patronage")

                    
        
                

                
        


            break


get_semicoloncartstore1()

            
#    print(f"customer's name: {type(customer_name)}")
#    for key, value in product_cart.items():
#        print(f"{key}:{value}")
           #customer_name = get_semicolonstorename(customer_name)
            #product_cart = get_semicoloncartstore1(product_purchased)
            #print(customer_name)
            #print(product_cart)



