


product_cart = {"product_purchased": [], "quantity": [], "unit_price": [], "product_price": []}
keys = ["product_purchased", "quantity", "unit_price", "product_price"]




while True:
    customer_name = input("Enter customer's name: ").strip()
    if customer_name.isalpha():
        print("Collected successfully")
        break
    else:
        print("Invalid input. Please, enter an alphabet")





    
while True:

    cashier_name = input("\nEnter cashier's name: ").strip()
    if cashier_name.isalpha():
        print("Collected successfully")
        break
    else:
        print("Invalid input. Please, enter an alphabet")
        
    




def user_input():
    while True:
        keys = ["product_purchased", "unit_price", "quantity", "product_price"]
        product_purchased = input("\nEnter the product: ")
        if product_purchased.isalpha():
            print("Collected successfully")
        



            for key in keys:
                if key in product_cart and key == "product_purchased":
                    product_cart[key].append(product_purchased)
                   

        else:
            print("Invalid input. Please, enter an alphabet")
    




        unit_price = float(input("\nEnter unit price: "))
        print("Collected successfully")
        for key in keys:
            if key in product_cart and key == "unit_price":
                product_cart[key].append(unit_price)


    
    
        quantity = int(input("\nEnter quantity: "))
        for key in keys:
            if key in product_cart and key == "quantity":
                product_cart[key].append(quantity)
    



        product_price = unit_price * quantity
        for key in keys:
            if key in product_cart and key == "product_price":
                product_cart[key].append(product_price)




        more_product = input("\nwould you like to add more to your cart?: ").lower()
        if more_product != "yes":

            break
   
    
    return product_cart



discount = 0
valued_added_tax = 0
bill_total = 0 
sub_total_price = 0   
def calculate_subtotal_price():
    global sub_total_price
    sub_total_price = sum(product_cart["product_price"])
    return sub_total_price


sub_total_price = user_input()
calculate_subtotal_price()



def calculate_discount():
    global discount
    PERCENTAGE_DISCOUNT = 0.08
    discount = (PERCENTAGE_DISCOUNT) * (sub_total_price)
    return discount

sub_total_price = calculate_subtotal_price()
calculate_discount()





def calculate_valued_added_tax():
    global valued_added_tax
    PERCENTAGE_VAT = 0.075
    valued_added_tax = (PERCENTAGE_VAT) * (sub_total_price)
    return valued_added_tax

sub_total_price = calculate_subtotal_price()
calculate_valued_added_tax()




def calculate_bill_total():
    global bill_total 
    bill_total = sub_total_price - discount + valued_added_tax
    return bill_total



sub_total_price = calculate_subtotal_price()
discount = calculate_discount()
valued_added_tax = calculate_valued_added_tax()
calculate_bill_total()






def print_product_cart(product_cart):
    global customer_name
    global cashier_name
    print(f"\nSEMICOLON STORES\nMAIN BRANCH\nLOCATION:\t312, HERBERT MACAULY WAY, SABO YABA, LAGOS\nTEL:\t03293828343\nDate:\t4th December, 2024\nCustomer's name:\t{customer_name}\nCashier's name:\t{cashier_name} ")
    print("="*80)
    print(f"\tITEM\t\tQTY\t\tPRICE\t\tTOTAL(NGN)")
    print("-"*80)
    for i in range(len(product_cart["product_purchased"])):
        print(f"\t{product_cart["product_purchased"][i]}\t\t{product_cart["quantity"][i]}\t\t{product_cart["unit_price"][i]}\t\t{product_cart["product_price"][i]}")
    print("-"*80)






def print_payment_invoice():
    print_product_cart(product_cart)
    print(f"\t\t\t\tSub total:\t\t{sub_total_price}\n\t\t\t\tDiscount:\t\t{discount: .2f}\n\t\t\t\tVAT @7.5%:\t\t{valued_added_tax: .2f}")
    print("="*80)
    print(f"\t\t\t\tBill Total:\t\t{bill_total: .2f}")
    print("="*80)
    print(f"\tTHIS IS NOT A RECEIPT KINDLY PAY {bill_total: .2f}")
    print("="*80)
print_payment_invoice()
    





def print_receipt():
    global cashier_name
    global customer_name



    while True:
        amount = float(input("\n\nEnter amount: "))
        if amount >= bill_total:
            balance = amount - bill_total
            receipt_option = input("\nwould you like to view your recipt? click yes if you want to or no to terminate the exercise:").lower()



            if receipt_option == 'yes':
                print("\n\nHERE IS YOUR RECEIPT")
                print_product_cart(product_cart)
                print(f"\t\t\tSub total:\t{sub_total_price: .2f}\n\t\t\tDiscount:\t{discount: .2f}\n\t\t\tVAT @7.5%\t {valued_added_tax: .2f}")
                print("="*80)
                print(f"\t\t\tBill Total:\t{bill_total: .2f}")
                print(f"\t\t\tAmount Paid:\t{amount: .2f}\n\t\t\tBalance:\t{balance: .2f}")
                print("="*80)
                print(f"\tTHANK YOU FOR YOUR PATRONAGE")
                print("="*80)
                break





            else:
                print("THANK YOU FOR YOUR PATRONAGE")
                break




        else:
            print("Your bill total is: #{bill_total}. You must pay your bill total complete")
            
          

calculate_bill_total()
print_receipt()





