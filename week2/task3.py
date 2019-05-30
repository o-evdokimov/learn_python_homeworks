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
# name,age,job
#
# Маша,25,Scientist
#
# Вася,8,Programmer
#
# Эдуард,48,Big boss


import csv

list_of_dicts = [
        {'name': 'Маша', 'age': 25, 'job': 'Scientist'}, 
        {'name': 'Вася', 'age': 8, 'job': 'Programmer'}, 
        {'name': 'Эдуард', 'age': 48, 'job': 'Big boss'},
]


with open ('csv_file.csv', 'w', encoding = 'utf-8') as csvfile:
    tops = ['name','age','job']
    writer = csv.DictWriter (csvfile, tops, delimiter=',')
    writer.writeheader()

    for row in list_of_dicts:
        writer.writerow(row)
