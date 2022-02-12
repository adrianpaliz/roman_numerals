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
    
    # String = "(IV)CCCXXIX"
    # print(string[0:4]) for debugging
    if (string[0:4] == '(IV)'):
        result += 4000
        string = string[4:] # Ahora el string es CCCXXIX
    # print(string) for debugging

    for index in range(len(string) - 1):
        symbol = string[index]
        next_symbol = string[index + 1]
        symbol_value = symbol_to_value(symbol)
        next_symbol_value = symbol_to_value(next_symbol)       


        # Repetitions tester
        if symbol == next_symbol:
            repetitions_counter += 1
        elif symbol_value < next_symbol_value and repetitions_counter > 0:
            raise RomanError(f"Syntax error. {symbol} repetitions before subtract")
        else:
            repetitions_counter = 0
       
        if symbol in 'VLD' and repetitions_counter > 0:
            raise RomanError(f"Syntax error. Too many repetitions of {symbol}")        
        elif repetitions_counter > 2:
            raise RomanError(f"Syntax error. Too many repetitions of {symbol}")

        if symbol_value >= next_symbol_value:
            #Always sum
            result += symbol_value
        else:
            # Subtraction tests
            if symbol in 'VLD':
                raise RomanError(f"Syntax error. {symbol} can't subtract")
            elif symbol == 'I' and next_symbol not in ('XV'):
                raise RomanError(f"Syntax error. {symbol}{next_symbol} not allowed")
            elif symbol == 'X' and next_symbol not in ('LC'):
                raise RomanError(f"Syntax error. {symbol}{next_symbol} not allowed")
            elif symbol == 'C' and next_symbol not in ('DM'):
                raise RomanError(f"Syntax error. {symbol}{next_symbol} not allowed")

            result -= symbol_value   
                
    result += symbol_to_value(string[-1])
    return result