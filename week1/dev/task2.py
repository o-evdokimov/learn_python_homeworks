#!/usr/bin/python3


def get_string_compare(str1,str2):
    # не надо сравнивать с False, выражение само по себе булево
    # str1.isdigit() упадет в ошибку если там буде не строка а число
    if not (str1.isdigit()==False and str2.isdigit()==False and isinstance(str1, str) and isinstance(str2, str)): 
        # Все же лучше делать перенос строки :(
        return 0
    if str1 == str2:
        return 1
    if len(str1) > len(str2):
        return 2 
    if str2=='learn':
        return 3
    return 4
    
### Main ###

definition = [
    'Type is not STR',
    'STRINGS are equal',
    'STRINGS are different, and string #1 is longer',
    'STRINGS are different, and string #2 is "learn"',
    'You inputed two STRINGS'
]

str1 = input('\nInput str #1:')
str2 = input('Input str #2:')
str_compare = get_string_compare(str1, str2)
print('{}{} - {}\n'.format('Compare our strings:', str_compare, definition[str_compare]))
