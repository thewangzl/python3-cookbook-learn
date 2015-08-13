#

'''
Topic:最后一个周五
'''

from datetime import datetime, timedelta

weekdays = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']

def get_previous_byday(dayname,start_date=None):
	if start_date is None:
		start_date = datetime.today()
	day_num = start_date.weekday()
	print(day_num)
	day_num_target = weekdays.index(dayname)
	days_ago = (7 + day_num - day_num_target) % 7
	if days_ago == 0:
		days_ago = 7
	target_date = start_date - timedelta(days=days_ago)
	return target_date

if __name__ == '__main__':
	print(datetime.today())
	day = get_previous_byday('Monday')
	print(day)
	day = get_previous_byday('Tuesday')
	print(day)
	day = get_previous_byday('Friday')
	print(day)