from vk_api.api_client import APIRequest

payload = {
    "user_id": "7538793",
    "V": "5.131"
}


class User(APIRequest):
    def __init__(self, path=""):
        super().__init__()
        self.endpoint = "user.get"
        self.path = path
        self.response = APIRequest()

    def get_user_name(self):
        return self.get(self.endpoint, params=payload)
