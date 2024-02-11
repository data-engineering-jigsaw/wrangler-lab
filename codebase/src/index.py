import awswrangler as wr
import boto3
import pandas as pd


def get_data():
    url = './data/sales_dataset.csv'
    df = pd.read_csv(url)
    return df

def write_to_s3(df, path):
    response = wr.s3.to_parquet(df=df, path=path, 
    partition_cols = ['Order Date'],
    dataset=True, mode="overwrite")
    return response

def read_from_s3(path):
    
    df = wr.s3.read_parquet(path, dataset=True)
    return df

def read_from_db(query):
    return wr.athena.read_sql_query(query, database="ecommerce")