from vk_api.api_methods import User


class Test:
    user = User()

    def test(self):
        response = self.user.get_user_name()
        print(response.json_data)
        print(response.headers)
        print(response.request_headers)
