# serverless-etl-sample


## インストール

依存ライブラリのインストール

```
$ pipenv shell
$ pipenv install --dev
$ npm install (slsのプラグインをインストール)
```

Serverless Frameworkが入っていない場合はインストールしてください。

```
$ npm -g i serverless
```
## デプロイ

```
$ sls deploy --config serverless-resources.yml
$ sls deploy
```

## サンプルデータ投入

```
python scripts/set_sample_data.py
```