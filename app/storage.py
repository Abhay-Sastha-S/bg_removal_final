import boto3
from .config import S3_BUCKET, S3_REGION, S3_ACCESS_KEY, S3_SECRET_KEY

def upload_to_s3(file_path, file_name):
    s3 = boto3.client('s3',
                      region_name=S3_REGION,
                      aws_access_key_id=S3_ACCESS_KEY,
                      aws_secret_access_key=S3_SECRET_KEY)
    s3.upload_file(file_path, S3_BUCKET, file_name, ExtraArgs={'ACL':'public-read', 'ContentType':'image/png'})
    s3_url = f"https://{S3_BUCKET}.s3.{S3_REGION}.amazonaws.com/{file_name}"
    return s3_url
