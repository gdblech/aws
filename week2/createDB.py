import boto3
client = boto3.client('dynamodb')

client.create_table(
    AttributeDefinitions=[
        {
            'AttributeName': 'id',
            'AttributeType': 'N'
        },
    ],
    KeySchema=[
        {
            'AttributeName': 'id',
            'KeyType': 'HASH'
        },
    ],
    TableName='employees',
    BillingMode='PAY_PER_REQUEST',
)
