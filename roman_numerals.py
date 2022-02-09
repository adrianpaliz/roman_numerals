dictionary_roman_values = {
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

def arabic_to_roman(number):    
    roman = ''
    remainder = 1

    while remainder != 0:        
        for value in sorted(dictionary_roman_values.keys(), reverse = True):
            if number >= value:
                break    
        quotient = number // value
        remainder = number % value
        roman += quotient * dictionary_roman_values[value]        
        number = remainder    
    
    return roman

print(arabic_to_roman(36))