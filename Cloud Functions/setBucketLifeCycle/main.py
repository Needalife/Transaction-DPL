import functions_framework
from gcs import enforceNewRule, deleteCurrentRule

@functions_framework.http
def run(request):

    request_json = request.get_json(silent=True)

    if request_json:
        age = request_json['age']
        bucket = request_json['bucket']
        print(f"Recieve value of age(type:{type(age)}) and bucket(type:{type(bucket)}) name from POST")
        
        try:
            deleteCurrentRule(bucket)
            enforceNewRule(bucket, age)
            if age < 2:
                return f'Bucket {bucket}: object lifecycle set to {age} day'
            return f'Bucket {bucket}: object lifecycle set to {age} days'
        except Exception as e:
            print(f'Error: {e}')
            return(f'Error: {e}')        
    else:
        age = 'World'
        return 'Hello {}!'.format(age)
