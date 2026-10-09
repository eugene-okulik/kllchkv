import requests
import pytest
import allure

BASE_URL = 'http://objapi.course.qa-practice.com'


@pytest.fixture(scope='session')
def start_end_alert():
    print('Start testing')
    yield
    print('Testing completed')


@pytest.fixture(scope='function')
def before_after_alert():
    print('before test')
    yield
    print('after test')


@pytest.fixture(scope='function')
def object_id():
    object_id = create_obj()
    yield object_id
    clear(object_id)


@allure.feature('Тестовое API')
@allure.story('Получение данных')
@allure.title('Получение всех существующих объектов')
@allure.description('Тест получает все сущесвтующие объекты и убеждается, '
                    'что ошибок при получении не возникло')
def test_get_all_objects(start_end_alert, before_after_alert):
    response = requests.get(f'{BASE_URL}/object')

    assert response.status_code == 200, 'Статус ответа != 200'


def create_obj():
    body = {'name': 'test_data', 'data': {'data_name': 'test', 'is_valid': True}}
    response = requests.post(f'{BASE_URL}/object', json=body)
    print(response.json())

    # {'data': {'data_name': 'test', 'is_valid': True}, 'id': 3, 'name': 'test_data'}
    return response.json()['id']


def clear(obj_id):
    response = requests.delete(f'{BASE_URL}/object/{obj_id}')
    print(f'Код статуса удаления тестовой записи: {response.status_code}')


test_data = [{'name': 'test_data', 'data': {'data_name': 'test', 'is_valid': True}},
             {'name': '3', 'data': {'data_name': 'digit', 'is_valid': True}},
             {'name': '', 'data': {'data_name': 'empty_name', 'is_valid': False}}]


@allure.feature('Тестовое API')
@allure.story('Изменение данных')
@allure.title('Создание объекта')
@pytest.mark.critical
@pytest.mark.parametrize('body', test_data)
def test_create_object(before_after_alert, body):
    response = requests.post(f'{BASE_URL}/object', json=body)

    assert response.status_code == 200, 'Статус ответа != 200, не удалось создать объект'


@allure.feature('Тестовое API')
@allure.story('Получение данных')
@allure.title('Получение объекта по id')
def test_get_object_by_id(before_after_alert, object_id):
    response = requests.get(f'{BASE_URL}/object/{object_id}')

    assert response.status_code == 200, 'Статус ответа != 200'


@allure.feature('Тестовое API')
@allure.story('Изменение данных')
@allure.title('Полное обновление объекта')
def test_update_whole_object(before_after_alert, object_id):
    with allure.step('Выполнение запроса с подготовленными тестовыми данными'):
        body = {'name': 'test_data_FULL_UPDATE', 'data': {'data_name': 'test_UPDATE', 'is_valid': False}}
        response = requests.put(f'{BASE_URL}/object/{object_id}', json=body)

    with allure.step('Проверка корректности измененных данных'):
        assert response.json()['name'] == body['name'], 'Параметр "name" не обновлен'
        assert response.json()['data']['is_valid'] == body['data']['is_valid'], 'Параметр data.is_valid не обновлен'


@allure.feature('Тестовое API')
@allure.story('Изменение данных')
@allure.title('Частичное обновление объекта')
@pytest.mark.medium
def test_update_part_of_object(before_after_alert, object_id):
    body = {'name': 'test_data_PART_UPDATE'}
    response = requests.patch(f'{BASE_URL}/object/{object_id}', json=body)

    assert response.json()['name'] == body['name'], 'Параметр "name" не обновлен'


@allure.feature('Тестовое API')
@allure.story('Изменение данных')
@allure.title('Удаление объекта')
def test_delete_object(before_after_alert, object_id):
    with allure.step('Удаление объекта'):
        response = requests.delete(f'{BASE_URL}/object/{object_id}')

    with allure.step('Убеждаемся, что объект удален успешно'):
        assert response.status_code == 200, 'Статус ответа != 200, не удалось удалить запись'
