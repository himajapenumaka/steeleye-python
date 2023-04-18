# Uploading file to S3 bucket

import boto3

# S3 bucket name and file name
bucket_name = 'bucket-name'
file_name = 'csv_file_in_s3.csv'

# Create an S3 client
s3 = boto3.client('s3')

# Upload the file to S3
s3.upload_file("csv_file.csv", bucket_name, file_name)