# Log

- 開発やデプロイの際に生じた問題とその解決法をこのログに残す。

## push してデプロイすることできない

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

- ログを見ていると、`Pipfile.lock` の依存関係がおかしいとあった。おそらく、Heroku 上で Python のライブラリをインストールする作業でコケていると推測した。以下の参考の 1 の記事によると、Pipfile, Pipfile.lock と requirements.txt が共存すると、requirements.txt が無視されるようである。これは、Heroku 上の挙動からもわかる。Heroku 公式が推奨する Python ライブラリのインストール方法は、参考の 2 にあり、requirements.txt を使用するやり方である。従って、Pipfile と Pipfile.lock を削除して、requirements.txt からライブラリをインストールする方針に変更した。

### 参考

1. [requirements.txt vs Pipfile in heroku flask webapp deployment?](https://stackoverflow.com/questions/63252388/requirements-txt-vs-pipfile-in-heroku-flask-webapp-deployment)
2. [The basics](https://devcenter.heroku.com/articles/python-pip#the-basics)

## Python ライブラリが依存関係で上手くインストールできない

- まず、Heroku 上で動かすことのできる Python のバージョンを確認し、開発環境と合わせられるように設定する。サポートしている Python のバージョンは参考の 1 に記述されている。このバージョンを `runtime.txt` に記述すれば、そのバージョンの Python の仮想環境が作成される。[2] ちなみに、サポートされていないバージョン (例えば 3.6.5 など) を記述すると、エラーが生じ、仮想環境が作成されない。

### 参考

1. [Specifying a Python version ](https://devcenter.heroku.com/articles/python-support#specifying-a-python-version)
2. [Specifying a Python Runtime](https://devcenter.heroku.com/articles/python-runtimes)

## Heroku 上の環境変数に、Flask のエントリーポイントとなるファイルのパスとデバッグオプションを設定する

- Deploy には成功したが、アプリケーションが正常に動作しない。`heroku run bash` コマンドでデプロイ先の Heroku のパスを確認する。その後、GUI あるいは CLI で `FLASK_APP=/app/autoapp.py` を設定する。CLI から環境変数を設定する方法は参考 2 に記述されている。コマンドは、以下の 2 つである。

```bash
heroku config:set FLASK_APP=/app/autoapp.py
heroku config:set FLASK_DEBUG=1
heroku config:set CONDUIT_SECRET='hogehogehoge'
```

### 参考

1. [heroku run](https://devcenter.heroku.com/articles/heroku-cli-commands#heroku-run)
2. [Managing config vars](https://devcenter.heroku.com/articles/config-vars#managing-config-vars)
