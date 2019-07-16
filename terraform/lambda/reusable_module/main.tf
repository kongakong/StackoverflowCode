variable "env" {}
variable "region" {}

provider "aws" {
  region = "${var.region}"
}

resource "aws_iam_role" "mylambda_role" {
  name = "${var.env}-mylambda-role"

  assume_role_policy = <<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Action": "sts:AssumeRole",
      "Principal": {
        "Service": "lambda.amazonaws.com"
      },
      "Effect": "Allow",
      "Sid": ""
    }
  ]
}
EOF
}
 
module "mylambda" {
    source = "../base"
    lambda_filename = "mylambda"
    function_name = "${var.env}-mylambda"
    env = "${var.env}"
    role = "${aws_iam_role.mylambda_role.arn}"
    script_env_vars = {
      DUMMY = "123"
    }
}


