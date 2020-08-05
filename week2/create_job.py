import boto3
client = boto3.client("glue")

response = client.create_job(
    Name='testJob',
    Role='rn:aws:iam::800064582571:role/Glue_role',

    Command={
        'Name': 'glueetl',
        'ScriptLocation': 's3://gdblechtest/week2',
    },
)
