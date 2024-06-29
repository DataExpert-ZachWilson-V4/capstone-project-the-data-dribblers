import math
import time
import http.client
import requests
import boto3
import json
from dagster import asset
from datetime import date
import pandas as pd
import numpy as np

# Replace with your AWS credentials
AWS_ACCESS_KEY_ID = 'AKIAW3MEDYXI3MA3H2MN'
AWS_SECRET_ACCESS_KEY = 'lGwbIHpJYNvGpUeS3T9PQImIagzeFeYWd76FisMj'
BUCKET_NAME = 'datadribblers'

# Initialize S3 client
s3 = boto3.client(
    's3',
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY
)


def get_players(page, fail = 0):
    try:
        url = "https://futdb.app/api/players?page={}".format(page)

        payload = {}
        headers = {
            'accept': 'application/json',
            'X-AUTH-TOKEN': '2aa32e98-c6d2-4ea6-a85a-c07050e459cd'
        }

        response = requests.request("GET", url, headers=headers, data=payload)

        return response.json()['items']
    except Exception as e:
        print(e)
        time.sleep(60)
        if fail < 10:
            get_players(page, fail+1)


def get_players_price(id: str, fail = 0):
    try:
        url = "https://futdb.app/api/players/{}/price".format(id)

        payload = {}
        headers = {
            'accept': 'application/json',
            'X-AUTH-TOKEN': '2aa32e98-c6d2-4ea6-a85a-c07050e459cd'
        }

        response = requests.request("GET", url, headers=headers, data=payload)

        return response.json()
    except Exception as e:
        print(e)
        time.sleep(60)
        if fail < 10:
            get_players_price(id, fail+1)


def get_ea_players(fail=0):
    try:
        url = "https://www.ea.com/ea-sports-fc/ultimate-team/web-app/content/24B23FDE-7835-41C2-87A2-F453DFDB2E82/2024/fut/items/web/players.json?_=22192"

        payload = {}
        headers = {
            'Cookie': 'ak_bmsc=B671FD960A64BE18692862C455FE1984~000000000000000000000000000000~YAAQBYXYF7M4uQiQAQAA9H87OxgiVtcWRHbyCVVQ0BBVRA/MfozM+3ythb+no1bg7nvsf/oeu4xgOMkBONR7HQAJ4q996/2FbMBLhFUEPLttBkuOxErgCFisSdClI32T/vM5BoHT++U+cET4rgAihySqLdexww/DRblDghgd3sQ4rbI7PV7gwFkGki5LEND44N+2iMptVTDrIAs884rOrvj4ir2Qs839thADyX0VeCovtdJ+4KqZrXAk/p4KgOZpJA8MYyBKTiO+ziHJlofe9pY3QI41Thdw2gM+PLERXLjR1oFRU4vdXh3lfoLoKw5WqH2uDhjIR/HY8h8gkP6ywjRNyizXeQpK/NjkVRIMUMBqbFcsQvdNrEQc; ealocale=en-us; EDGESCAPE_COUNTRY=US; EDGESCAPE_REGION=NJ; EDGESCAPE_TIMEZONE=EST'
        }

        response = requests.request("GET", url, headers=headers, data=payload)

        df = response.json()
        return df
    except Exception as e:
        print(e)
        time.sleep(60)
        if fail < 10:
            get_ea_players(fail+1)


def get_ea_players_price(player_id, platform, fail=0):
    try:
        conn = http.client.HTTPSConnection("futbin.org")
        payload = ''
        headers = {}
        conn.request("GET", "/futbin/api/fetchPriceInformation?playerresource={}&platform={}".format(player_id,
                                                                                                     platform), payload,
                     headers)
        res = conn.getresponse()
        data = res.read()
        # print('Got for {}'.format(player_id))
        return data.decode("utf-8")
    except Exception as e:
        print(e)
        time.sleep(60)
        if fail < 10:
            get_ea_players_price(player_id, platform, fail+1)


def save_data_to_s3(data, key):
    """Saves data to S3 bucket."""
    try:
        s3.put_object(Bucket=BUCKET_NAME, Key=key, Body=json.dumps(data))
        print(f"Data saved to S3: {key}")
    except Exception as e:
        print(f"Error saving data to S3: {e}")


@asset(group_name="bootcamp")
def get_futdb_data():
    for i in range(14946, 22749):
        data = get_players_price(i)
        save_data_to_s3(data, 'price_{}/player_{}.json'.format(date.today(), i))


@asset(group_name="bootcamp")
def get_ea_data():
    df = get_ea_players()
    df1 = pd.DataFrame(df['LegendsPlayers'])
    df2 = pd.DataFrame(df['Players'])
    df3 = pd.concat([df1, df2])
    df3.reset_index(inplace=True)
    df3['pricing_data'] = df3['id'].apply(lambda x: get_ea_players_price(x, 'PS'))
    df3.to_csv('price_PS.csv')
    save_data_to_s3(df3.to_json(), 'ea_{}/price_PS_{}.csv'.format(date.today()))
    # df3['pricing_data'] = df3['id'].apply(lambda x: get_ea_players_price(x, 'PC'))
    # df3.to_csv('price_PC.csv')
    # save_data_to_s3(df3.to_json(), 'ea_{}/price_PC_{}.csv'.format(date.today()))