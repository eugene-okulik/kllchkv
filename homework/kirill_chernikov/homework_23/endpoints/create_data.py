import allure

from endpoints.endpoint import Endpoint


class CreateData(Endpoint):

    @allure.step('Создание нового объекта')
    def create(self, body, client):
        # self.client = client
        self.response = client.post(f'/object', json=body)

        if self.response.status_code != 200:
            print(f'Код статуса создания тестовой записи: {self.response.status_code}')
            print(f'Ответ: {self.response.text}')

            self.response.raise_for_status()

        self.response_json = self.response.json()

        return self.response_json
