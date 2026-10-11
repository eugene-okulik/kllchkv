class Endpoint:
    url = 'http://objapi.course.qa-practice.com'
    response = None
    response_json = None

    def assert_status_200(self):
        assert self.response.status_code == 200, 'Статус ответа != 200'
