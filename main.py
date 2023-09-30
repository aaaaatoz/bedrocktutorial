
from bedrockboto3.bedrockclient import BedrockClient
from tabulate import tabulate


def main():
    bedrock_client = BedrockClient()
    response = bedrock_client.available_models()
    # print the response as a table
    print(tabulate(response, headers='keys'))


if __name__ == "__main__":
    main()