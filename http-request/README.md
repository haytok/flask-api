# 目的

- Heroku 上の REST API に対して Python の requests と curl コマンドで HTTP request を投げる。

# 準備

## 手段 1

- 仮想環境上で以下のコマンドを実行する。

```bash
pip install -r requirements.txt
```

## 手段 2

- Docker を使用する。

```bash
docker build -t main .
docker run -it -v `pwd`:`pwd` main
```

# 方法

## 手段 1

- Pyhton スクリプトで REST API に HTTP Request を行う。

```bash
python main.py
```

## 手段 2

- curl で REST API に HTTP Request を行う。

- このコマンドは、ユーザを作成するための API を叩く curl コマンドである。

- `main.py` の `Main.create_user()` に該当する。 

```bash
curl -X POST \
  https://boiling-wildwood-20063.herokuapp.com/api/users \
  -H 'cache-control: no-cache' \
  -H 'content-type: application/json' \
  -H 'x-requested-with: XMLHttpRequest' \
  -d '{
	"user": {
		"email": "test@test.com",
		"password": "test12345",
		"username": "test"
	}
}'
```

- このコマンドは、ログインするための API を叩く curl コマンドである。
- `main.py` の `Main.login_user()` に該当する。 

```bash
curl -X GET \
  https://boiling-wildwood-20063.herokuapp.com/api/user \
  -H 'authorization: Token eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE2MjE5MzM2MzgsIm5iZiI6MTYyMTkzMzYzOCwianRpIjoiODkxZTYyM2YtNDZhYi00ZGVhLTk2NDctZmVmMDI2MDYyNTU1IiwiZXhwIjoxNjIxOTM0NTM4LCJpZGVudGl0eSI6NiwiZnJlc2giOmZhbHNlLCJ0eXBlIjoiYWNjZXNzIn0.FAqVX4Cwr7XAiYIrrbma3sDIWaFUicUnq67OvIbq4sY' \
  -H 'cache-control: no-cache' \
  -H 'content-type: application/json' \
  -H 'x-requested-with: XMLHttpRequest'
```

- このコマンドは、ログインしたユーザが記事を作成する API を叩く curl コマンドである。
- `main.py` の `Main.create_article()` に該当する。(未実装)

```bash
curl -X POST \
  https://boiling-wildwood-20063.herokuapp.com/api/articles \
  -H 'authorization: Token eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE2MjE5MzM2MzgsIm5iZiI6MTYyMTkzMzYzOCwianRpIjoiODkxZTYyM2YtNDZhYi00ZGVhLTk2NDctZmVmMDI2MDYyNTU1IiwiZXhwIjoxNjIxOTM0NTM4LCJpZGVudGl0eSI6NiwiZnJlc2giOmZhbHNlLCJ0eXBlIjoiYWNjZXNzIn0.FAqVX4Cwr7XAiYIrrbma3sDIWaFUicUnq67OvIbq4sY' \
  -H 'content-type: application/json' \
  -H 'x-requested-with: XMLHttpRequest' \
  -d '{
  "article": {
    "title": "test",
    "description": "test",
    "body": "test",
    "tagList": ["test"]
  }
}'
```
