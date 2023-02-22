import boto3

dynamodb = boto3.resource('dynamodb')
table_name = 'food-db'

table = dynamodb.create_table(
    TableName=table_name,
    KeySchema=[
        {
            'AttributeName': 'food_name',
            'KeyType': 'HASH'
        },
        {
            'AttributeName': 'scientific_name',
            'KeyType': 'RANGE'
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'food_name',
            'AttributeType': 'S'
        },
        {
            'AttributeName': 'scientific_name',
            'AttributeType': 'S'
        }
        # ,
        # {
        #     'AttributeName': 'group',
        #     'AttributeType': 'S'
        # },
        # {
        #     'AttributeName': 'sub_group',
        #     'AttributeType': 'S'
        # }
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 5,
        'WriteCapacityUnits': 5
    }
    # GlobalSecondaryIndexes=[
    #     {
    #         'IndexName': 'my-index',
    #         'KeySchema': [
    #             {
    #                 'AttributeName': 'col1',
    #                 'KeyType': 'HASH'
    #             },
    #             {
    #                 'AttributeName': 'col2',
    #                 'KeyType': 'RANGE'
    #             }
    #         ],
    #         'Projection': {
    #             'ProjectionType': 'ALL'
    #         },
    #         'ProvisionedThroughput': {
    #             'ReadCapacityUnits': 5,
    #             'WriteCapacityUnits': 5
    #         }
    #     }
    # ]
)

print("Table status:", table.table_status)
