import requests


class Friend:

    def __init__(self, user_id):
        self.user_id = user_id

    def __str__(self):
        return 'https://vk.com/id' + self.user_id

    def friends(self):
        params = {
            'user_id': self.user_id,
            'access_token': '799650ccb127156208bf56b9fcb711b18811b45b2fd21204d56df1d6edc49a0d4cd8288a548a9403d4979',
            'v': '5.92',
            'fields': 'domain'
        }
        response = requests.get('https://api.vk.com/method/friends.get', params)
        data_users = response.json()
        users_set = set()
        for user in data_users['response']['items']:
            users_set.add(user['id'])
        return users_set

    def __and__(self, other):
        user_friends = list(self.friends() & other.friends())
        user_list = [Friend(i) for i in user_friends]
        print(user_list)


if __name__ == "__main__":
    user_1 = Friend('65106773')
    user_2 = Friend('18265880')
    user_1 & user_2
    print(user_1)
    print(user_2)