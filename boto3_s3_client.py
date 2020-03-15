import boto3
import botocore

S3_ACCESS_ID = '*****'
S3_SECRET_ACCESS_KEY = '****'
S3_BUCKET = '***'

s3_client = boto3.client('s3',aws_access_key=S3_ACCESS_ID, aws_secret_access_key=S3_SECRET_ACCESS_KEY, region_name='eu-west-1')
s3_resource = boto3.resource('s3',aws_access_key=S3_ACCESS_ID, aws_secret_access_key=S3_SECRET_ACCESS_KEY, region_name='eu-west-1')



response = s3_client.list_buckets()

# Output the bucket names
print('Existing buckets:')
for bucket in response['Buckets']:
    print(f'  {bucket["Name"]}')


bucket = s3_resource.Bucket(S3_BUCKET)


for bucket_object in bucket.objects.all()
	if bucket_object.key.lower().endswith('.txt'):
		print("Contents of Key: " + bucket_object.key)
		process_file(bucket_object.key)


def process_file(key):
	s3_object = s3_client.Object(S3_BUCKET,key)

	for(line in s3_object):
		print(line)



