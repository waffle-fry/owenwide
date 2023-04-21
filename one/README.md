# Task One

_Lambda Deployment_

Owenwide's Chief Technical Officer has decided that Lambdas are our deployment method of choice.

As a Proof of Concept, he would like to see our customer endpoint made available via a Lambda function. Luckily, another Engineer has already created the code - so you just need to deploy it.

## Prerequisites

You will need Terraform for this, as well as the AWS CLI. If you are using the provided devcontainer, it should be updated to include both dependencies; otherwise everything (including Python) should be installed locally.

## The Task

1. If you do not already have one, create an AWS account.
2. Setup your local environment so that you can run AWS CLI commands.
3. Create a Lambda function in Terraform - you will find Terraform's [AWS Lambda Function](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/lambda_function) documentation helpful - which deploys `customers_lambda.py`. Keep in mind that you will also need to include `owenwide.py` as part of your deployment.

You should be able to test the Lambda Function in the AWS console and see a list of customers.

__Add a screenshot to this folder of the repository once complete, and commit and push your code.__

## Extra Credit
There are some additional tasks that you can complete, if you want to impress Owenwide's CTO:

1. Make the Lambda Function publicly accessible via a URL.

The CTO is happy to help and support as much as necessary while you implement your solution.
