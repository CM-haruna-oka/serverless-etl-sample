# serverless-etl-sample


## インストール

Serverless Frameworkが入っていない場合はインストールしてください。

```
$ npm -g i serverless
```

依存ライブラリのインストール

```
$ pipenv shell
$ pipenv install --dev
$ npm install (slsのプラグインをインストール)
```


## デプロイ

```
$ sls deploy --config serverless-resources.yml
$ sls deploy
```

## サンプルデータ投入

```
$ python scripts/set_sample_data.py
$ aws s3 cp sample/devices-raw-data.json s3://devices-raw-data-999999999999-ap-northeast-1/
(アカウントID部分を書き換えてください)
```

## 実行

```
$ sls invoke stepf --name BatchStateMachine
```

'{"result": "Success."}'が返ってくればOKです。