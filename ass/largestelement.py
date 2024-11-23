def get_largestelement(number:list)->int:
    largest = number[0]
    for i in number:
        if i > largest:
            largest = i
    return largest
       
