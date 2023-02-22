import csv
import boto3


REGION ="us-east-1"
TABLE_NAME = 'food-db'

# dynamodb = boto3.client('dynamodb', region_name = REGION)
dynamodb = boto3.resource('dynamodb', region_name=REGION)
table = dynamodb.Table(TABLE_NAME)

#Function to upload data from csv file to dynamodb table
def import_data(path):

    with open(path , 'r') as file:
        reader = csv.reader(file)
        next(reader)
        data = [dict(zip(['food_name','scientific_name','group','sub_group'],row))for row in reader]

    # for item in data:
    #     dynamodb.put_item(TableName = table, Item=item)
    # print("here")
    with table.batch_writer() as batch:
        for item in data:
            # print(item['scientific_name'])
            if item['scientific_name'] == None:
                item['scientific_name'] = 'NULL'
            batch.put_item(Item=item)
    print("done")
    
import_data('C:/Users/nnkum/Downloads/generic-food.csv')