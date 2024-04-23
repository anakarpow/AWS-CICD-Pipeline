import boto3


def list_stacks_with_prefix(cf_client, prefix):
    """
    Lists all CloudFormation stacks with a specified prefix.

    Parameters:
    - prefix (str): The prefix to filter CloudFormation stack names.

    Returns:
    - list: A list of stack names with the specified prefix.
    """
    # Create Boto3 CloudFormation client

    # List all CloudFormation stacks
    response = cf_client.list_stacks(
        StackStatusFilter=['CREATE_COMPLETE', 'UPDATE_COMPLETE'])

    # Extract stack names with the specified prefix
    stack_names = [stack['StackName'] for stack in response.get('StackSummaries', [])
                   if stack['StackName'].startswith(prefix)]

    return stack_names


def delete_stacks(cf_client, stack_names):
    """
    Deletes CloudFormation stacks with specified names.

    Parameters:
    - stack_names (list): A list of CloudFormation stack names to delete.
    """

    # Delete each stack
    for stack_name in stack_names:
        print("Deleting stack:", stack_name)
        try:
            cf_client.delete_stack(StackName=stack_name)
        except Exception as e:
            print(e)
            pass


cf_client = boto3.client('cloudformation', region_name='eu-west-1')

# Specify the prefix for CloudFormation stack names
# Replace 'your_stack_prefix' with the desired prefix
stack_prefix = 'SC-'

# List CloudFormation stacks with the specified prefix
stacks_with_prefix = list_stacks_with_prefix(cf_client, stack_prefix)
print(stacks_with_prefix)
delete_stacks(cf_client, stacks_with_prefix)

# # Print the list of stacks
# print("CloudFormation stacks with prefix '{}':".format(stack_prefix))
# for stack_name in stacks_with_prefix:
#     print(stack_name)
