def get_sumofnumbers1(numbers:list)->int:
    sum = 0
    for element in numbers:
        sum += element
    return sum 
def get_sumofnumbers2(numbers2:list)->int:
    total = 0
    count = 0
    while count < len(numbers2):
        total += numbers2[count]
        count += 1
    return total 

def get_largestelement(number:list)->int:
    largest = number[0]
    for i in number:
        if i > largest:
            largest = i
    return largest

def get_runningtotal(number:list):
    total = 0
    for elements in number:
        total += elements
    return total

def get_palindromechecker(word:str)->bool:
    if word == word[::-1]:
        return True
    else:
        return False
def get_reversedelement(number:list)->list:
    number = number[::-1]
    return number

def get_listconcatenation(letters:list, numbers:list)->list:
    pass 






