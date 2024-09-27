from services.base_service import BaseService


class UserSwaggerService(BaseService):
    def __init__(self):
        super().__init__()
        self.url = 'https://petstore.swagger.io/v2/user'

    def post_user(self, user_name, email):
        url = f'{self.url}/createWithArray'
        body = [
            {
                "id": 0,
                "username": user_name,
                "firstName": "string",
                "lastName": "string",
                "email": email,
                "password": "string",
                "phone": "string",
                "userStatus": 0
            }
        ]
        return self.post_request(url=url, body=body)

    def get_user(self, user_name):
        url = f'{self.url}/{user_name}'
        return self.get_request(url=url)

    def put_user(self, user_name, last_name, email, phone):
        url = f'{self.url}/{user_name}'
        body = {
            "id": 0,
            "username": user_name,
            "firstName": "string",
            "lastName": last_name,
            "email": email,
            "password": "string",
            "phone": phone,
            "userStatus": 0
        }
        return self.put_request(url=url, body=body)

    def delete_user(self, user_name):
        url = f'{self.url}/{user_name}'
        return self.delete_request(url=url, code=200)


