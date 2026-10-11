import allure
import requests

from homework.kirill_chernikov.test_api_kchernikov.endpoints.endpoint import Endpoint


class GetData(Endpoint):
    @allure.step('Получение всех существующих объектов')
    def get_all(self):
        self.response = requests.get(f'{self.url}/object')
        if self.response.status_code != 200:
            print(f'Код статуса создания тестовой записи: {self.response.status_code}')
            print(f'Ответ: {self.response.text}')
        self.response_json = self.response.json()

        return self.response_json

    @allure.step('Получение объекта по id')
    def get_by_id(self, object_id):
        self.response = requests.get(f'{self.url}/object/{object_id}')
        if self.response.status_code != 200:
            print(f'Код статуса создания тестовой записи: {self.response.status_code}')
            print(f'Ответ: {self.response.text}')

        self.response_json = self.response.json()

        return self.response_json
