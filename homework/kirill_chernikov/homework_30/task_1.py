"""Напишите тест, который заходит на страницу https://www.apple.com/shop/buy-iphone,
кликает по iPhone 17 Pro & iPhone 17 Pro Max, в открывшемся попапе проверяет заголовок.
Перед открытием страницы включите отлавливание запроса в котором приходит информация
о товарах и измените ответ так так, чтобы iPhone 17 Pro в попапе назывался "яблокофон 17 про"
Попробуйте самостоятельно поискать сам запрос и где что нужно подменить в ответе на этот запрос.
Вам в помощь всякие онлайн отображатели json, чтобы было проще разобраться в структуре ответа.
Я обычно пользуюсь https://jsoneditoronline.org/
Ну и при проверке заголовка в попапе проверяйте, что заголовок = тому, на что вы заменили название телефона."""
import json
import re

from playwright.sync_api import Page, expect, Route


def handle_route(route: Route):
    response = route.fetch()
    body = response.json()

    for py_dict in body['body']['digitalMat']:
        if py_dict['productName'].replace('\xa0', ' ') == 'iPhone 18 Pro':
            for el in py_dict['familyTypes']:
                if el['productName'].replace('\xa0', ' ') == 'iPhone 18 Pro':
                    el['productName'] = 'яблокофон18про'
                    print('успешно поменял данные')
                    break

            break

    body = json.dumps(body)
    route.fulfill(
        response=response,
        body=body
    )


def test_req_intercept(page: Page):
    digital_mat_pattern = re.compile(r"/shop/api/digital-mat\?")
    page.route(digital_mat_pattern, handle_route)
    page.goto('https://www.apple.com/shop/buy-iphone', timeout=60000)

    iphone_pictures = page.locator('.rf-hcard-img-wrapper')
    iphone_pictures.locator('nth=1').click()

    header_phone = page.locator("[data-autom='DigitalMat-overlay-header-1-0']")
    expect(header_phone).to_have_text('яблокофон18про')
