roman_values = {
    1: 'I',
    4: 'IV',
    5: 'V',
    9: 'IX',
    10: 'X',
    40: 'XL',
    50: 'L',
    90: 'XC',
    100: 'C',
    400: 'CD',
    500: 'D',
    900: 'CM',
    1000: 'M'
}

roman_symbols = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
    }

class RomanError(Exception):
    pass

def number_validation(number):
    if not isinstance(number, int):
        raise TypeError(f"{number} mush be a integer")

    if number <= 0:
        raise ValueError(f"{number} mush be a positive integer")

def arabic_to_roman(number):
    number_validation(number)  
    roman = ''
    remainder = None

    while remainder != 0:        
        for value in sorted(roman_values.keys(), reverse = True):
            if number >= value:
                break  

        quotient = number // value
        remainder = number % value
        roman += quotient * roman_values[value]        
        number = remainder    
    
    return roman

def symbol_to_value(symbol):
    try:
        return roman_symbols[symbol]
    except KeyError as error_key:
        raise RomanError(f"Syntax error. Symbol {error_key} not allowed")    

def roman_to_arabic(string):
    result = 0
    repetitions_counter = 0
    string = string.upper()
    
    for index in range(len(string) - 1):
        letter = string[index]
        next_letter = string[index + 1]
        letter_value = symbol_to_value(letter)
        next_letter_value = symbol_to_value(next_letter)
       
        # Repetitions tester
        if letter == next_letter:
            repetitions_counter += 1
        elif letter_value < next_letter_value and repetitions_counter > 0:
            raise RomanError(f"Syntax error. {letter} repetitions before subtract")
        else:
            repetitions_counter = 0
       
        print(repetitions_counter)
        if letter in 'VLD' and repetitions_counter > 0:
            raise RomanError(f"Syntax error. Too many repetitions of {letter}")        
        elif repetitions_counter > 2:
            raise RomanError(f"Syntax error. Too many repetitions of {letter}")

        if letter_value >= next_letter_value:
            #Always sum
            result += letter_value
        else:
            # Subtraction tests
            if letter in 'VLD':
                raise RomanError(f"Syntax error. {letter} can't subtract")
            elif letter == 'I' and next_letter not in ('XV'):
                raise RomanError(f"Syntax error. {letter}{next_letter} not allowed")
            elif letter == 'X' and next_letter not in ('LC'):
                raise RomanError(f"Syntax error. {letter}{next_letter} not allowed")
            elif letter == 'C' and next_letter not in ('DM'):
                raise RomanError(f"Syntax error. {letter}{next_letter} not allowed")

            result -= letter_value   
                
    result += symbol_to_value(string[-1])
    return result