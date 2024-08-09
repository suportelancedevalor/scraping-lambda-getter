import json
import boto3

client = boto3.client('dynamodb')
dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table('http-crud-tutorial-items')

def get(event, context):
    statusCode = 200
    headers = {
        "Content-Type": "application/json"
    }

    response = table.scan()
    data = response['Items']
    
    while response.get('LastEvaluatedKey'):
        response = table.scan(ExclusiveStartKey=response['LastEvaluatedKey'])
        data.extend(response['Items'])

    body = json.dumps(data)
    res = {
        "statusCode": statusCode,
        "headers": headers,
        "body": body
    }

    return res