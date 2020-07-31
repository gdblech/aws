
import boto3

client = boto3.client('dynamodb')



client.put_item(
    TableName='employees',
    Item={
        'name': {
            'S': 'Jack',
        },
        'age':{
            'N': '45',
        },
        'id': {
            'N': '1',
        }
    },
)