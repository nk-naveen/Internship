import os
import boto3

def list_objects(bucket_name):

    s3_client = boto3.client("s3")
    objects = s3_client.list_objects_v2(Bucket=bucket_name)

    for obj in objects['Contents']:
        print("|--" +  obj['Key'])
            # print(names)

list_objects("my-new-bucket-nk")