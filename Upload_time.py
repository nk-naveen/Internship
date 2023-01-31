import boto3 
# import time
import logging
from datetime import datetime
import os
from botocore.exceptions import ClientError

def s3_upload(file_name, bucket, object_name=None):

    s3_client = boto3.client("s3")
    if object_name is None:
        object_name = os.path.basename(file_name)

    try:
        start = datetime.now()
        # print(start)
        resp = s3_client.upload_file(file_name, bucket, object_name)
        end = datetime.now()
        # print(end)

        diff = end - start 
        print(f"Time Took to Upload file is {diff.total_seconds() / 60 } mins")

    except ClientError as e:
        logging.error(e)
        return False
    return True         

s3_upload('C:/Users/nnkum/Downloads/015 Cross-Region Replication - Lab.mp4','my-new-bucket-nk')    

