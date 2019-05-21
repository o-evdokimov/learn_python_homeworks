#!/usr/bin/python3


def get_career(age):
    prof = 'undefined'

    car = [
     ['kindergarten child', 0, 5],
     ['schoolboy', 6, 17],      
     ['highs school student', 18, 23],   
     ['job proffesional', 24, 120]
    ]
    
    item = 0
    for item in range(len(car)):
        if (age > car[item][1] and age < car[item][2]): 
       	    prof = car[item][0]
            break
   
    return prof


### Main ###

age = input('Input age:')
career = get_career(int(age))
print ('The one is',career)
