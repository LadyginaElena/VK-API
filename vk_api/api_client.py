from dataclasses import dataclass
import allure
import logging
import requests
from requests import Response
import json


@dataclass
class Response:
    status_code: int
    json_data: object
    headers: dict
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
        self.headers = {
            "accept": "application/json",
            "Content-Type": "application/json",
        }

    def get(self, endpoint="", path="", params=None, headers=None):
        url = f"{self.base_url}/{endpoint}/{path}"
        response = requests.get(url, params=params, headers=self.headers)
        logging.info(f"{response.status_code} => {response.ok}")
        with allure.step(f"GET request from url {response.request.path_url}"):
            return self.get_response_data(response)

    def post(self, endpoint="", path="", json=None, headers=None):
        url = f"{self.base_url}/{endpoint}/{path}"
        response = requests.post(url, json=json, headers=self.headers)
        logging.info(f"{response.status_code} => {response.ok}")
        with allure.step(f"PUT request from url {response.request.path_url}"):
            return self.get_response_data(response)

    def put(self, endpoint="", json=None, headers=None):
        url = f"{self.base_url}/{endpoint}"
        response = requests.post(url, json=json, headers=self.headers)
        logging.info(f"{response.status_code} => {response.ok}")
        with allure.step(f"POST request from url {response.request.path_url}"):
            return self.get_response_data(response)

    def delete(self, endpoint="", path="", json=None, headers=None):
        url = f"{self.base_url}/{endpoint}/{path}"
        response = requests.delete(url, json=pet_data, headers=self.headers)
        logging.info(f"{response.status_code} => {response.ok}")
        with allure.step(f"DELETE request from url {response.request.path_url}"):
            return self.get_response_data(response)

    def get_response_data(self, response):
        status_code = response.status_code
        json_data = response.json()
        headers = response.headers
        text = response.text
        data = response.content
        assert validate_json(data) is True
        with allure.step(f"Response status code{status_code}"):
            return Response(status_code, json_data, headers, text)
        # request.path_url, request.method
        # response.request.headers получить заголовки запроса