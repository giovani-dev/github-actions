import os
import boto3
from dotenv import load_dotenv


load_dotenv()


ACCESS_KEY = os.getenv("ACCESS_KEY")
SECRET_KEY = os.getenv("SECRET_KEY")
ENDPOINT = os.getenv("ENDPOINT")


def s3_list_buckets():
    session = boto3.Session(
        aws_access_key_id=ACCESS_KEY,
        aws_secret_access_key=SECRET_KEY,
    )
    s3 = session.client(service_name="s3", endpoint_url=ENDPOINT)
    buckets = s3.list_buckets()
    return buckets["Buckets"]


if __name__ == "__main__":
    x = s3_list_buckets()
    print(x)
