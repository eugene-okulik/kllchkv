import allure


@allure.feature('Тестовое API')
@allure.story('Получение данных')
@allure.title('Получение всех существующих объектов')
@allure.description('Тест получает все сущесвтующие объекты и убеждается, '
                    'что ошибок при получении не возникло')
def test_get_all_objects(get_data):
    get_data.get_all()
    get_data.assert_status_200()


@allure.feature('Тестовое API')
@allure.story('Получение данных')
@allure.title('Получение объекта по id')
def test_get_object_by_id(get_data, object_id_with_cleanup):
    get_data.get_by_id(object_id_with_cleanup)
    get_data.assert_status_200()
