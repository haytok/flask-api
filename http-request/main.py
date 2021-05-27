import argparse
import json

import requests
from dotenv import dotenv_values


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
            self.base_headers['Authorization'] = 'Token {}'.format(self.token)
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

    def create_article(self, title, description, body, tagList):
        request_url = '{}/api/articles'.format(self.BASE_URL)

        headers = self.base_headers.copy()

        payload = {
            'article': {
                'title': title,
                'description': description,
                'body': body,
                'tagList': tagList
            }
        }

        create_article_response = requests.post(
            request_url,
            headers=headers,
            data=json.dumps(payload)
        )
        try:
            return create_article_response.json()
        except:
            status_code = create_article_response.status_code
            if 500 <= status_code < 600:
                print('backend error {}'.format(status_code))
            elif 400 <= status_code < 500:
                print('invalid input data {}'.format(status_code))
            else:
                print('unexpected error {}'.format(status_code))


if __name__ == '__main__':
    # コマンドライン引数から値を受け取る
    parser = argparse.ArgumentParser()
    parser.add_argument('-e', '--environment', help='set environment.')
    args = parser.parse_args()

    # 環境変数を読み出す
    configs = dotenv_values('.env')
    base_url = configs['DEV_BASE_URL'] if args.environment == 'dev' else configs['PROD_BASE_URL']

    print(base_url)

    # ユーザを登録する際は、毎回値を変更する必要がある。
    email = 'test_1@mail.com'
    password = 'password'
    username = 'test_1'

    # 記事を登録する際は、毎回値を変更する必要がある。
    title = 'What I cannot create, I do not understand'
    description = 'Richard Feynman Physics notebook'
    body = 'Richard Feynman Physics notebook'
    tagList = ['Physics']
    
    main = Main(email, password, username, base_url)
    main.create_user()
    main.create_article(title, description, body, tagList)
