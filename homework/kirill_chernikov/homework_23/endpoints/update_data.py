import allure
import requests

from endpoints.endpoint import Endpoint


class UpdateData(Endpoint):
    @allure.step('Обновление объекта')
    def update(self, client, object_id, body):
        # self.client = client
        self.response = client.patch(f'/object/{object_id}', json=body)

        if self.response.status_code != 200:
            print(f'Код статуса создания тестовой записи: {self.response.status_code}')
            print(f'Ответ: {self.response.text}')

            self.response.raise_for_status()

        self.response_json = self.response.json()

    def assert_param(self, body, param):
        assert self.response_json[param] == body[param], f'Параметр {param} не обновлен'

    def assert_nested_param(self, body: dict, path_to_param: str):
        # {'data': {'data_name': 'test', 'is_valid': True}, 'id': 3, 'name': 'test_data'}

        params = path_to_param.split('.')
        nested_value_response = self.response_json.copy()
        nested_value_request = body.copy()

        for param in params:
            nested_value_response = nested_value_response[param]
            nested_value_request = nested_value_request[param]

        print(nested_value_response)
        print(nested_value_request)
        assert nested_value_response == nested_value_request, f'Параметр {path_to_param} не обновлен'
