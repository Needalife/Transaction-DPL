from google.cloud import storage

def enforceNewRule(bucket_name,age):
    storage_client = storage.Client()

    bucket = storage_client.get_bucket(bucket_name)
    rules = bucket.lifecycle_rules

    print(f"Lifecycle management rules for bucket {bucket_name} are {list(rules)}")
    bucket.add_lifecycle_delete_rule(age=age)
    bucket.patch()

    rules = bucket.lifecycle_rules
    print(f"Lifecycle management is enable for bucket {bucket_name} and the rules are {list(rules)}")

def deleteCurrentRule(bucket_name):
    storage_client = storage.Client()

    bucket = storage_client.get_bucket(bucket_name)
    bucket.clear_lifecyle_rules()
    bucket.patch()
    rules = bucket.lifecycle_rules

    print(f"Lifecycle management is disable for bucket {bucket_name} and the rules are {list(rules)}")