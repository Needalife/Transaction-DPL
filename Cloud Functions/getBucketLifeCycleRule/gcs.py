from google.cloud import storage

def getBucketRule(bucket_name):
    storage_client = storage.Client()
    bucket = storage_client.get_bucket(bucket_name)

    print(f"Rules: {list(bucket.lifecycle_rules)}")
    return list(bucket.lifecycle_rules)