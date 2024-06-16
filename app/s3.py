import boto3
from config import Config


s3_client = boto3.client(
        's3', 
        aws_access_key_id = Config.AWS_ACCESS_KEY_ID, 
        aws_secret_access_key=Config.AWS_SECRET_ACCESS_KEY
)

def upload_file_to_s3(file, filename): 
    s3_client.put_object(Bucket=Config.AWS_S3_Bucket, Key=filename, Body=file)
    return filename

