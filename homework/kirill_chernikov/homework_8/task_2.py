# Напишите функцию-генератор, которая генерирует бесконечную последовательность чисел фибоначчи
# Распечатайте из этого списка пятое число, двухсотое число, тысячное число, стотысячное число

global_iteration_counter = 1


def fibonacci_numbers():
    numbers = [0, 1]

    while True:
        numbers.append(numbers[-1] + numbers[-2])
        yield numbers[-1]


"""
Интернеты подсказали вот такую реализацию
Решил закрепить написанием

def fibonacci_numbers():
    a, b = 1, 1
    yield a
    yield b

    while True:
        a, b = b, a + b
        yield b

iteration_counter = 0
"""

for number in fibonacci_numbers():
    global_iteration_counter += 1
    if global_iteration_counter in [5, 200, 1000, 100000]:
        print(number)

    if global_iteration_counter > 100000:
        break
