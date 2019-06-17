#!/usr/bin/env python

# In a very simple version, the url generated is
# https://zeetings-upload-play.s3.amazonaws.com/1-2-bcea83ce-22d4-4785-b066-f038fedb9787.pptx?AWSAccessKeyId=ABC&content-type=image%2Fjpeg&Expires=1560840279&Signature=ZJRC4QFMAXYCrauF%2FdTVlEjnnF8%3D
# But with the s3v4 switch, it becomes
# https://zeetings-upload-play.s3.amazonaws.com/1-2-bcea83ce-22d4-4785-b066-f038fedb9787.pptx?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Expires=86400&X-Amz-Credential=ABC%2F20190617%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-SignedHeaders=content-type%3Bhost&X-Amz-Date=20190617T064705Z&X-Amz-Signature=bf8c49c3de6bd8e40589e85b52e6fe25219fc76ea53031960c113dfd423562e6

import sys
import boto3
from botocore.client import Config
from datetime import datetime, date, time

def sign(access_key, secret_key, s3_bucket, object_name, mime_type, expires, region):
    s3_client = boto3.client('s3',
                             config=Config(signature_version='s3v4'),
                             region_name=region,
                             aws_access_key_id=access_key,
                             aws_secret_access_key=secret_key)

    # Don't include content type
    #    'ContentType': mime_type
    params = {
        'Bucket': s3_bucket,
    	'Key': object_name,
        }

    response = s3_client.generate_presigned_url('put_object',
                                                Params=params,
                                                ExpiresIn=expires)

    return response


def main(key, secret):
    access_key = 'ABC' if key is None else key
    secret_key = 'EDF' if secret is None else secret 
    s3_bucket = 'zeetings-upload-play'
    object_name = '1-2-bcea83ce-22d4-4785-b066-f038fedb9787.pptx'
    mime_type = 'image/jpeg'
    region = 'us-west-2'
    expires = 24 * 60 * 60 # link expriy in sec
    print sign(key, secret, s3_bucket, object_name, mime_type, expires, region)


if __name__ == '__main__':
    key = secret = None
    if len(sys.argv) == 3:
        key = sys.argv[1]
        secret = sys.argv[2]

    main(key, secret)

