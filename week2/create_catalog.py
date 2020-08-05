import boto3

client = boto3.client("athena")

client.create_data_catalog(
    Name='TestCatalog',
    Type='GLUE'
)
