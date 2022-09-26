import boto3
pipeline = boto3.client('codepipeline')
regions = 'ap-south-1'
instance = ['i-01121e78e6807681e']
ec2 = boto3.client('ec2', region_name=regions)

def lambda_handler(event, context):
    ec2.start_instances(InstanceIds=instance)
    print('started your instances: ' + str(instance))
    
    response = pipeline.put_job_success_result(
        jobId=event['CodePipeline.job']['id']
    )
    return response
