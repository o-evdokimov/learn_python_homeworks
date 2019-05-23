#!/usr/bin/python3

# WHILE

def ask_user():
    answer=''
    while answer != 'Good':
        answer = input('How are you?')
    

### Main ###

print('1. ask_user or 2. ask_program')

select = input('Select 1 or 2 ?')

if select == 1: ask_user()
