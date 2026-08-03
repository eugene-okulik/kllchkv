# реализация декоратора, который принимает аргументы

def repeat_me_advanced(count):
    def repeater(func):
        def wrapper(*args):
            for _ in range(count):
                func(*args)

        return wrapper
    return repeater


@repeat_me_advanced(count=3)
def example(text):
    print(text)


example('print me')
