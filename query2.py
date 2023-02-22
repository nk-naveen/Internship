import boto3
from boto3.dynamodb.conditions import Key, Attr


REGION = 'us-east-1'
TABLE_NAME = 'food-db'
dyanmo_db = boto3.resource('dynamodb')
table = dyanmo_db.Table(TABLE_NAME)


def crud(f_name, g_name):

        ##query to write data to table
        # table.put_item(
        #     Item={
        #             'food_name': 'janedoe',
        #             'scientific_name': 'Jane',
        #             'group': 'Doe',
        #             'sub_group': 'Doe1245'
        #         }
        #     )
    ## query to get an itemm from table
    # response = table.get_item(
    #         Key={
    #             'food_name': f_name,
    #             'scientific_name': g_name
    #         }
    #     )
    # item = response['Item']
    # print(item)


    ## query to update an item
    # table.update_item(
    # Key={
    #     'food_name': f_name,
    #     'scientific_name': g_name
    # },
    # UpdateExpression='SET group = :val1',
    #     ExpressionAttributeValues={
    #         ":val1": {"S": "my-group"}
    #     }
    # )
    # Invalid UpdateExpression: Attribute name is a reserved keyword; reserved keyword: group


    ## query to get data based on characters
#     response = table.scan(
#     FilterExpression=Attr('food_name').begins_with('A') & Attr('group').eq(g_name)
# )
#     items = response['Items']

#     for n in items:
#         print(n['food_name'])


    response = table.scan(
    FilterExpression=Attr('scientific_name').begins_with('A') & Attr('sub_group').eq(g_name)
    )       


    items = response['Items']

    for n in items:
        print(n['scientific_name'])
    print("done")


# crud('Ascidians','Vegetables')

crud('Ascidians','Tropical fruits')