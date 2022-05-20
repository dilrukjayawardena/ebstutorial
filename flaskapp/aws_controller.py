from urllib import response
import boto3

AWS_SERVER_PUBLIC_KEY="AKIAQ2UESSD64JDFZC7L"
AWS_SERVER_SECRET_KEY="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"
dynamo_client = boto3.client('dynamodb',
                            aws_access_key_id=AWS_SERVER_PUBLIC_KEY, 
                            aws_secret_access_key=AWS_SERVER_SECRET_KEY, 
                            region_name='eu-west-1')

def get_items():
    response=dynamo_client.scan(
        TableName='FilmInfoTable'
    )
    return response['Items']