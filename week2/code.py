# Set up logging
import json
import os
import logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Import Boto 3 for AWS Glue
import boto3
client = boto3.client('glue')
dynamodb = boto3.resource('dynamodb')

# Variables for the job:
glueJobName = "testJob"

# Define Lambda function
def lambda_handler(event, context):
    logger.info('## TRIGGERED BY EVENT: ')
    logger.info(event['detail'])
    response = client.start_job_run(JobName=glueJobName)
    logger.info('## STARTED GLUE JOB: ' + glueJobName)
    logger.info('## GLUE JOB RUN ID: ' + response['JobRunId'])
    return response

def query_emp_age(age):
    table = dynamodb.Table('employees')
    response = table.query(
        KeyConditionExpression=Key('age').exists()
    )
    return response

import datetime

def date_conv():
    return datetime.date.today().__format__("%d/%m/%Y")
