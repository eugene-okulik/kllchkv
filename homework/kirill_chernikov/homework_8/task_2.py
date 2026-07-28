# Напишите функцию-генератор, которая генерирует бесконечную последовательность чисел фибоначчи
# Распечатайте из этого списка пятое число, двухсотое число, тысячное число, стотысячное число

global_iteration_counter = 1


def fibonacci_numbers():
    counter = 1
    numbers = [0, 1]

    while counter != 100004:
        numbers.append(numbers[-1] + numbers[-2])
        yield numbers[-1]
        counter += 1


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
    if (global_iteration_counter == 5 or global_iteration_counter == 200
            or global_iteration_counter == 1000 or global_iteration_counter == 100000):
        print(number)

    if global_iteration_counter > 100000:
        break
