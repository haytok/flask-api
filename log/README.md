# Log

- 開発やデプロイの際に生じた問題とその解決法をこのログに残す。

## push してデプロイすることができない

- 開発したものを Heroku 上に Deploy する際、`git push heroku master` ではなく、 `git push heroku main` のコマンドを打つ必要がある。これは、GitHub のデフォルトブランチが master から main になったからである。

### 参考

- [Deploying code](https://devcenter.heroku.com/articles/git#deploying-code)
- [【凡ミス注意！！】git push heroku masterしたら「error: failed to push some refs to ](https://zenn.dev/shimotaroo/articles/14ef835293981a)

## push すると、Python アプリケーションがコンパイルされない

- 開発したアプリケーションを Heroku 上に push すると、以下のエラーが出た。

```bash
heroku Push rejected, failed to compile Python app.
...
```

- ログを見ていると、`Pipfile.lock` の依存関係がおかしいとあった。おそらく、Heroku 上で Python のライブラリをインストールする作業でコケていると推測できる。以下の参考の 1 の記事によると、Pipfile, Pipfile.lock と requirements.txt が共存すると、requirements.txt が無視されるようである。これは、Heroku 上の挙動からもわかる。Heroku 公式が推奨する Python ライブラリのインストール方法は、参考の 2 に記述されていて、requirements.txt を使用するやり方である。従って、Pipfile と Pipfile.lock を削除して、requirements.txt からライブラリをインストールする方針に変更した。

### 参考

1. [requirements.txt vs Pipfile in heroku flask webapp deployment?](https://stackoverflow.com/questions/63252388/requirements-txt-vs-pipfile-in-heroku-flask-webapp-deployment)
2. [The basics](https://devcenter.heroku.com/articles/python-pip#the-basics)

## Python のバージョンを決める

- まず、Heroku 上で動かすことのできる Python のバージョンを確認し、開発環境と合わせられるように設定する。サポートしている Python のバージョンは参考の 1 に記述されている。このバージョンを `runtime.txt` に記述すれば、そのバージョンの Python の仮想環境が作成される。[2] ちなみに、サポートされていないバージョン (例えば 3.6.5 など) を記述すると、エラーが生じ、仮想環境が作成されない。

### 参考

1. [Specifying a Python version ](https://devcenter.heroku.com/articles/python-support#specifying-a-python-version)
2. [Specifying a Python Runtime](https://devcenter.heroku.com/articles/python-runtimes)

## ライブラリが依存関係で上手くインストールできない

- 開発環境でのライブラリのバージョンは参考の 1 を参考にした。しかし、本番環境では、`SQLAlchemy` などのライブラリが古いとのエラーが出て、インストールできなかった。そこで、本番環境では、ライブラリを最新バージョンをインストールし、アプリケーション側でその整合性を保つように変更した。

- ライブラリを再度インストールする際に、キャッシュが効くのが原因で `requirements.txt` を変更してもライブラリが再度インストールされない。また、`pip uninstall hogehoge && pip install hogehoge` を行ってもバージョンはアップデートされない。参考の 2, 3 の記事より、プラグインである [heroku-builds](https://github.com/heroku/heroku-builds) を使って一度インストールしたライブラリを削除してから、再度 `git push heroku master` のコマンドを実行し、再度ライブラリをインストールする手順が必要である。

- ライブラリがインストールされない理由は、Heroku を構成するコンテナ (Dyno) のライフサイクルと関係している。このライフサイクルは興味深いのだが、本筋とは外れるので、ここでは割愛する。

### 参考

1. [Fixes PyJWT and Flask-JWT-Extended version incompatiblity #42](https://github.com/gothinkster/flask-realworld-example-app/pull/42/files)
2. [Build cache](https://devcenter.heroku.com/articles/slug-compiler#build-cache)
3. [How do I clear the build cache?](https://help.heroku.com/18PI5RSY/how-do-i-clear-the-build-cache)
4. [heroku-builds](https://github.com/heroku/heroku-builds)

## ライブラリのバージョンを上げたせいで SQLAlchemy でエラーが生じた

- 生じたエラーは以下である。

```bash
...
AttributeError: 'SQLAlchemy' object has no attribute 'Binary'
...
```

- これは開発環境では古い `SQLAlchemy` を使っていたから生じた問題である。古いバージョン (1.1.9) には `Binary Type` があったが、Heroku が求めるバージョン (1.4.15) では、`Binary Type` が無くなっている。これは参考の 1 の changelog に記述されている。従って、`conduit/user/models.py` に定義されている `User クラス` の `password フィールド` のフィールドの型を `Binary` から `LargeBinary` に変更し、再度データベースを migration する。

- この修正は [b12f224f2c26de27b4f5cf62772bbb27dde7ca80](https://github.com/dilmnqvovpnmlib/flask-api/commit/b12f224f2c26de27b4f5cf62772bbb27dde7ca80) から確認できる。

### 参考

1. [Remove deprecated class Binary. Please use LargeBinary.](https://docs.sqlalchemy.org/en/14/changelog/changelog_14.html#change-214869a306f72f33237772d33fc332ec)

## Heroku 上に PostgresSQL Database を立ち上げる

- そもそも DB を立ち上げていなかったので、Heroku のアドオンを使って立ち上げる。

```bash
heroku addons:create heroku-postgresql:hobby-dev
```

### 参考

- [Managed PostgreSQL from Heroku](https://www.heroku.com/postgres)

## Flask アプリケーションから Heroku 上の Postgres にアクセスする設定を行う

- Postgres のプロセスを指すパスを Flask 側から読み出し、接続する必要がある。しかし、デフォルトの設定では上手くいかないので、参考の 1 の記述に従って [9b6f967b3776cd03aa5d3770e3f151b844fe264c](https://github.com/dilmnqvovpnmlib/flask-api/blob/9b6f967b3776cd03aa5d3770e3f151b844fe264c/conduit/settings.py#L33) の修正を行った。そうすると、DB に接続することはできる。

### 参考

1. [Why is SQLAlchemy 1.4.x not connecting to Heroku Postgres?](https://help.heroku.com/ZKNTJQSK/why-is-sqlalchemy-1-4-x-not-connecting-to-heroku-postgres)

## DB に Unique 制約がなく migration ができない

- `heroku run bash` で Heroku 上に繫ぎ、以下のコマンドを実行して DB のスキーマを定義したい。

```bash
flask db init
flask db migrate
flask db upgrade
```

- しかし、以下のエラーが出て migration できない。おそらくどこかの model に unique 制約を付け忘れていると推測できる。そこで、[019b6f9704e89a8ecd0f06868922b2d22b8eb3a7](https://github.com/dilmnqvovpnmlib/flask-api/commit/019b6f9704e89a8ecd0f06868922b2d22b8eb3a7) のようにプログラムを修正して migration を行うと上手くいった。

```bash
...
sqlalchemy unique constraint
...
```

## Heroku 上の環境変数に、Flask のエントリーポイントとなるファイルのパスとデバッグオプションと秘匿情報を設定する

- Deploy には成功したが、アプリケーションが正常に動作しない。`heroku run bash` コマンドでデプロイ先の Heroku のパスを確認する。[1] そうすると Flask のエントリーポイントのパスがわかる。
- その後、GUI あるいは CLI で 3 つの環境変数を設定する。CLI から環境変数を設定する方法は参考 2 に記述されている。

```bash
heroku config:set FLASK_APP=/app/autoapp.py
heroku config:set FLASK_DEBUG=1
heroku config:set CONDUIT_SECRET='hogehogehoge'
```

### 参考

1. [heroku run](https://devcenter.heroku.com/articles/heroku-cli-commands#heroku-run)
2. [Managing config vars](https://devcenter.heroku.com/articles/config-vars#managing-config-vars)
