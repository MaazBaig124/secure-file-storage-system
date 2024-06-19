import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your_secret_key'
    AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID') or 'test'
    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY') or 'test'
    AWS_S3_BUCKET = os.environ.get('AWS_S3_BUCKET') or 'my-local-bucket'
    AWS_S3_ENDPOINT_URL = os.environ.get('AWS_S3_ENDPOINT_URL') or 'http://localhost:4566'
