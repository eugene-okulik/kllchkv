# Напишите программу, которая добавляет ‘ing’ в конец слов (к каждому слову)
# в тексте “Etiam tincidunt neque erat, quis molestie enim imperdiet vel. Integer urna nisl,
# facilisis vitae semper at, dignissim vitae libero” и после этого выводит получившийся текст на экран.
# Знаки препинания не должны оказаться внутри слова. Если после слова идет запятая или точка,
# этот знак препинания должен идти после того же слова, но уже преобразованного.


text = ('Etiam tincidunt neque erat, quis molestie enim imperdiet vel. Integer urna nisl, '
        'facilisis vitae semper at, dignissim vitae libero')

text_separated = text.split()

for idx, word in enumerate(text_separated):
    if word.endswith('.') or word.endswith(','):
        text_separated[idx] = word[:-1] + 'ing' + word[-1]

    else:
        text_separated[idx] = word + 'ing'

result = ' '.join(text_separated)
print(result)
