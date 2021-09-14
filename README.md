# flask-api

## 背景と目的

- curl コマンドを検証する。

## 方法

- [Flask](https://flask.palletsprojects.com/en/2.0.x/) という Python の Web フレームワークを用いて基本的な機能を兼ね備えた REST API を作成する。その API を [Heroku](https://jp.heroku.com/home) という PaaS 上に Deploy する。そして、その API を叩くための Python スクリプトと curl コマンドを実装する。
- 詳細は [http-request](https://github.com/dilmnqvovpnmlib/flask-api/tree/main/http-request) 配下に記述している。

### 検証環境

- Ubuntu 18.04.5 LTS
- Intel(R) Core(TM) i7-8550U CPU @ 1.80GHz

### 主要な技術スタック

- Python 3.6.5

- Flask 2.0.0

- [requests 2.25.1](https://github.com/psf/requests)

- [curl 7.58.0 (x86_64-pc-linux-gnu)](http://manpages.ubuntu.com/manpages/trusty/man1/curl.1.html)

### REST API の仕様

- [仕様](https://github.com/gothinkster/realworld/tree/master/api)
  - ユーザ認証 (認証方式は JWT) で、CRUD の API を兼ね備えた REST API である。
  - [RealWorld example apps](https://github.com/gothinkster/realworld) の backends で紹介されている [flask-realworld-example-app](https://github.com/gothinkster/flask-realworld-example-app) を参考にしている。これは、[Medium.com](https://medium.com/) の API の clone である。

#### API List

- `/api/hello`
  - GET
- `/api/users`
  - POST

### API サーバの開発環境の構築方法

- API サーバのビルド

```bash
make dev-build
```

- API サーバの起動

```bash
make dev-up
```

- API サーバの停止

```bash
make dev-down
````

### Deploy する際に行った作業のログ

- [Log](https://github.com/dilmnqvovpnmlib/flask-api/tree/main/log)
