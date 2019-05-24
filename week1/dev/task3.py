#!/usr/bin/python3


#$ ./task3.py 
#Score of class 4a = 3.8
#Score of class 4b = 2.8
#Score of class 4c = 4.4
#Score of class 4d = 3.6
#Score of class 4e = 3.8
#------------------------------
#The medium of scores in school = 3.68



# FOR

### Main ###

school_classes = [
    {'school_class':'4a','scores':[3,4,5,5,2]}, 
    {'school_class':'4b','scores':[2,4,4,2,2]},   
    {'school_class':'4c','scores':[5,4,5,5,3]}, 
    {'school_class':'4d','scores':[4,4,4,2,4]}, 
    {'school_class':'4e','scores':[3,4,5,5,2]},   
]


item = {}
# зачем _? я понимаю, типа приватные переменные, но тут излишне
#_sum = 0
#_len = 0
# ^ а вот эти две перемменые можно вообще и не объявлять тут

_sum_total = 0
_len_total = 0

for item in school_classes:
    # потому что они все равно переопределяются тут
    _sum = sum(item['scores'])
    _len = len(item['scores'])

    _sum_total = _sum_total + _sum
    _len_total = _len_total + _len # а вот это можно не считать потому что len_total == len(school_classes) :)
    print ('Score of class {} = {}'.format(item['school_class'], _sum/_len))
    print ('Score of class {} = {}'.format(item['school_class'], _sum/len(school_classes)))

print ('-'*30)
print ('{}{}'.format('The medium of scores in school = ',_sum_total/_len_total))