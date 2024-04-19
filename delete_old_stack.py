import boto3

cf_client = boto3.client('cloudformation', region_name="eu-west-1")

for stack in cf_client.describe_stacks()['Stacks']:
    print("deleting {}".format(stack['StackName']))
    cf_client.delete_stack(StackName=stack['StackName'])
