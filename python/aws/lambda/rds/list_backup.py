#!/usr/bin/env python
import os
import boto3

aws_access_key_id = os.environ["DEV_AWS_ACCESS_KEY_ID"]
aws_secret_access_key = os.environ["DEV_AWS_SECRET_ACCESS_KEY"]
aws_session_token = os.environ["DEV_AWS_SESSION_TOKEN"]
aws_default_region = os.environ["DEV_AWS_DEFAULT_REGION"]


def main():
    # rds_client = boto3.client('rds',
    #                          aws_access_key_id=aws_access_key_id,
    #                          aws_secret_access_key=aws_secret_access_key,
    #                          aws_session_token=aws_session_token,
    #                          region_name=aws_default_region)
    rds_client = boto3.client('rds',
                              aws_access_key_id=aws_access_key_id,
                              aws_secret_access_key=aws_secret_access_key,
                              aws_session_token=aws_session_token,
                              region_name='us-west-2')
    response = rds_client.describe_db_snapshots(DBInstanceIdentifier='media-master')
    print response


if __name__ == '__main__':
    main()
