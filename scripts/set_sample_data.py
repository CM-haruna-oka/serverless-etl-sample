import boto3
import yaml
with open('scripts/config.yml', 'r') as yml:
    config = yaml.safe_load(yml)

DEVICES_TABLE_NAME = 'Devices'


def set_test_data(table_name, data):
    dynamodb = boto3.resource('dynamodb')

    table = dynamodb.Table(table_name)
    for i in data:
        table.put_item(Item=i)

set_test_data(DEVICES_TABLE_NAME, config['devices'])
