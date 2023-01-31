import boto3
import logging
from botocore.exceptions import ClientError
import os


def create_bucket(bucket_name):
    
    s3_client = boto3.client("s3")

    try:
        #Creating bucket
        s3_client.create_bucket(Bucket=bucket_name)

    except ClientError as e:
        logging.error(e)
        return False
    return True  

create_bucket("")    


def delete_bucket(bucket_name):
    
    s3_client = boto3.client("s3")
    try:
        #delete bucket
        s3_client.delete_bucket(Bucket=bucket_name)

    except ClientError as e:
        logging.error(e)
        return False
    return True  

delete_bucket("my-new-bucket-nk-for-ta")



# def upload_file(file_name, bucket, object_name=None):

#     if object_name is None:
#         object_name = os.path.basename(file_name)
#     s3_client= boto3.client("s3")

#     try:
#         resp = s3_client.upload_file(file_name, bucket, object_name) 
#     except ClientError as e:
#         logging.error(e)
#         return False
#     return True        

#function call
# upload_file('C:/Users/nnkum/Desktop/boto3/file4.txt','my-new-bucket-nk')    



# def list_objects(bucket_name):

#     s3_client = boto3.client("s3")
#     objects = s3_client.list_objects_v2(Bucket=bucket_name)

#     for obj in objects['Contents']:
#         for names in obj['Key']:
#             print(names)

# #function call        
# list_objects('my-new-bucket-nk')       


# def transfer_acceleration(bucket_name):

#     s3_client = boto3.client("s3")

#     try:
#         resp = s3_client.put_bucket_accelerate_configuration(
#             Bucket = bucket_name,
#             AccelerateConfiguration = {
#                 'Status' : 'Suspended'
#                 #'Enabled'  
#             },
#             ChecksumAlgorithm='SHA256'
#         )
#         response = s3_client.get_bucket_accelerate_configuration(Bucket=bucket_name)
#         print(response)
#     except ClientError as e:
#         logging.error(e)
#         return False
#     return True        

# #Transfer Acceleration
# transfer_acceleration("  ")
