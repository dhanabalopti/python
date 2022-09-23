import boto3
region = 'ap-south-1'
instance = ['i-01121e78e6807681e']
ec2 = boto3.client('ec2', region_name=region)

def lambda_handler(event, context):
    ec2.start_instances(InstanceIds=instance)
    print('started your instances: ' + str(instance))
