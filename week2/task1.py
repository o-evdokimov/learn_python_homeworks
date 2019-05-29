#!/usr/local/bin/python3

from datetime import date, datetime, timedelta
import dateutil.relativedelta

date_now = datetime.now()
date_yesterday = (date_now - timedelta(days=1)).strftime('%Y-%m-%d')
date_month_ago = (date_now + dateutil.relativedelta.relativedelta(months=-1)).strftime('%Y-%m-%d')
date_now = datetime.today().strftime('%Y-%m-%d')

print ('\nToday: {}\nYesterday: {}\nMonth ago: {}\n'.format(date_now, date_yesterday, date_month_ago))

