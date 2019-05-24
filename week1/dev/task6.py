#!/usr/bin/python3

#Task6:

# 6.1
# Напишите функцию get_summ(num_one, num_two), которая принимает на вход два целых числа (int) и складывает их

# 6.2
# Оба аргумента нужно приводить к целому числу при помощи int() и перехватывать исключение ValueError 
# если приведение типов не сработало



def get_sum (i1, i2):
	try:
	    sum = int(i1) + int(i2)
	    print ('sum =', sum)
	except ValueError:
		print ('Error: digits are not integer !')

### Main ###

my_int1 = input('Input integer #1')
my_int2 = input('Input integer #2')
get_sum(my_int1, my_int2)
