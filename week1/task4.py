#!/usr/bin/python3

# WHILE

def ask_user():
    answer=''
    while answer.lower() != 'good':
        answer = input('How are you? ')

def ask_program():
    dialog = {
            'How are you?':"I'm fine",
            'What are you doing?':"I'm coding"
    }
    question=''
    while question.lower() != 'bye':
        try:
            question = input()
        except KeyError: 
            print ("Exuse me. I don't understand you")
        print('{}'.format(dialog[question]))
    

### Main ###

print('1. ask_user\n2. ask_program')

select = int(input('Select 1 or 2 ? '))

if select == 1: ask_user()
elif select == 2: ask_program()
else: print ('Bye!'), exit(1)
