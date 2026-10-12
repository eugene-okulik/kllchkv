import allure
import requests

from homework.kirill_chernikov.test_api_kchernikov.endpoints.endpoint import Endpoint


class DeleteData(Endpoint):
    @allure.step('Удаление объекта')
    def delete(self, object_id):
        self.response = requests.delete(f'{self.url}/object/{object_id}')
        print(f'Код статуса удаления тестовой записи: {self.response.status_code}')
