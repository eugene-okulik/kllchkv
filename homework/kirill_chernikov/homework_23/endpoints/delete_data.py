import allure

from endpoints.endpoint import Endpoint


class DeleteData(Endpoint):

    @allure.step('Удаление объекта')
    def delete(self, object_id, client):
        self.client = client
        self.response = self.client.delete(f'/object/{object_id}')
        print(f'Код статуса удаления тестовой записи: {self.response.status_code}')