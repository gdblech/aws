provider "aws" {
  region                  = "us-east-2"
  shared_credentials_file = "/home/gdblech/.aws/credebtials"
  profile                 = "terraform"
}


resource "aws_iam_role" "role" {
  name = "s3CloudWatch"
  assume_role_policy  = <<POLICY
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Action": "sts:AssumeRole",
      "Principal": {
        "Service": ["s3.amazonaws.com","cloudwatch.amazonaws.com"]
      },
      "Effect": "Allow",
      "Sid": ""
    }
  ]
}
  POLICY
}

