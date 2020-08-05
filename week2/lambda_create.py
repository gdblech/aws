import boto3

client = boto3.client("lambda")


resp1 = client.create_function(
    FunctionName='glueFunc',
    Runtime='python3.8',
    Role='arn:aws:iam::800064582571:role/lambdaRole',
    Handler='code1.py',
    Code={
        'S3Bucket': 'gdblechtest',
        'S3Key': 'week2/code.zip',
    },
)
print(resp1)

resp2 = client.create_function(
    FunctionName='dynamodbFunc',
    Runtime='python3.8',
    Role='arn:aws:iam::800064582571:role/lambdaRole',
    Handler='code2.py',
    Code={
        'S3Bucket': 'gdblechtest',
        'S3Key': 'week2/code.zip',
    },
)

print(resp2)

resp3 = client.create_function(
    FunctionName='timeFunc',
    Runtime='python3.8',
    Role='arn:aws:iam::800064582571:role/lambdaRole',
    Handler='code3.py',
    Code={
        'S3Bucket': 'gdblechtest',
        'S3Key': 'week2/code.zip',
    },
)

print(resp3)