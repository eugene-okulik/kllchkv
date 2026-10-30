from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
import selenium.webdriver.support.expected_conditions as EC


def test_new_tab():
    driver = webdriver.Chrome()
    actions = ActionChains(driver)
    wait = WebDriverWait(driver, 20)
    driver.get('http://testshop.qa-practice.com/')

    desk = driver.find_element(By.LINK_TEXT, 'Customizable Desk')
    actions.key_down(Keys.COMMAND).click(desk).key_up(Keys.COMMAND)
    actions.perform()

    tabs = driver.window_handles

    driver.switch_to.window(tabs[1])

    add_to_cart_button = driver.find_element(By.CSS_SELECTOR, '[data-animation-selector]')
    add_to_cart_button.click()

    wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '.btn.btn-secondary'))
    )

    continue_shopping_button = driver.find_element(By.CSS_SELECTOR, '.btn.btn-secondary')
    continue_shopping_button.click()

    # дожидаемся, когда появится отбивка об успешном добавлении товара в корзину
    wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '[role="alert"]'))
    )

    driver.close()
    driver.switch_to.window(tabs[0])

    cart_button = driver.find_element(By.CSS_SELECTOR, '[aria-label="Main"] [href="/shop/cart"]')
    cart_button.click()

    wait.until(
        EC.element_to_be_clickable((By.TAG_NAME, 'h6'))
    )

    item = driver.find_element(By.TAG_NAME, 'h6')
    assert item.text == 'Customizable Desk (Steel, White)'


def test_pop_up():
    driver = webdriver.Chrome()
    actions = ActionChains(driver)
    wait = WebDriverWait(driver, 20)
    driver.get('http://testshop.qa-practice.com/')

    pictures = driver.find_elements(By.CSS_SELECTOR, '.oe_product_image.position-relative')
    cart_pop_ups = driver.find_elements(By.CSS_SELECTOR, '[title="Shopping cart"]')
    items = driver.find_elements(By.CLASS_NAME, 'o_wsale_products_item_title')

    actions.move_to_element(pictures[0]).move_to_element(cart_pop_ups[0]).click()
    actions.perform()

    wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '[role="dialog"]'))
    )

    item_at_pop_up = driver.find_element(By.CSS_SELECTOR, '.product-name.product_display_name')

    assert items[0].text in item_at_pop_up.text
