#!/usr/local/bin/python3

# Week2 Task1
#
# Напечатайте в консоль даты: вчера, сегодня, месяц назад
# Превратите строку "01/01/17 12:10:03.234567" в объект datetime
#
# Output:
#
# Today: 2019-05-30
# Yesterday: 2019-05-29
# Month ago: 2019-04-30
# datetime: 2017-01-01 12:10:03  type: <class 'datetime.datetime'>


from datetime import date, datetime, timedelta
import dateutil.relativedelta

#1
date_now = datetime.now()
date_yesterday = (date_now - timedelta(days=1)).strftime('%Y-%m-%d')
date_month_ago = (date_now + dateutil.relativedelta.relativedelta(months=-1)).strftime('%Y-%m-%d')
date_now = datetime.today().strftime('%Y-%m-%d')

#2
my_date_string = '01/01/17 12:10:03.234567'

dt = datetime.strptime(my_date_string, "%d/%m/%y %H:%M:%S.%f")
print ('\nToday: {}\nYesterday: {}\nMonth ago: {}\ndatetime: {}  type: {}\n'.format(date_now, date_yesterday, date_month_ago, dt, type(dt)))



