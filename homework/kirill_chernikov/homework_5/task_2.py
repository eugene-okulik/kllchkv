# Задание - нужно написать один код (который сможет работать с любым из примеров)
# и скопировать его для обработки каждой строки

txt_1 = 'результат операции: 42'
number_index_1 = txt_1.index(':')
result_1 = int(txt_1[number_index_1 + 2:]) + 10
print(result_1)


txt_2 = 'результат операции: 514'
number_index_2 = txt_2.index(':')
result_2 = int(txt_2[number_index_2 + 2:]) + 10
print(result_2)

txt_3 = 'результат работы программы: 9'
number_index_3 = txt_3.index(':')
result_3 = int(txt_3[number_index_3 + 2:]) + 10
print(result_3)
