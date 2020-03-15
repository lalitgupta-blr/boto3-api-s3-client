import boto3
import botocore

S3_ACCESS_ID = '*****'
S3_SECRET_ACCESS_KEY = '****'
S3_BUCKET = '***'

s3_client = boto3.client('s3',aws_access_key=S3_ACCESS_ID, aws_secret_access_key=S3_SECRET_ACCESS_KEY, region_name='eu-west-1')
s3_resource = boto3.resource('s3',aws_access_key=S3_ACCESS_ID, aws_secret_access_key=S3_SECRET_ACCESS_KEY, region_name='eu-west-1')

bucket = s3_resource.Bucket(S3_BUCKET)


for bucket_object in bucket.objects.all()
	if bucket_object.key.lower().endswith('.txt'):
			process_file(bucket_object)


def process_file(key):
	s3_object = s3_client.Object(S3_BUCKET,key)

	for(line in s3_object):
		print(line)



