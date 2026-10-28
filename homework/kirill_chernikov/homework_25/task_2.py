"""
Напишите программу, которая зайдет на страницу https://demoqa.com/automation-practice-form
и полностью заполнит форму (кроме загрузки файла) и нажмет Submit.
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://demoqa.com/automation-practice-form')
wait = WebDriverWait(driver, 5)
actions = ActionChains(driver)
driver.execute_script("document.body.style.zoom = '50%'")

first_name = driver.find_element(By.ID, 'firstName')
first_name.send_keys('test')

last_name = driver.find_element(By.ID, 'lastName')
last_name.send_keys('testov')

email = driver.find_element(By.ID, 'userEmail')
email.send_keys('test@yandex.ru')

male_gender = driver.find_element(By.ID, 'gender-radio-1')
male_gender.click()

user_number = driver.find_element(By.ID, 'userNumber')
user_number.send_keys('79995553322')

date_of_birth_input = driver.find_element(By.ID, 'dateOfBirthInput')
date_of_birth_input.click()
calendar = driver.find_element(By.CLASS_NAME, 'react-datepicker-popper')

years_select = driver.find_element(By.CLASS_NAME, 'react-datepicker__year-select')
years = Select(years_select)
years.select_by_value('2002')

month_select = driver.find_element(By.CLASS_NAME, 'react-datepicker__month-select')
months = Select(month_select)
months.select_by_value('8')

days = driver.find_elements(By.CLASS_NAME, 'react-datepicker__day')
birthday_day = None
for day in days:
    if day.text == '17':
        birthday_day = day
        break

birthday_day.click()

subject_placeholder = driver.find_element(By.CLASS_NAME, 'subjects-auto-complete__value-container')
subject_placeholder.click()

subject_input = driver.find_element(By.CLASS_NAME, 'subjects-auto-complete__input')
subject_input.send_keys('A')

wait.until(
    EC.presence_of_element_located((By.CLASS_NAME, 'subjects-auto-complete__option'))
)

suggestions = driver.find_elements(By.CLASS_NAME, 'subjects-auto-complete__option')

subject = None

for suggestion in suggestions:
    if suggestion.text == 'Social Studies':
        subject = suggestion
        break

actions.scroll_to_element(subject).perform()
subject.click()

sports_hobby = driver.find_element(By.ID, 'hobbies-checkbox-1')
sports_hobby.click()
music_hobby = driver.find_element(By.ID, 'hobbies-checkbox-3')
music_hobby.click()

current_address = driver.find_element(By.ID, 'currentAddress')
current_address.send_keys('Ulitsa Testov UI')

state_listbox = driver.find_element(By.ID, 'state')
# actions.scroll_to_element(state_listbox).perform()
# actions.scroll_by_amount(0, 400).perform()

wait.until(
    EC.element_to_be_clickable((By.ID, 'state'))
)

state_listbox.click()

wait.until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, '[role="option"]'))
)

states = driver.find_elements(By.CSS_SELECTOR, '[role="option"]')

user_state = None
for state in states:
    if state.text == 'NCR':
        user_state = state
        break

actions.scroll_to_element(user_state).perform()
user_state.click()

city_listbox = driver.find_element(By.ID, 'city')
city_listbox.click()

wait.until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, '[role="option"]'))
)

cities = driver.find_elements(By.CSS_SELECTOR, '[role="option"]')
user_city = None
for city in cities:
    if city.text == 'Delhi':
        user_city = city

actions.scroll_to_element(user_city).perform()
user_city.click()

submit_button = driver.find_element(By.ID, 'submit')
submit_button.submit()

wait.until(
    EC.presence_of_element_located((By.CLASS_NAME, 'table-dark'))
)

table_elements = driver.find_element(By.TAG_NAME, 'tbody').find_elements(By.TAG_NAME, 'tr')

for idx, element in enumerate(table_elements):
    print(f'Элемент таблицы №{idx}: {element.text}')
