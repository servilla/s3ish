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
import base64
import hashlib

import boto3


def get_sha1_checksum(filename) -> str:
  hasher = hashlib.sha1()
  with open(filename, 'rb') as file:
    while True:
      chunk = file.read(4096)  # Read file in chunks
      if not chunk:
        break
      hasher.update(chunk)
  base64_checksum = base64.b64encode(hasher.digest()).decode('utf-8')

  return base64_checksum


def get_md5_checksum(filename) -> str:
  hasher = hashlib.md5()
  with open(filename, 'rb') as file:
    while True:
      chunk = file.read(4096)  # Read file in chunks
      if not chunk:
        break
      hasher.update(chunk)
    base64_checksum = base64.b64encode(hasher.digest()).decode('utf-8')
  return base64_checksum


def list_buckets():
    s3 = boto3.resource('s3')
    for bucket in s3.buckets.all():
        print(bucket.name)

def push_obj():
    s3 = boto3.resource('s3')
    obj = "/home/servilla/tmp/edi.1790.1.xml"
    sha1 = get_sha1_checksum(obj)
    md5 = get_md5_checksum(obj)
    bucket = "servilla.74ab2caa-4e29-4b34-a191-4eff0d6b8bb9"
    with open(obj, "rb") as data:
        s3.Bucket(bucket).put_object(
            Key="edi.1790.1/edi.1790.1.xml",
            # ChecksumAlgorithm = "SHA1",
            ChecksumSHA1 = sha1,
            ContentMD5 = md5,
            Body=data)


if __name__ == '__main__':
    list_buckets()
    push_obj()

