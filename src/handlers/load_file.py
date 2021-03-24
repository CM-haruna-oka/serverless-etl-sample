import os
import boto3
import botocore
from aws_lambda_powertools import Logger
from aws_lambda_powertools.utilities.typing import LambdaContext
logger = Logger()
DEVICES_RAW_DATA_BUCKET_NAME = os.getenv(
    'DEVICES_RAW_DATA_BUCKET_NAME')


@logger.inject_lambda_context(log_event=True)
def handler(event, context: LambdaContext):
    logger.info(event)

    s3 = boto3.resource('s3')
    key = 'devices-raw-data.json'

    # ファイルがあるか確認
    try:
        logger.debug(DEVICES_RAW_DATA_BUCKET_NAME)
        s3.Object(DEVICES_RAW_DATA_BUCKET_NAME, key).load()
    except botocore.exceptions.ClientError as e:
        logger.warn(e)
        logger.info('File Not Exist.')
        
        return {'file_exist': False}

    logger.info('File Exist.')
    
    return {
        'file_exist': True,
        'bucket_name': DEVICES_RAW_DATA_BUCKET_NAME,
        's3_object_key': key}
