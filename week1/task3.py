#!/usr/bin/python3


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
_sum_total = 0
_len_total = 0
for item in school_classes:
    _sum = sum(item['scores'])
    _sum_total = _sum_total + _sum
    _len = len(item['scores'])
    _len_total = _len_total + _len
    print ('Score of class {} is {}'.format(item['school_class'],_sum/_len))

print ('-'*30)
print ('{}{}'.format('The medium of scores in school=',_sum_total/_len_total))