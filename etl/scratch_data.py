import sqlalchemy
import boto3
import json
import pandas as pd
from sqlalchemy import create_engine

# Replace with your AWS credentials
AWS_ACCESS_KEY_ID = 'AKIAW3MEDYXI3MA3H2MN'
AWS_SECRET_ACCESS_KEY = 'lGwbIHpJYNvGpUeS3T9PQImIagzeFeYWd76FisMj'
BUCKET_NAME = 'datadribblers'
engine = create_engine('postgresql://postgres:password@localhost:5432/bootcamp')

s3 = boto3.client('s3', aws_access_key_id=AWS_ACCESS_KEY_ID, aws_secret_access_key=AWS_SECRET_ACCESS_KEY)


def get_data_s3_df(key):
    response = s3.get_object(Bucket=BUCKET_NAME, Key=key)
    object_data = response['Body'].read().decode('utf-8')
    try:
        return pd.DataFrame.from_dict(json.loads(object_data)['items'])
    except Exception as e:
        return pd.DataFrame.from_dict(json.loads(object_data))


def get_players(bucket_name=BUCKET_NAME, path='players/'):
    # List objects in the specified path or prefix within the bucket
    response = s3.list_objects_v2(Bucket=bucket_name, Prefix=path)
    for obj in response.get('Contents', []):
        if '.json' in obj['Key']:
            data = get_data_s3_df(obj['Key'])
            data.to_sql('players', engine, if_exists='append',
                        dtype={"paceAttributes": sqlalchemy.types.JSON, 'shootingAttributes': sqlalchemy.types.JSON,
                               'passingAttributes': sqlalchemy.types.JSON,
                               'dribblingAttributes': sqlalchemy.types.JSON,
                               'defendingAttributes': sqlalchemy.types.JSON,
                               'physicalityAttributes': sqlalchemy.types.JSON,
                               'goalkeeperAttributes': sqlalchemy.types.JSON})


def get_prices(path, bucket_name=BUCKET_NAME):
    response = s3.list_objects_v2(Bucket=bucket_name, Prefix=path)
    for obj in response.get('Contents', []):
        if '.json' in obj['Key']:
            name = obj['Key'].split('/')[1].split('.')[0].split('_')[1]
            data = get_data_s3_df(obj['Key'])
            data['id'] = name
            data['date'] = path.split('_')[1]
            data.to_sql('players_price', engine, if_exists='append')