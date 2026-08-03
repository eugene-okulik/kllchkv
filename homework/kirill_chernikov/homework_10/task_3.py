
def choose_operator(func):

    def wrapper(*args):
        a, b = args

        if a < 0 or b < 0:
            return func(a, b, operation='*')

        if a == b:
            return func(a, b, operation='+')
        elif a > b:
            return func(a, b, operation='-')
        elif a < b:
            return func(a, b, operation='/')

        return None

    return wrapper


@choose_operator
def calc(first_num, second_num, operation=None):
    if operation == '+':
        return first_num + second_num
    elif operation == '-':
        return first_num - second_num
    elif operation == '*':
        return first_num * second_num
    elif operation == '/':
        return first_num / second_num

    return None, 'Неизвестная операция, попробуйте еще раз'


num_1, num_2 = 1, -10
call_decorator = calc(num_1, num_2)
print(call_decorator)
