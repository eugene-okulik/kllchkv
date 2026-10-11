import allure
import requests

from homework.kirill_chernikov.test_api_kchernikov.endpoints.endpoint import Endpoint


class UpdateData(Endpoint):
    @allure.step('Полное обновление объекта')
    def update_full(self, object_id, body):
        self.response = requests.put(f'{self.url}/object/{object_id}', json=body)
        if self.response.status_code != 200:
            print(f'Код статуса создания тестовой записи: {self.response.status_code}')
            print(f'Ответ: {self.response.text}')

            self.response.raise_for_status()

        self.response_json = self.response.json()

    @allure.step('Частичное обновление объекта')
    def update_part(self, object_id, body):
        self.response = requests.patch(f'{self.url}/object/{object_id}', json=body)
        if self.response.status_code != 200:
            print(f'Код статуса создания тестовой записи: {self.response.status_code}')
            print(f'Ответ: {self.response.text}')

            self.response.raise_for_status()

        self.response_json = self.response.json()
