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


            