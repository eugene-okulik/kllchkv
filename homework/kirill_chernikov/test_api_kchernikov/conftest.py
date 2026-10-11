import pytest

from homework.kirill_chernikov.test_api_kchernikov.endpoints.create_data import CreateData
from homework.kirill_chernikov.test_api_kchernikov.endpoints.delete_data import DeleteData
from homework.kirill_chernikov.test_api_kchernikov.endpoints.get_data import GetData
from homework.kirill_chernikov.test_api_kchernikov.endpoints.update_data import UpdateData


@pytest.fixture
def create_data():
    return CreateData()


@pytest.fixture
def get_data():
    return GetData()


@pytest.fixture
def update_data():
    return UpdateData()


@pytest.fixture
def delete_data():
    return DeleteData()


@pytest.fixture(scope='function')
def object_id_with_cleanup(create_data, delete_data):

    body = {'name': 'test_data', 'data': {'data_name': 'test', 'is_valid': True}}
    create_data.create(body=body)

    # response_json = {'data': {'data_name': 'test', 'is_valid': True}, 'id': 3, 'name': 'test_data'}
    object_id = create_data.response_json['id']
    yield object_id

    delete_data.delete(object_id=object_id)
