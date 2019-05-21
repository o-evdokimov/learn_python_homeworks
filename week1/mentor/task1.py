#!/usr/bin/python3


def get_career(age):
    prof = 'undefined'

    # не понял почему car :)
    car = [
        # если мы берем такой подход - лучше через словарь условий вида age_conditions = {'kindergarten child': (0, 5),... },
     ['kindergarten child', 0, 5],
     ['schoolboy', 6, 17],      
     # вот тут упадет в ошибку
     ['high's school student', 18, 23], 
     ['job proffesional', 24, 120]
    ]
    
    item = 0
    # зачем так сложно? можно было сразу итерировать по car
    # но я бы написал словарь условий (см. выше) и итерировал по нему - for age_group, condition in age_conditions.items(): ...
    for item in range(len(car)):
        if (age > car[item][1] and age < car[item][2]): 
            # если уж делаем через перебор в цикле - то можно сразу делать return а не break
       	    prof = car[item][0]
            break
    # а тут возвращать что нибудь стандартное если не нашли (типа 'probably dead' :)
    return prof


### Main ###

age = input('Input age:')
career = get_career(int(age))
print ('The one is',career)
