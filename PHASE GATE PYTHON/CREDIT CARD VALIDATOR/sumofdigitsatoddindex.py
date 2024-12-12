def get_creditcardcheckerexistence(card_number):
    card_number = str(card_number)   
    if len(card_number) >= 13 and len(card_number) <= 16:
        return "Length of card number is within range"
    else:
        return "Length of card number out of range"           

card_number = 4388576018402626



def get_typevisacard(card_number):
    card_number = 4388576018402626
    card_number_list = list(map(int, str(card_number)))
    card_type = ""
    for number in card_number_list:
        if card_number_list[0] == 4:
           card_type = "Visa Cards"
    return card_type


def get_typemastercard(card_number):
    card_number = 5388576018402626
    card_number_list = list(map(int, str(card_number)))
    card_type = ""
    for number in card_number_list:
        if card_number_list[0] == 5:
            card_type = "Master Card"

    return card_type



def get_typediscoverycard(card_number):
    card_number = 6388576018402626
    card_number_list = list(map(int, str(card_number)))
    card_type = ""
    for number in card_number_list:
        if card_number_list[0] == 6:
            card_type = "Discovery Card"

    return card_type



def get_typeamericanexpresscard(card_number):
    card_number = 3788576018402626
    card_number_list = list(map(int, str(card_number)))
    card_type = ""
    for number in card_number_list:
        if card_number_list[0] == 3 and card_number_list[1] == 7:
            card_type = "American Express Card"
    return card_type



def get_doubleseconddigitofcreditcard(card_number):
    card_number = 4388576018402626
    card_number_list = list(map(int, str(card_number)))
    card_number_list = card_number_list[::-1]

    new_list = []
    for count in range(1, len(card_number_list), 2):
        new_list.append(2*card_number_list[count])
    return new_list


def get_adddoubledigits(card_number):
    card_number = 4388576018402626
    card_number_list = list(map(int, str(card_number)))
    card_number_list = card_number_list[::-1]

    new_list = []
    for count in range(1, len(card_number_list), 2):
        new_list.append(2*card_number_list[count])
    new_number_list = [sum(int(digit) for digit in str(digits)) if digits >= 10 else digits for digits in new_list]
    return new_number_list



def get_sumofdigitsinprevioustest(card_number):
    card_number = 4388576018402626
    card_number_list = list(map(int, str(card_number)))
    card_number_list = card_number_list[::-1]

    new_list = []
    for count in range(1, len(card_number_list), 2):
        new_list.append(2*card_number_list[count])
    new_number_list = [sum(int(digit) for digit in str(digits)) if digits >= 10 else digits for digits in new_list]
    total_digits = sum([i for i in new_number_list])
    return total_digits
    
   


def get_sumofdigitsatoddindex(card_number):
    card_number = 4388576018402626
    card_number_list = list(map(int, str(card_number)))
    card_number_list = card_number_list[::-1]

    new_list = []
    for count in range(0, len(card_number_list), 2):
        new_list.append(card_number_list[count])
    sum_new_list = sum([i for i in new_list])
    return sum_new_list

        

def get_sumofvaluesofdigitsinlasttwotests(card_number):
    card_number = 4388576018402626
    card_number_list = list(map(int, str(card_number)))
    card_number_list = card_number_list[::-1]

    new_list1 = []
    for count in range(1, len(card_number_list), 2):
        new_list1.append(2*card_number_list[count])
    new_number_list = [sum(int(digit) for digit in str(digits)) if digits >= 10 else digits for digits in new_list1]
    total_digits = sum([i for i in new_number_list])


    new_list2 = []
    for count in range(0, len(card_number_list), 2):
        new_list2.append(card_number_list[count])
    sum_new_list = sum([i for i in new_list2])
    return total_digits + sum_new_list
        























            
