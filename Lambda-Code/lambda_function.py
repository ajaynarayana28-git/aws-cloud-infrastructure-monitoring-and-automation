import boto3
import json

ec2 = boto3.client('ec2')

INSTANCE_ID =  'your-public-ec2-instance-id'

def lambda_handler(event, context):
    print("Received event:")
    print(json.dumps(event))

    response = ec2.reboot_instances(
        InstanceIds=[INSTANCE_ID]
    )

    print(f"EC2 reboot triggered successfully for {INSTANCE_ID}")
    print(response)

    return {
        'statusCode': 200,
        'body': f'EC2 reboot triggered successfully for {INSTANCE_ID}'
    }

