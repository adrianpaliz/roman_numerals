tuple_roman_values = [    
    (1000, 'M'),
    (900, 'CM'),
    (500, 'D'),
    (400, 'CD'),
    (100, 'C'),
    (90, 'XC'),
    (50, 'L'),
    (10, 'X'),
    (9, 'IX'),
    (5, 'V'),
    (4, 'IV'),
    (1, 'I')
]

def arabic_to_roman(number):    
    roman = ''
    remainder = 1

    while remainder != 0:        
        for value, simbol in tuple_roman_values:
            if number >= value:
                break    
        quotient = number // value
        remainder = number % value
        roman += quotient * simbol         
        number = remainder    
    
    return roman

print(arabic_to_roman(36))