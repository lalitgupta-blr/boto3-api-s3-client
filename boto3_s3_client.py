import boto3
import botocore
import io

S3_ACCESS_KEY_ID = '***'
S3_SECRET_ACCESS_KEY = '***'
S3_BUCKET = '**'

class s3ObjectIterator(io.RawIOBase):
    def __init__(self, resources, s3_bucket, key):
        """Initialize with S3 bucket and key names"""
        self.s3r = resources
        self.obj = self.s3r.Object(s3_bucket, key)
        self.obj_stream = self.obj.get()['Body']

    def read(self, n=-1):
        """Read from the stream"""
        return self.obj_stream.read() if n == -1 else self.obj_stream.read(n)


def process_file(s3_resource,key):
	s3_object = s3ObjectIterator(s3_resource,S3_BUCKET, key)

	for line in s3_object:
		print(line)
        
        
# Main method.
if __name__ == '__main__': 

    s3_client = boto3.client('s3', aws_access_key_id=S3_ACCESS_KEY_ID,
                                      aws_secret_access_key=S3_SECRET_ACCESS_KEY , region_name='eu-west-1')
    s3_resource = boto3.resource('s3', aws_access_key_id=S3_ACCESS_KEY_ID,
                                      aws_secret_access_key=S3_SECRET_ACCESS_KEY , region_name='eu-west-1')

    response = s3_client.list_buckets()

    # Output the bucket names
    print('Existing buckets:')
    for bucket in response['Buckets']:
        print(f'  {bucket["Name"]}')

    bucket = s3_resource.Bucket(S3_BUCKET)

    for bucket_object in bucket.objects.all():
        if bucket_object.key.lower().endswith('.txt'):
            print("Contents of Key: " + bucket_object.key)
            process_file(s3_resource,bucket_object.key)





