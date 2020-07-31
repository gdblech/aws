import boto3

glue = boto3.client("glue")

glue.create_crawler(
    Name="testCrawler",
    Role="arn:aws:iam::800064582571:role/Glue_role",
    Targets={
        'S3Targets': [
            {'Path': 's3://gdblechtest/week2'},
        ]
    },
    DatabaseName="test1"
)

glue.start_crawler(Name='testCrawler')
