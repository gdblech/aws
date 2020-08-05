import boto3

client = boto3.client("lambda")


client.create_function(
    FunctionName='glueFunc',
    Runtime='python3.8',
    Role='arn:aws:iam::800064582571:role/lambdaRole',
    Handler='code.py',
    Code={
        'S3Bucket': 'gdblechtest',
        'S3Key': 'week2/code.zip',
    },
)