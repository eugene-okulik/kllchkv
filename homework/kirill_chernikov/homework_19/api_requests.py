import requests

BASE_URL = 'http://objapi.course.qa-practice.com'

def get_all_objects():
    response = requests.get(f'{BASE_URL}/object')
    print(response.json())

    assert response.status_code == 200, 'Статус ответа != 200'


def clear(obj_id):
    response = requests.delete(f'{BASE_URL}/object/{obj_id}')
    print(f'Код статуса удаления тестовой записи: {response.status_code}')

    assert response.status_code == 200, 'Статус ответа != 200, не удалось удалить запись'


def create_obj():
    body = {'name': 'test_data', 'data': {'data_name': 'test', 'is_valid': True}}
    response = requests.post(f'{BASE_URL}/object', json=body)
    print(response.json())

    assert response.status_code == 200, 'Статус ответа != 200, не удалось создать объект'

    # {'data': {'data_name': 'test', 'is_valid': True}, 'id': 3, 'name': 'test_data'}
    return response.json()['id']


def get_object_by_id():
    object_id = create_obj()

    response = requests.get(f'{BASE_URL}/object/{object_id}')
    print(response.json())

    clear(object_id)
    assert response.status_code == 200, 'Статус ответа != 200'


def update_whole_object():
    object_id = create_obj()

    body = {'name': 'test_data_FULL_UPDATE', 'data': {'data_name': 'test_UPDATE', 'is_valid': False}}
    response = requests.put(f'{BASE_URL}/object/{object_id}', json=body)
    print(response.json())

    clear(object_id)

    assert response.json()['name'] == body['name'], 'Параметр "name" не обновлен'
    assert response.json()['data']['is_valid'] == body['data']['is_valid'], 'Параметр data.is_valid не обновлен'


def update_part_of_object():
    object_id = create_obj()

    body = {'name': 'test_data_PART_UPDATE'}
    response = requests.patch(f'{BASE_URL}/object/{object_id}', json=body)
    print(response.json())

    clear(object_id)

    assert response.json()['name'] == body['name'], 'Параметр "name" не обновлен'


def delete_object():
    object_id = create_obj()
    response = requests.delete(f'{BASE_URL}/object/{object_id}')
    print(f'Код статуса удаления тестовой записи: {response.status_code}')

    assert response.status_code == 200, 'Статус ответа != 200, не удалось удалить запись'


get_all_objects()
get_object_by_id()
update_whole_object()
update_part_of_object()
delete_object()
