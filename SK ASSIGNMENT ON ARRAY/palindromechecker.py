def get_palindromechecker(word:str)->bool:
    if word == word[::-1]:
        return True
    else:
        return False
            
    
        