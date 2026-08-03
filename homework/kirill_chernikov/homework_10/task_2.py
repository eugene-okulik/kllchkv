# Создайте универсальный декоратор, который будет управлять тем,
# сколько раз запускается декорируемая функция
import random


def repeat_me(func):

    def wrapper(*args, **kwargs):
        n = kwargs['count']
        for _ in range(n):
            func(*args)

    return wrapper


@repeat_me
def example(text):
    print(text)


example('print me', count=2)


@repeat_me
def example_2(x, y):
    print(x + y)


number_1, number_2 = random.randint(1, 10), random.randint(1, 10)
example_2(number_1, number_2, count=4)
