# Декоратор должен распечатывать слово "finished" после выполнения декорированной функции

def add_finished(func):

    def wrapper(*args):
        func(*args)
        print('finished')

    return wrapper


@add_finished
def example_func(text, second_text):
    print(text, second_text)


example_func("I am test function.", "I test text.")
