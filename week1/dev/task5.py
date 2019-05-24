#!/usr/bin/python3

# Task:
# Перепишите функцию ask_user() из задания про while, 
# чтобы она перехватывала KeyboardInterrupt, писала пользователю "Пока!" 
# и завершала работу при помощи оператора break

def ask_user():
    answer=''
    while answer.lower() != 'good':
        try:
            answer = input('How are you?')
        except KeyboardInterrupt:
            print ('\nBye!')
            break


def ask_program():
    dialog = {
            'how are you?' : "I'm fine",
            #              ^ тут пробел нужен
            'what are you doing?' : "I'm coding",
            #                     ^ и тут пробел нужен
            'bye' : 'Ok. Bye!'
    }
    question=''
    while question.lower() != 'bye':
        question = input().lower()
        try:
            print('{}'.format(dialog[question]))
        except KeyError:
            print ("Exuse me. I don't understand you")
    

### Main ###

print('1. ask_user\n2. ask_program')

select = int(input('Select 1 or 2 ? '))

if select == 1: # лучше переносить после :
    ask_user()
elif select == 2:
    ask_program()
else:
    print ('Bye!'), exit(1)
