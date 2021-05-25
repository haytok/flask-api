import requests
import json
import sys
import argparse

class Main(object):
    def __init__(self, email, password, username, base_url):
        self.email = email
        self.password = password
        self.username = username
        
        self.token = None

        self.BASE_URL = base_url
        self.base_headers = {
            'Content-Type':  'application/json',
            'X-Requested-With': 'XMLHttpRequest',
            # 'Authorization': 'Token {{token}}'
        }
    
    def create_user(self):
        request_url = '{}/api/users'.format(self.BASE_URL)

        headers = self.base_headers.copy()

        payload = {
            'user': {
                'email': self.email,
                'password': self.password,
                'username': self.username
            }
        }

        create_user_response = requests.post(
            request_url,
            headers=headers,
            data=json.dumps(payload)
        )
        print(create_user_response)
        create_user_response_json = create_user_response.json()

        print(create_user_response_json)
        if 'errors' in create_user_response_json:
            print(*create_user_response_json['errors']['body'])
            login_user_response = self.login_user()
            self.token = login_user_response['user']['token']
            return
        
        if 'user' in create_user_response_json:
            print('Success user create.')
        
        self.token = create_user_response_json['user']['token']
    
    def login_user(self):
        request_url = '{}/api/users/login'.format(self.BASE_URL)

        headers = self.base_headers.copy()

        payload = {
            'user': {
                'email': self.email,
                'password': self.password,
            }
        }

        login_user_response = requests.post(
            request_url,
            headers=headers,
            data=json.dumps(payload)
        )
        return login_user_response.json()


    def create_article(self):
        pass

if __name__== '__main__':
    # コマンドライン引数から値を受け取る
    parser = argparse.ArgumentParser()
    parser.add_argument('-e', '--environment', help='set environment.')
    args = parser.parse_args()
    print(args.environment)

    # テストする際に定義する必要がある。
    email = 'test_1@mail.com'
    password = 'password'
    username = 'test_1'

    dev_base_url = 'http://127.0.0.1:5000'
    prod_base_url = 'https://boiling-wildwood-20063.herokuapp.com'
    base_url = dev_base_url if args.environment == 'dev' else prod_base_url

    main = Main(email, password, username, base_url)
    main.create_user()
