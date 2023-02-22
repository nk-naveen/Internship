import json
import boto3
from boto3.dynamodb.conditions import Key, Attr

def lambda_handler(event, context):

    TABLE_NAME = 'food-db'
    dyanmo_db = boto3.resource('dynamodb')
    table = dyanmo_db.Table(TABLE_NAME)
    
    f_name = event.get("food_name")
    
    try:
        response = table.query(
            KeyConditionExpression=Key('food_name').eq(f_name))
        
        items = response['Items'][0]
        s_name = items["scientific_name"]
        print(f"scientific name for {f_name} is {s_name}")
        
    except Exception as e:
        raise e
   
    