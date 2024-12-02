#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
:Mod:
    push

:Synopsis:

:Author:
    servilla

:Created:
    12/1/24
"""
import boto3


def list_buckets():
    s3 = boto3.resource('s3')
    for bucket in s3.buckets.all():
        print(bucket.name)

def push_obj():
    s3 = boto3.resource('s3')
    obj = "/home/servilla/tmp/edi.1790.1.xml"
    bucket = "servilla.74ab2caa-4e29-4b34-a191-4eff0d6b8bb9"
    with open(obj, "rb") as data:
        s3.Bucket(bucket).put_object(Key="edi.1790.1/edi.1790.1.xml", Body=data)


if __name__ == '__main__':
    list_buckets()
    push_obj()

