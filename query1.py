#  Question 2: List the all foods when we provide a group name as input. Eg when we
# provide vegetables as a group name it should output all the foods in
# vegetable group. Hint - use scan api

import boto3
from boto3.dynamodb.conditions import Key, Attr


REGION = 'us-east-1'
TABLE_NAME = 'food-db'
dyanmo_db = boto3.resource('dynamodb')
table = dyanmo_db.Table(TABLE_NAME)


def list_food_names(g_name):

    response = table.scan(
        FilterExpression=Key("group").eq(g_name)
    )

    items = response['Items']

    print(f"food names in group: {g_name}")
    for n in items:
        print(n['food_name'])


list_food_names("Aquatic foods")
