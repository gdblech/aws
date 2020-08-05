import boto3

client = boto3.client("lambda")


resp1 = client.create_function(
    FunctionName='glueFunc',
    Runtime='python3.8',
    Role='arn:aws:iam::800064582571:role/lambdaRole',
    Handler='code1.lambda_handler',
    Code={
        'S3Bucket': 'gdblechtest',
        'S3Key': 'week2/code.zip',
    },
)

resp2 = client.create_function(
    FunctionName='dynamodbFunc',
    Runtime='python3.8',
    Role='arn:aws:iam::800064582571:role/lambdaRole',
    Handler='code2.query_emp_age',
    Code={
        'S3Bucket': 'gdblechtest',
        'S3Key': 'week2/code.zip',
    },
)

resp3 = client.create_function(
    FunctionName='timeFunc',
    Runtime='python3.8',
    Role='arn:aws:iam::800064582571:role/lambdaRole',
    Handler='code3.date_conv',
    Code={
        'S3Bucket': 'gdblechtest',
        'S3Key': 'week2/code.zip',
    },
)
