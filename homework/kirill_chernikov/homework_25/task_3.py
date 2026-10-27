import pytest
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def driver():
    return webdriver.Chrome()


def test_submit_language(driver):
    """
    Напишите тест, который заходит на страницу https://www.qa-practice.com/elements/select/single_select,
    выбирает какой-нибудь вариант из Choose language, кликает Submit и проверяет, что в окошке с результатом
    отображается тот вариант, который был выбран.
    """
    wait = WebDriverWait(driver, 3)
    driver.get('https://www.qa-practice.com/elements/select/single_select')

    languages = driver.find_element(By.ID, 'id_choose_language')
    select_language = Select(languages)
    select_language.select_by_value('2')

    submit_button = driver.find_element(By.ID, 'submit-id-submit')
    submit_button.submit()

    wait.until(
        EC.presence_of_element_located((By.ID, 'result-text'))
    )

    result_text = driver.find_element(By.ID, 'result-text')

    assert result_text.text == 'Ruby'


def test_hello_world(driver):
    """
    Напишите тест, который зайдет на страницу https://the-internet.herokuapp.com/dynamic_loading/2,
    нажмет Start, и проверит, что на странице появляется текст "Hello World!"
    """
    wait = WebDriverWait(driver, 10)
    driver.get('https://the-internet.herokuapp.com/dynamic_loading/2')

    start_button = driver.find_element(By.CSS_SELECTOR, '#start button')
    start_button.click()

    wait.until(
        EC.presence_of_element_located((By.ID, 'finish'))
    )

    result = driver.find_element(By.ID, 'finish')

    assert result.text == 'Hello World!'
