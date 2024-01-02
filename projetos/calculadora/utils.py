dot_and_number = '0123456789.'
operators = 'C◀^/*-+='

def isValidNumber(number:str) -> str:
    try:
        float(number)
        return True
    except:
        return False