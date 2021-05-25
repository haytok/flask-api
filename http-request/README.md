# 背景と目的

# 方法

- ユーザを作成するための API を叩く curl コマンド
- `main.py` の `Main.create_user()` に該当する。 

```bash
curl -X POST \
  http://127.0.0.1:5000/api/users \
  -H 'cache-control: no-cache' \
  -H 'content-type: application/json' \
  -H 'postman-token: baf48c18-5238-8958-b2f1-cfa18f0f336b' \
  -H 'x-requested-with: XMLHttpRequest' \
  -d '{
	"user": {
		"email": "test@test.com",
		"password": "test12345",
		"username": "test"
	}
}'
```

-   ログインするための API を叩く curl コマンド
- `main.py` の `Main.login_user()` に該当する。 

```bash
curl -X GET \
  http://127.0.0.1:5000/api/user \
  -H 'authorization: Token eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE2MjE1MDA2MDgsIm5iZiI6MTYyMTUwMDYwOCwianRpIjoiMGUwZTAxMGEtOGQ1OC00MjEyLTgzNDgtMDMyMTE2YzZjZDVlIiwiZXhwIjo4ODAyMTUwMDYwOCwiaWRlbnRpdHkiOjMsImZyZXNoIjpmYWxzZSwidHlwZSI6ImFjY2VzcyJ9.mPRHtpozzGyzPHud4RHUVKSPzeoKEwAXqFIXws2u3RM' \
  -H 'cache-control: no-cache' \
  -H 'content-type: application/json' \
  -H 'postman-token: 22e897c5-f734-c2fb-8174-223463d21c10' \
  -H 'x-requested-with: XMLHttpRequest'
```

-  ログインしたユーザが記事を作成する API を叩く curl コマンド
- `main.py` の `Main.create_article()` に該当する。 

```bash
curl -X POST \
  http://127.0.0.1:5000/api/articles \
  -H 'authorization: Token eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE2MjE1MDA2MDgsIm5iZiI6MTYyMTUwMDYwOCwianRpIjoiMGUwZTAxMGEtOGQ1OC00MjEyLTgzNDgtMDMyMTE2YzZjZDVlIiwiZXhwIjo4ODAyMTUwMDYwOCwiaWRlbnRpdHkiOjMsImZyZXNoIjpmYWxzZSwidHlwZSI6ImFjY2VzcyJ9.mPRHtpozzGyzPHud4RHUVKSPzeoKEwAXqFIXws2u3RM' \
  -H 'cache-control: no-cache' \
  -H 'content-type: application/json' \
  -H 'postman-token: 22beb665-0e01-219c-74a2-5457b16116a9' \
  -H 'x-requested-with: XMLHttpRequest' \
  -d '{
  "article": {
    "title": "How to train your dragon",
    "description": "Ever wonder how?",
    "body": "You have to believe",
    "tagList": ["reactjs", "angularjs", "dragons"]
  }
}'
```
