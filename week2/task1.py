#!/usr/local/bin/python3

# Week2 Task1
#
# Напечатайте в консоль даты: вчера, сегодня, месяц назад
# Превратите строку "01/01/17 12:10:03.234567" в объект datetime

from datetime import date, datetime, timedelta
import dateutil.relativedelta

#1
date_now = datetime.now()
date_yesterday = (date_now - timedelta(days=1)).strftime('%Y-%m-%d')
date_month_ago = (date_now + dateutil.relativedelta.relativedelta(months=-1)).strftime('%Y-%m-%d')
date_now = datetime.today().strftime('%Y-%m-%d')

#2
my_date_old = '01/01/17 12:10:03.234567'
my_date_split = my_date_old.split(' ')
my_date = my_date_split[0]
my_time = my_date_split[1].split('.')[0]
my_year_split = my_date.split('/')
my_year = my_year_split[2]
my_year_new = '20'+ my_year
my_date = my_date.replace(my_year,my_year_new,1)
my_date_new = my_date + ' ' + my_time

dt = datetime.strptime(my_date_new, "%d/%m/%Y %H:%M:%S")


print ('\nToday: {}\nYesterday: {}\nMonth ago: {}\ndatetime: {}  type: {}\n'.format(date_now, date_yesterday, date_month_ago, dt, type(dt)))

