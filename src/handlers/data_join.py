import json
import os
from datetime import datetime
import boto3
import botocore
import pandas as pd
from aws_lambda_powertools import Logger
from aws_lambda_powertools.utilities.typing import LambdaContext
logger = Logger()
DEVICES_DATA_ANALYTICS_BUCKET_NAME = os.getenv(
    'DEVICES_DATA_ANALYTICS_BUCKET_NAME')


@logger.inject_lambda_context(log_event=True)
def handler(event, context: LambdaContext):
    logger.info(event)
    # S3からデータを取得
    s3 = boto3.resource('s3')
    obj = s3.Bucket(event['bucket_name']).Object(event['s3_object_key'])
    response = obj.get()
    body = response['Body'].read().decode('utf-8')
    devices_raw_data = json.loads(body)['data']
    logger.debug(devices_raw_data)
    logger.debug(type(devices_raw_data))

    # Dynamoからデータ取得
    dynamodb = boto3.resource('dynamodb')
    TABLE_NAME = os.getenv('DEVICES_TABLE_NAME')
    table = dynamodb.Table(TABLE_NAME)
    response = table.scan()
    devices = response.get('Items', [])
    logger.debug(devices)
    logger.debug(type(devices))

    # Pandasでデータ結合
    df_devices_raw_data = pd.DataFrame(devices_raw_data)
    df_devices = pd.DataFrame(devices)
    devices_analysis_data = df_devices_raw_data.merge(df_devices)
    logger.debug(devices_analysis_data)

    # S3出力
    csv_data = devices_analysis_data.to_csv(encoding='utf-8', index=None)
    today = datetime.now().strftime('%Y%m%d')
    key = f'devices_operation_history_data/{today}.csv'
    obj = s3.Bucket(DEVICES_DATA_ANALYTICS_BUCKET_NAME).Object(key)
    obj.put(Body=csv_data)
    return {'result': 'Success.'}
