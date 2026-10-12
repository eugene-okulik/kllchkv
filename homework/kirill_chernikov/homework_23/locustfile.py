from locust import task, HttpUser

from endpoints.create_data import CreateData
from endpoints.delete_data import DeleteData
from endpoints.get_data import GetData
from endpoints.update_data import UpdateData


class ObjectApi(HttpUser):
    create_data = CreateData()
    delete_data = DeleteData()
    get_data = GetData()
    update_data = UpdateData()

    object_id = None

    def on_start(self):
        body = {'name': 'test_data', 'data': {'data_name': 'test', 'is_valid': True}}
        self.create_data.create(client=self.client, body=body)

        # response_json = {'data': {'data_name': 'test', 'is_valid': True}, 'id': 3, 'name': 'test_data'}
        self.object_id = self.create_data.response_json['id']
        print(f'Тестовый юзер с id={self.object_id} создан')

    def on_stop(self):
        self.delete_data.delete(client=self.client, object_id=self.object_id)
        print(f'Тестовый юзер с id={self.object_id} удален')

    @task(1)
    def get_users(self):
        self.get_data.get_all(client=self.client)

    @task(3)
    def get_user_by_id(self):
        self.get_data.get_by_id(client=self.client, object_id=self.object_id)

    @task(2)
    def full_update_user(self):
        body = {'name': 'test_data_FULL_UPDATE', 'data': {'data_name': 'test_UPDATE', 'is_valid': False}}
        self.update_data.update_full(client=self.client, object_id=self.object_id, body=body)
