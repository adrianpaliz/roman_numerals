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

inverted_dictionary_roman_values = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
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

def roman_to_arabic(string):
    result = 0
    
    for simbol in range(len(string) - 1):
        letter = string[simbol]
        next = string[simbol + 1]
        if inverted_dictionary_roman_values[letter] >= inverted_dictionary_roman_values[next]:
            result += inverted_dictionary_roman_values[letter]
        else:
            result -= inverted_dictionary_roman_values[letter]
    result += inverted_dictionary_roman_values[string[-1]]
    return result