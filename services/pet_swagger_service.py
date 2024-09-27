from services.base_service import BaseService
import allure
import requests
import pytest


class PetSwaggerService(BaseService):
    def __init__(self):
        super().__init__()
        self.url = 'https://petstore.swagger.io/v2/pet/'

    @allure.title('Add a new pet')
    def post_pet_store(self, pet_id, pet_name):
        url = self.url
        body = {
            "id": pet_id,
            "category": {
                "id": 0,
                "name": "string"
            },
            "name": pet_name,
            "photoUrls": [
                "string"
            ],
            "tags": [
                {
                    "id": 0,
                    "name": "string"
                }
            ],
            "status": "available"
        }
        return self.post_request(url=url, body=body)

    @allure.title('Find pet by ID')
    def get_pet_id(self, pet_id):
        url = self.url + str(pet_id)
        return self.get_request(url=url)

    @allure.title('Update pet')
    def put_pet_id(self, pet_id):
        url = self.url + str(pet_id)
        body = {
            "id": pet_id,
            "category": {
                "id": 0,
                "name": "string"
            },
            "name": "doggie",
            "photoUrls": [
                "string"
            ],
            "tags": [
                {
                    "id": 0,
                    "name": "string"
                }
            ],
            "status": "available"
        }
        return self.put_request(url=url, body=body)

    @allure.title('Deletes a pet')
    def delete_pet_id(self, pet_id):
        url = self.url + str(pet_id)
        return self.delete_request(url=url, code=200)
