# Выведите на экран каждый ключ словаря столько раз сколько указано в значении

words = {'I': 3, 'love': 5, 'Python': 1, '!': 50}

for word, repeat_number in words.items():
    print(word * repeat_number)
