import os
import sys


sys.path.append(f"{os.getcwd()}/src")


from main import s3_list_buckets


class TestS3BucketList:
    def test_list_buckets(self):
        buckets = s3_list_buckets()
        assert buckets
