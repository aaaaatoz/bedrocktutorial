import boto3


class BedrockClient:

    def __init__(self):
        self.bedrockclient = boto3.client('bedrock', region_name='us-east-1')

    def available_models(self):
        response = self.bedrockclient.list_foundation_models()

        return response['modelSummaries']
