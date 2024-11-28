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
    number = [str(count) for count in numbers]
    letters.extend(number)
    return letters
  
def get_elementsalternation(letters:list, numbers:list)->list:
    alternate_list = []
    length1 = len(letters)
    length2 = len(numbers)
    for index1, index2 in zip (letters, numbers):
        alternate_list.append(index1)
        alternate_list.append(index2)
    return alternate_list

def get_primenumber(number):
     counter = 0
     for element in range (1, number):
        if number % element == 0:
            counter += 1
     if counter == 1:
        return True
     else:
        return False
def get_evennumber (number):
    if number % 2 == 0:
        return True
    else:
        return False

def get_positivedifference(integer1, integer2):
    positiveDifference = 0
    if integer1 < integer2:
        temporaryInteger = integer1;
        integer1 = integer2;
        integer2 = temporaryInteger;
        positiveDifference = integer1 - integer2;
        return positiveDifference
    else:
        positiveDifference = integer1 - integer2;
        return positiveDifference; 

def get_divisionquotient(number1, number2):
    quotient = 0
    quotient = number1/number2
    if number2 == 0:
        quotient = 0
    return quotient

def get_factorsofnumber(value):
    pass 








        








 






