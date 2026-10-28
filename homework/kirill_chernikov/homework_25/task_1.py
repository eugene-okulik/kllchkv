"""
Задание 1
Напишите программку, которая заходит на вот эту страницу: https://www.qa-practice.com/elements/input/simple,
вводит какой-то текст в поле, делает submit , а после этого находит элемент, в котором отображается тот текст,
который был введен и рапечатывает этот текст.
"""

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://www.qa-practice.com/elements/input/simple')

text_form = driver.find_element(By.ID, 'id_text_string')
text_form.send_keys('testdata')

text_form.submit()

text_appeared = driver.find_element(By.CLASS_NAME, 'result-text')
print(text_appeared.text)
