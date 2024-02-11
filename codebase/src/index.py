import awswrangler as wr
import boto3
import pandas as pd


def get_data():
    url = './data/sales_dataset.csv'
    df = pd.read_csv(url)
    return df

def write_to_s3(df, path):
    pass

def read_from_s3(path):
    pass

def read_from_db(query):
    pass
