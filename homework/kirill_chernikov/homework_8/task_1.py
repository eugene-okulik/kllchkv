#Напишите программу. Есть две переменные, salary и bonus.
# Salary - int, bonus - bool. Спросите у пользователя salary. А bonus пусть назначается рандомом.

import random

def total_salary(salary):
    bonus = bool(random.randint(0, 1))
    # альтернативно можно рандомно выбирать True / False значение:
    # seq = [True, False]
    # bonus = random.choice(seq)

    if bonus:
        salary += random.randint(0, 10000)

    return salary


user_salary = int(input('Желаемая зарплата в рублях: '))
print(total_salary(user_salary))
