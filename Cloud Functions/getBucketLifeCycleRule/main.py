import functions_framework
from gcs import getBucketRule

@functions_framework.http
def run(request):
  request_json = request.get_json(silent=True)

  if request_json:
    bucket = request_json['bucket']
    rules = getBucketRule(bucket)
    print(f"Recieve value of bucket(type:{type(bucket)}) name from POST")
    
    return rules

  else:
    print(f"Got nothing from POST")
    return (f"Fail to receive input from POST")