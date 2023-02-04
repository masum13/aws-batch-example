# aws-batch-example
This repository contains an example of how to use AWS Batch for batch processing workloads. The example includes a Terraform module for resource creation.

## Requirements
In order to run this example, you will need the following:

## An AWS account
Terraform installed on your computer
Basic knowledge of AWS Batch and Terraform
Terraform Module for Resource Creation
The Terraform module in this repository is used to create the necessary AWS Batch resources for this example. The module creates the following resources:

- Compute Environment
- Job Queue
- Job Definition

To use the Terraform module, follow these steps:

1. Clone this repository to your computer
2. Navigate to the terraform directory
3. Run terraform init to initialize the Terraform working directory
4. Run terraform apply to create the AWS Batch resources
5. After the resources have been created, run terraform destroy to delete the resources when you are finished with the example

### Example Usage
The example in this repository demonstrates how to run a simple batch job using AWS Batch. The batch job runs a shell script that prints the current date and time.

### To run the example, follow these steps:

1. Make sure the AWS Batch resources have been created using the Terraform module
2. Navigate to the batch-job directory
3. Edit the submit-job.sh script to include the correct AWS region and Job Definition name
4. Run ./submit-job.sh to submit the batch job to AWS Batch
5. Monitor the status of the batch job in the AWS Batch console

### Conclusion
This example demonstrates how to use AWS Batch for batch processing workloads. The Terraform module provides a way to create the necessary AWS Batch resources, and the example demonstrates how to run a simple batch job using AWS Batch. Use this example as a starting point for your own batch processing workloads on AWS.
