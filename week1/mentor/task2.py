#!/usr/bin/python3


def get_string_compare(str1,str2):
    # в задании довольно размыто написано, не уверен надо было проверять на isdigit (потому что строка '123' все еще строка)
    # кстати, оно упадет если в функцию явно передать не str (потому что isdigit есть только у str)
    if not (str1.isdigit()==False and str2.isdigit()==False and isinstance(str1, str) and isinstance(str2, str)): # после двоеточия у функции конечно можно не перносить каретку, но не нужно
        # кстати, почитай еще про any(), очень удобная штука для объединения условий
        return 0
    if str1 == str2:
         return 1
    if len(str1) > len(str2): 
        return 2 
    if str2 == 'learn': 
        return 3
    # задание просила вернуть None, хоть и неявно :)
    return 4

### Main ### ???

# дальше ок, но по заданию нам просто требуется модуль
# чтоьы его оттестить, можно не писать код с inputами, а просто написать несколько вызовов с разными условиями (юнит тестирование), можно даже прикрутить assert, если очень захочется
# print(get_string_compare(1, 'строка') или assert get_string_compare(1, 'строка') == 0, 'должно вернуть 0'

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
