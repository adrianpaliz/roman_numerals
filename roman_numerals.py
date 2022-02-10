roman_values = {
    1: 'I',
    4: 'IV',
    5: 'V',
    9: 'IX',
    10: 'X',
    50: 'L',
    90: 'XC',
    100: 'C',
    400: 'CD',
    500: 'D',
    900: 'CM',
    1000: 'M'
}

inverted_roman_values = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
    }

class Roman_error(Exception):
    pass

def number_validation(number):
    if not isinstance(number, int):
        raise TypeError(f"{number} mush be a integer")
    if number <= 0:
        raise ValueError(f"{number} mush be a positive integer")

def arabic_to_roman(number):
    number_validation(number)  
    roman = ''
    remainder = 1

    while remainder != 0:        
        for value in sorted(roman_values.keys(), reverse = True):
            if number >= value:
                break    
        quotient = number // value
        remainder = number % value
        roman += quotient * roman_values[value]        
        number = remainder    
    
    return roman

def roman_to_arabic(string):
    result = 0
    repetitions_counter = 0
    
    for index in range(len(string) - 1):
        letter = string[index]
        next = string[index + 1]

        # Repetitions tester
        if letter == next:
            repetitions_counter += 1
        elif inverted_roman_values[letter] < inverted_roman_values[next] and repetitions_counter > 0:
            raise Roman_error(f"Syntax error. {letter} tree repetitions dont could subtract")
        else:
            repetitions_counter = 0
        
        if letter in 'VLD' and repetitions_counter > 0 or repetitions_counter > 2 :
            raise Roman_error(f"Syntax error. Too many repetitions of {letter}")

        if inverted_roman_values[letter] >= inverted_roman_values[next]:
            result += inverted_roman_values[letter]
        else:
            if letter in 'VLD':
                raise Roman_error(f"Syntax error. {letter} can't subtract")
            result -= inverted_roman_values[letter]    
                
    result += inverted_roman_values[string[-1]]
    return result