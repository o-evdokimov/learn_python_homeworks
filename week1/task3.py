#!/usr/bin/python3

#$ ./task3.py 
#Score of class 4a = 3.8
#Score of class 4b = 2.8
#Score of class 4c = 4.4
#Score of class 4d = 3.6
#Score of class 4e = 3.8
#------------------------------
#The medium of scores in school = 3.68


### Main ###

school_classes = [
    {'school_class':'4a','scores':[3,4,5,5,2]}, 
    {'school_class':'4b','scores':[2,4,4,2,2]},   
    {'school_class':'4c','scores':[5,4,5,5,3]}, 
    {'school_class':'4d','scores':[4,4,4,2,4]}, 
    {'school_class':'4e','scores':[3,4,5,5,2]},   
]

item = {}
_sum = 0
_len = 0
for item in school_classes:
    _sum_of_class = sum(item['scores'])
    _sum_total += _sum_of_class
    _number_of_scores = len(item['scores'])
    _number_total += _number_of_scores

print ('{}{}{}{}'.format('The medium of scores in school=',_sum_total / _number_total))
