import boto3

client = boto3.client('dynamodb')

response = client.get_item(
    TableName='employees',
    Key={
        'id': {
            'N': '1',
        }
    },
)

print(response)
