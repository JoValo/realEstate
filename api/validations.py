import boto3, json

class CoordinatesValidation():
  def valid(self, latitude, longitude):
    coordinates= json.dumps({
      "latitude": latitude,
      "longitude": longitude
    })

    client = boto3.client('lambda')
    response = client.invoke(
      FunctionName='CoordinatesValidation',
      InvocationType='RequestResponse',
      Payload=bytes(coordinates, 'utf8')
    )
    approved = response['Payload'].read().decode("utf-8")

    return approved == "true"
