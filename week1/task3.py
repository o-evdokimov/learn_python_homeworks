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
for item in school_classes:
    _sum += sum(item['scores'])
    _len += len(item['scores'])

print ('{}{}'.format('The medium of scores in school=',_sum/_len))