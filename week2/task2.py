#!/usr/local/bin/python3

# Week2 Task1
#
# Прочитайте содержимое файла в перменную, подсчитайте длинну получившейся строки
# Подсчитайте количество слов в тексте
# Замените точки в тексте на восклицательные знаки
# Сохраните результат в файл referat2.txt
#
# Output:
#
# len_of_string: 1509
# number_of_words: 159
# referat2 is created
#

referat_str=''

with open('referat.txt', 'r', encoding = 'utf-8') as referat:
    referat_str = referat.read()

print ('\nlen_of_string: {}'.format(len(referat_str)))
print ('number_of_words: {}'.format(len(referat_str.split(' '))))

referat_str = referat_str.replace ('.','!')

with open('referat2.txt', 'w', encoding = 'utf-8') as referat2:
    referat2.write(referat_str)
    print ('referat2 is created \n')
