#!/usr/bin/env python
import boto3
from datetime import datetime, date, time

def sign(access_key, secret_key, s3_bucket, object_name, mime_type, expires):
    s3_client = boto3.client('s3',
                             aws_access_key_id=access_key,
                             aws_secret_access_key=secret_key)

    params = {
        'Bucket': s3_bucket,
    	'Key': object_name,
        'ContentType': mime_type
        }

    response = s3_client.generate_presigned_url('put_object',
                                                Params=params,
                                                ExpiresIn=expires)

    return response


def main():
    key = 'ABC'
    secret = 'BBC'
    s3_bucket = 'zeetings-upload-play'
    object_name = '1-2-bcea83ce-22d4-4785-b066-f038fedb9787.pptx'
    mime_type = 'image/jpeg'
    d = date(2019, 7, 14)
    t = time(12, 30)
    expires = datetime.combine(d, t)
    print sign(key, secret, s3_bucket, object_name, mime_type, expires)


if __name__ == '__main__':
    main()

