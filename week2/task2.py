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

referat_str=''

with open('referat.txt', 'r', encoding = 'utf-8') as referat:
    referat_str = referat.read()

print ('len_of_string: {}'.format(len(referat_str)))