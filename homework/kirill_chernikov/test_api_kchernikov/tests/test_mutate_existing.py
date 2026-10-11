import allure
import pytest


@allure.feature('Тестовое API')
@allure.story('Изменение данных')
@allure.title('Полное обновление объекта')
def test_update_whole_object(object_id_with_cleanup, update_data):
    body = {'name': 'test_data_FULL_UPDATE', 'data': {'data_name': 'test_UPDATE', 'is_valid': False}}
    update_data.update(object_id=object_id_with_cleanup, body=body)
    update_data.assert_param(body, 'name')
    update_data.assert_nested_param(body, 'data.is_valid')


@allure.feature('Тестовое API')
@allure.story('Изменение данных')
@allure.title('Частичное обновление объекта')
@pytest.mark.medium
def test_update_part_of_object(object_id_with_cleanup, update_data):
    body = {'name': 'test_data_PART_UPDATE'}
    update_data.update(object_id=object_id_with_cleanup, body=body)
    update_data.assert_param(body, 'name')


@allure.feature('Тестовое API')
@allure.story('Изменение данных')
@allure.title('Удаление объекта')
def test_delete_object(delete_data, object_id_with_cleanup):
    delete_data.delete(object_id_with_cleanup)
