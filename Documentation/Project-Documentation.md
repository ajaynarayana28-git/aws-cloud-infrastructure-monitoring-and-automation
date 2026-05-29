# AWS Cloud Infrastructure Monitoring and Automation

## Project Objective


- Amazon VPC
- Amazon EC2 (Windows)
- Amazon CloudWatch
- Amazon SNS
- AWS Lambda
- Amazon EventBridge
- AWS CloudTrail
- Amazon S3
- VPC Flow Logs
- Internet Gateway
- Route Tables
- Security Groups

---

## Project Workflow

1. EC2 instances are launched within the custom VPC.
2. Amazon CloudWatch continuously monitors EC2 metrics.
3. CloudWatch alarms are triggered when CPU utilization exceeds the configured threshold.
4. Amazon SNS sends email notifications to administrators.
5. Amazon EventBridge detects the alarm state change.
6. EventBridge invokes the AWS Lambda function.
7. AWS Lambda performs automated EC2 management actions.
8. AWS CloudTrail records AWS API activities.
9. CloudTrail logs are stored in Amazon S3.
10. VPC Flow Logs capture network traffic and publish logs to CloudWatch Logs.

---

## Implementation Steps

### Step 1: VPC Creation

Created a custom VPC with CIDR block 10.0.0.0/16 to provide network isolation and host all project resources.

### Step 2: Subnet Configuration

Created:
- Public Subnet 1 (10.0.1.0/24)
- Public Subnet 2 (10.0.2.0/24)
- Private Subnet (10.0.3.0/24)

The public subnets host Windows EC2 instances while the private subnet hosts internal resources.

### Step 3: Internet Gateway and Route Tables

Created and attached an Internet Gateway to the VPC. Configured route tables to allow internet access for public subnets.

### Step 4: Security Group Configuration

Configured security groups to allow:
- RDP access for Windows instances
- ICMP traffic for testing
- Required outbound traffic

### Step 5: EC2 Deployment

Launched:
- Windows Public EC2 (Automation Target)
- Public EC2 #2 (Alarm Testing Instance)
- Private EC2 (No Public IP)

Verified connectivity and instance health.

### Step 6: CloudWatch Alarm Configuration

Created CloudWatch alarms to monitor EC2 CPU utilization.

Configuration:
- Metric: CPUUtilization
- Threshold: Greater than 70%
- Evaluation Period: 5 Minutes

### Step 7: SNS Notification Setup

Created an SNS topic and configured email subscriptions to receive alarm notifications whenever CloudWatch alarms change state.

### Step 8: Lambda Function Creation

Created an AWS Lambda function using Python and Boto3.

The function:
- Receives EventBridge events
- Performs EC2 automation actions
- Logs execution details for troubleshooting

### Step 9: EventBridge Integration

Configured Amazon EventBridge rules to detect CloudWatch alarm state changes and automatically invoke the Lambda function.

### Step 10: CloudTrail Logging

Enabled AWS CloudTrail to record AWS API activities and store audit logs in Amazon S3 for long-term retention.

### Step 11: VPC Flow Logs Configuration

Enabled VPC Flow Logs to capture network traffic information and publish logs to CloudWatch Logs for monitoring and analysis.

---

## Testing and Validation

The following tests were performed:

- Verified VPC creation and subnet configuration.
- Validated internet connectivity through Internet Gateway.
- Confirmed EC2 instance deployment and accessibility.
- Triggered CloudWatch alarms using high CPU utilization.
- Verified SNS email notifications.
- Confirmed EventBridge rule execution.
- Verified Lambda function execution.
- Checked CloudTrail log delivery to S3.
- Validated VPC Flow Log generation.

---

## Results

The project successfully demonstrated:

- Infrastructure monitoring using CloudWatch.
- Automated alerting through SNS.
- Event-driven automation using EventBridge and Lambda.
- Centralized logging and auditing using CloudTrail and S3.
- Network monitoring using VPC Flow Logs.
- Improved operational efficiency through automation.

---

## Challenges Faced

- Configuring CloudWatch alarm thresholds correctly.
- Managing IAM permissions for Lambda execution.
- Testing EventBridge integrations.
- Validating CloudTrail log delivery.
- Understanding VPC networking and route table configurations.

---

## Learning Outcomes

Through this project, the following AWS concepts were learned and implemented:

- Amazon VPC Networking
- Public and Private Subnets
- Internet Gateways and Route Tables
- Security Groups
- EC2 Deployment and Management
- CloudWatch Monitoring and Alarms
- SNS Notifications
- Lambda Automation
- EventBridge Event Routing
- CloudTrail Auditing
- Amazon S3 Storage
- VPC Flow Logs Monitoring

---

## Conclusion

This project demonstrates a practical AWS monitoring and automation solution that combines monitoring, alerting, logging, auditing, and automated operational response. By integrating CloudWatch, SNS, Lambda, EventBridge, CloudTrail, S3, and VPC Flow Logs, the solution provides improved visibility, automation, and operational efficiency within an AWS environment.
