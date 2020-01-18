# coding: utf8

import boto3
import json
import os

ENV = os.environ.get('ENV')

s3 = boto3.resource('s3')

def lambda_handler(event, context):

    print(f'event:{event}')

    print(f'ENV:{ENV}')

    response = {'message': 'success'}

    return json.dumps(response)