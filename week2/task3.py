#!/usr/local/bin/python3

# Week2 Task3
#
# Создайте список словарей:
#        [
#        {'name': 'Маша', 'age': 25, 'job': 'Scientist'}, 
#        {'name': 'Вася', 'age': 8, 'job': 'Programmer'}, 
#        {'name': 'Эдуард', 'age': 48, 'job': 'Big boss'},
#    ]
# Запишите содержимое списка словарей в файл в формате csv
#
# Output:
#
#

import csv

list_of_dicts = [
        {'name': 'Маша', 'age': 25, 'job': 'Scientist'}, 
        {'name': 'Вася', 'age': 8, 'job': 'Programmer'}, 
        {'name': 'Эдуард', 'age': 48, 'job': 'Big boss'},
]


with open ('csv_file.csv', 'w', encoding = 'utf-8') as csvfile:
    tops = ['name ','age','job']
    reader = csv.DictReader (csvfile, tops, delimiter=',')
    for row in reader:
        csvfile.write(row)
        