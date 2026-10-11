import allure

from endpoints.endpoint import Endpoint


class UpdateData(Endpoint):
    @allure.step('Обновление объекта')
    def update_full(self, client, object_id, body):
        # self.client = client
        self.response = client.put(f'/object/{object_id}', json=body)

        if self.response.status_code != 200:
            print(f'Код статуса создания тестовой записи: {self.response.status_code}')
            print(f'Ответ: {self.response.text}')

            self.response.raise_for_status()

        self.response_json = self.response.json()

    @allure.step('Обновление объекта')
    def update_part(self, client, object_id, body):
        # self.client = client
        self.response = client.patch(f'/object/{object_id}', json=body)

        if self.response.status_code != 200:
            print(f'Код статуса создания тестовой записи: {self.response.status_code}')
            print(f'Ответ: {self.response.text}')

            self.response.raise_for_status()

        self.response_json = self.response.json()