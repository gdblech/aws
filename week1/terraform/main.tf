provider "aws" {
  region                  = "us-east-2"
  shared_credentials_file = "/home/gdblech/.aws/credebtials"
  profile                 = "terraform"
}


resource "aws_iam_policy" "policy" {
  name = "s3CW"

  policy = <<POLICY
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Action": ["*"],
      "Effect": "Allow",
      "Resource": ["arn:aws:s3:::*","arn:aws:cloudwatch:::*"]
    }
  ]
}
  POLICY
}
