class Endpoint:
    url = 'http://objapi.course.qa-practice.com'
    response = None
    response_json = None

    def assert_status_200(self):
        assert self.response.status_code == 200, 'Статус ответа != 200'

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
