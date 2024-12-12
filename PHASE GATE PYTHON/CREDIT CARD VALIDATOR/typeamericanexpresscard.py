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

    new_card_number_list = []
    for count in range(1, len(card_number_list), 2):
        count = 2 * count
        new_card_number_list.append(count)
    return new_card_number_list

























            
