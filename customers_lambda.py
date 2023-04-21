from owenwide import customers


def lambda_handler(event, context):
    return {
        'statusCode': 200,
        'body': customers()
    }
