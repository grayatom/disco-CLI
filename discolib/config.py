import boto3

try:
    sts = boto3.client('sts')
    caller_identity = sts.get_caller_identity()
    user_arn = caller_identity["Arn"]
    USER_EMAIL = user_arn.split(':user/')[1]
except Exception as e:
    print(f'{e.__class__.__name__}: {e}')
    exit(1)
