from vk_api.api_methods import User
from vk_api.api_client import APIRequest


class Test:
    user = User()

    def test(self):
        response = self.user.get_user_name()
        print(response.json_data)
        print(response.headers)
