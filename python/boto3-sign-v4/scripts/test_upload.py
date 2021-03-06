#!/usr/bin/env python
import os
import sys
from gen_url import sign
import requests
import uuid

import httplib as http_client
http_client.HTTPConnection.debuglevel = 1


def upload_me(file_path, key=None, secret=None):
    access_key = 'ABC' if key is None else key
    secret_key = 'EDF' if secret is None else secret
    s3_bucket = 'zeetings-upload-play'
    object_name = '1-2-{uuid}.jpeg'.format(uuid=uuid.uuid4())
    mime_type = 'image/jpeg'
    expires = 24 * 60 * 60 # link expriy in sec
    os.environ['AWS_ACCESS_KEY_ID'] = access_key
    os.environ['AWS_SECRET_ACCESS_KEY'] = secret_key
    region = 'us-west-2'
    url = sign(key, secret, s3_bucket, object_name, mime_type, expires, region)
    print url
    with open(file_path, 'rb') as f:
        resp = requests.put(url, data=f)
        print resp.content


if __name__ == '__main__':
    argc = len(sys.argv)
    key = secret = None
    if argc == 2 or argc == 4:
        file_path = sys.argv[1]
        if argc == 4:
            key = sys.argv[2]
            secret = sys.argv[3]
    else:
        raise Exception('1 or 3 arguments')
    upload_me(file_path, key, secret)

