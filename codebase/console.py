import awswrangler as wr

from src.index import get_data, read_from_db, read_from_s3, write_to_s3

path = 's3://jigsaw-wrangler'

df = get_data()
# write_to_s3(df, path)
# read_from_s3(path)
