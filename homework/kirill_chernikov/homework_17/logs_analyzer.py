import os
import argparse
from collections import defaultdict
import datetime
import colorama

base_homework_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

parser = argparse.ArgumentParser()
parser.add_argument('path_to_data',
                    help="При запуске скрипта путь необходимо передавать в виде строки с кавычками. "
                         r"Например, 'C:\user\data\logs'"
                    )
parser.add_argument('--text')

args = parser.parse_args()

# подстраиваю путь под запуск скрипта в рамках нашего репозитория
data_path = args.path_to_data.replace('\\', '/')
data_idx = data_path.index('data')
after_user_path = data_path[data_idx:]
file_path = str(os.path.join(base_homework_path, 'eugene_okulik/', after_user_path)).rstrip('/')


def read_file(path) -> dict[str, list]:
    with open(path, 'r') as file:
        result_with_idx = defaultdict(list)
        log_date = None

        for idx, line in enumerate(file):
            line_beginning = line[:23]
            is_date = if_data_is_datetime(line_beginning)

            if is_date:
                log_date = line_beginning
                line = line[24:]

            result_with_idx[log_date].append((idx + 1, line))

        return result_with_idx


def if_data_is_datetime(date_str: str):
    # парсер на проверку даты формата 2022-02-03 00:01:13.623
    date_format = '%Y-%m-%d %H:%M:%S.%f'

    try:
        datetime.datetime.strptime(date_str, date_format)
        return True
    except ValueError:
        return False


def open_file(path: str) -> dict[str, dict] | tuple[None, str]:
    files_map = dict()

    if os.path.isdir(path):
        files = os.listdir(path)
        files.sort()

        if not files:
            return None, "Selected directory is empty"

        for file_name in files:
            new_path = f'{path}/{file_name}'
            data = read_file(new_path)  # получаем данные в виде {'log_data': [...]}
            files_map[file_name] = data

    else:
        data = read_file(path)
        file_name = os.path.basename(path)
        files_map[file_name] = data

    return files_map


def get_text_from_data_block(data_block: list, word_to_find: str):
    """
    функция-генератор, которая:
    - получает список сырых данных
    - возвращает кусок текста + номер строки, на котором находится заданное слово
    """

    # преобразование из [(0, 'текст крупный'), (...)] в [(0, 'текст'), (0, 'крупный'), ...]
    words_with_line_nums = [(line_num, word) for line_num, line in data_block for word in line.split()]

    for idx, data_tuple in enumerate(words_with_line_nums):
        line_num, word = data_tuple

        if word == word_to_find:
            word_position = words_with_line_nums.index(data_tuple)

            start_position = word_position - 5
            if start_position < 0:
                start_position = 0

            end_position = word_position + 6
            if end_position > len(words_with_line_nums):
                end_position = len(words_with_line_nums)

            text_sample = words_with_line_nums[start_position:end_position]
            text_result_part = str(' '.join(word for _, word in text_sample))

            yield line_num, text_result_part


def text_finder(text_to_find: str, data: dict):
    """
    функция-генератор, которая проверяет наличие нужного слова в каждом блоке текста.
    - отдает данные в другой генератор
    - возвращает все куски текста и номер строки, где встретилось заданное слово
    """
    for data_block in data.values():

        for line_num, line in data_block:
            # ожидается, что data_block - массив кортежей (line_idx, line_text)
            if text_to_find in line:
                yield from get_text_from_data_block(data_block, text_to_find)
                break

            continue


def data_printer(data, file_name):
    """функция, которая печатает найденные данные в нужном формате"""
    for line_num, text_sample in data:
        colored_file_name = colorama.Fore.RED + file_name + colorama.Style.RESET_ALL
        colored_num = colorama.Fore.CYAN + f'№{line_num}' + colorama.Style.RESET_ALL
        colored_text = colorama.Fore.CYAN + text_sample + colorama.Style.RESET_ALL

        print(f'Найдено совпадение в файле {colored_file_name} на строке {colored_num}. Текст: {colored_text}')


result_dict = open_file(file_path)

for file_name, file_data in result_dict.items():
    text_rows = text_finder(args.text, file_data)
    data_printer(text_rows, file_name)
