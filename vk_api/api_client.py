from dataclasses import dataclass
import allure
import logging
import requests
from requests import Response
import json
from tests.conf import ACCESS_TOKEN
import vk_api

# session = vk_api.Vkapi(token=ACCESS_TOKEN)
# vk = session


@dataclass
class Response:
    status_code: int
    json_data: object
    headers: dict
    request_headers: dict
    text: str


def validate_json(data):
    try:
        loaded = json.loads(data)
    except ValueError as e:
        logging.error(e)
        return False
    return True


class APIRequest:
    def __init__(self):
        self.base_url = "https://api.vk.com/method"
        self.headers = {"access_token": ACCESS_TOKEN}

    def get(self, endpoint="", path="", params=None):
        url = f"{self.base_url}/{endpoint}/{path}"
        response = requests.get(url, params=params, headers=self.headers)
        logging.info(f"{response.status_code} => {response.ok}")
        with allure.step(f"GET request from url {response.request.path_url}"):
            return self.get_response_data(response)

    def post(self, endpoint="", path="", data=None):
        url = f"{self.base_url}/{endpoint}/{path}"
        response = requests.post(url, data=data, headers=self.headers)
        logging.info(f"{response.status_code} => {response.ok}")
        with allure.step(f"POST request from url {response.request.path_url}"):
            return self.get_response_data(response)

    @staticmethod
    def get_response_data(response):
        status_code = response.status_code
        json_data = response.json()
        request_headers = response.request.headers
        headers = response.headers
        text = response.text
        data = response.content
        assert validate_json(data) is True
        with allure.step(f"Response status code{status_code}"):
            return Response(status_code, json_data, request_headers, headers, text)

        # request.method
        # response.request.headers получить заголовки запроса
