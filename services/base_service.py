import json
import requests
from helpers.logger import create_logger


class BaseService:
    def __init__(self):
        self.logger = create_logger()

    def post_request(self, url, body, code=200):
        headers = {
            'Content-Type': 'application/json'
        }
        payload = json.dumps(body)
        response = requests.post(url, data=payload, headers=headers)

        if response.status_code == code:
            self.logger.info(f'HTTP: {response.url}: {response.text}"')
            return response.json()
        else:
            self.logger.error(f"ERORR HTTP: {response.url}: {response.text}")
            return False

    def put_request(self, url, body, code=200):
        headers = {
            'accept': 'application/json',
            'Content-Type': 'application/json'
        }
        payload = json.dumps(body)
        response = requests.put(url, data=payload, headers=headers)

        if response.status_code == code:
            self.logger.info(f'HTTP: {response.url}: {response.text}"')
            return response.json()
        else:
            self.logger.error(f"ERORR HTTP: {response.url}: {response.text}")
            return False

    def get_request(self, url, code=200):
        headers = {
            'accept': 'application/json'
        }
        response = requests.get(url, headers=headers)

        if response.status_code == code:
            self.logger.info(f'HTTP: {response.url}: {response.text}"')
            return response.json()
        else:
            self.logger.error(f"ERORR HTTP: {response.url}: {response.text}")
            return False

    def delete_request(self, url, code=200):
        headers = {
            'accept': 'application/json'
        }
        response = requests.delete(url, headers=headers)

        if response.status_code == code:
            self.logger.info(f'Request is DELETE HTTP: {response.url}: {response.text}"')
            return response.json()
        else:
            self.logger.error(f"Request is not DELETE HTTP: {response.url}: {response.text}")
            return False

