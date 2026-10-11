import pytest
import allure

test_data = [{'name': 'test_data', 'data': {'data_name': 'test', 'is_valid': True}},
             {'name': '3', 'data': {'data_name': 'digit', 'is_valid': True}},
             {'name': '', 'data': {'data_name': 'empty_name', 'is_valid': False}}]


@allure.feature('Тестовое API')
@allure.story('Изменение данных')
@allure.title('Создание объекта')
@pytest.mark.critical
@pytest.mark.parametrize('body', test_data)
def test_create_object(create_data, body):
    create_data.create(body=body)
    create_data.assert_status_200()
