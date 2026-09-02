"""Нужно прочитать файлик, который лежит в репозитории в моей папке. Здесь: homework/eugene_okulik/hw_13/data.txt

Файлик не копируйте и никуда не переносите. Напишите программу, которая читает этот файл,
находит в нём даты и делает с этими датами то, что после них написано. Опирайтесь на то, что структура каждой
строки одинакова: сначала идет номер, потом дата, потом дефис и после него текст. У вас должен получиться код,
который находит даты и для даты под номером один в коде должно быть реализовано то действие, которое написано
в файле после этой даты. Ну и так далее для каждой даты."""

# 1. 2023-11-27 20:34:13.212967 - распечатать эту дату, но на неделю позже. Должно получиться 2023-12-04 20:34:13.212967
# 2. 2023-07-15 18:25:10.121473 - распечатать какой это будет день недели
# 3. 2023-06-12 15:23:45.312167 - распечатать сколько дней назад была эта дата

import os
import datetime

base_path = os.path.dirname(__file__)
homework_path = os.path.dirname(os.path.dirname(base_path))
data_file_path = os.path.join(homework_path, 'eugene_okulik', 'hw_13', 'data.txt')


def read_file(file):
    with open(file) as f:
        for line in f.readlines():
            start_idx = line.index(' ')
            end_idx = line.index('распечатать')
            yield line[start_idx:end_idx].rstrip(' - ').lstrip(' ')


for idx, file_line in enumerate(read_file(data_file_path)):
    python_date = datetime.datetime.strptime(file_line, '%Y-%m-%d %H:%M:%S.%f')

    if idx == 0:
        date = python_date + datetime.timedelta(weeks=1)
        print(date)

    if idx == 1:
        print(python_date.isoweekday())

    if idx == 2:
        time_passed = datetime.datetime.now() - python_date
        print(time_passed.days)
