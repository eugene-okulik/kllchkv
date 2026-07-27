# Программа, которая не завершается, пока пользователь не угадает цифру.

import random


def guess_the_number():
    guess = random.randint(0, 9)
    number = int(input('Я загадал цифру. Угадайте какую: '))

    while guess != number:
        print('Попробуйте снова')
        number = int(input('Я загадал цифру. Угадайте какую: '))

    print('Поздравляю! Вы угадали!')


guess_the_number()
