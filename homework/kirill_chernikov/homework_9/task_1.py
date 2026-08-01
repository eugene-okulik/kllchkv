# Обработка даты

import datetime

date = 'Jan 15, 2023 - 12:05:33'

python_date = datetime.datetime.strptime(date, '%b %d, %Y - %H:%M:%S')
# ожидаемый вывод - January
print(python_date.strftime('%B'))

human_date = python_date.strftime('%d.%m.%Y, %H:%M')
# ожидаемый вывод - 15.01.2023, 12:05
print(human_date)


