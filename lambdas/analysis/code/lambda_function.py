import json

def lambda_handler(event, context):
    if -90.0 <= event['latitude'] <= 90.0 and -180.0 <= event['longitude'] <= 180.0:
      return True
    else:
      return False
