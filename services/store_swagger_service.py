from services.base_service import BaseService
import allure


class StoreSwaggerService(BaseService):
    def __init__(self):
        super().__init__()
        self.url = 'https://petstore.swagger.io/v2/store/order/'

    def post_order_pet(self, order_id, pet_id):
        url = self.url
        body = {
            "id": order_id,
            "petId": pet_id,
            "quantity": 0,
            "shipDate": "2024-09-26T07:59:06.996Z",
            "status": "placed",
            "complete": True
        }
        return self.post_request(url=url, body=body)

    def get_order_id(self, order_id):
        url = self.url + str(order_id)
        return self.get_request(url=url)

    def delete_order_id(self, order_id):
        url = self.url + str(order_id)
        return self.delete_request(url=url, code=200)

