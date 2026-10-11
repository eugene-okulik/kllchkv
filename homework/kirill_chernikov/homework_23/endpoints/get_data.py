import allure


from endpoints.endpoint import Endpoint


class GetData(Endpoint):
    @allure.step('Получение всех существующих объектов')
    def get_all(self, client):
        # self.client = client
        self.response = client.get(f'/object')

        if self.response.status_code != 200:
            print(f'Код статуса создания тестовой записи: {self.response.status_code}')
            print(f'Ответ: {self.response.text}')

        self.response_json = self.response.json()

    @allure.step('Получение объекта по id')
    def get_by_id(self, client, object_id):
        self.client = client
        self.response = self.client.get(f'/object/{object_id}')

        if self.response.status_code != 200:
            print(f'Код статуса создания тестовой записи: {self.response.status_code}')
            print(f'Ответ: {self.response.text}')

        self.response_json = self.response.json()
