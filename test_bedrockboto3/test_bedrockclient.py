import unittest
from bedrockboto3.bedrockclient import BedrockClient

class TestBedrockBoto3(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super(TestBedrockBoto3, self).__init__(*args, **kwargs)
        self.bedrock_client = BedrockClient()
        self.available_models = self.bedrock_client.available_models()

    def test_foundation_models_number(self):

        # 17 models in the foundation package by 30/09/2023
        assert len(self.available_models) == 17

    def test_fine_tunable_models_number(self):

        # only Amazon Titan is fine-tunable
        assert len(list(filter(lambda item: item.get('customizationsSupported') == ['FINE_TUNING'] , self.available_models))) == 1

    def test_providers(self):
        # response is a list of dictionaries, get the unique value of the provider by the key name providerName
        providers = list(set(map(lambda item: item.get('providerName'), self.available_models)))
        expected_result = ['Amazon', 'Stability AI', 'AI21 Labs', 'Cohere', 'Anthropic']
        # assert that the providers are the same as expected regarding the order of the list
        assert providers.sort() == expected_result.sort()

if __name__ == '__main__':
    unittest.main()
