import os

import boto3
import pandas as pd
import pandas as pd

s3 = boto3.client('s3')


def lambda_handler(event, context) -> None:
    """contains function invoked by Lambda
    """

    print('testing pipeline CICD')

    print(os)

    print(s3)

    print(pd.DataFrame())

    return event


if __name__ == "__main__":
    lambda_handler(None, None)
