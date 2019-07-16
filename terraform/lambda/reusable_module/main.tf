variable "env" {}
variable "region" {}
variable "function_name" {}

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

locals {
    default_function_name = "${var.env}-mylambda"
    final_function_name = "${var.function_name != "" ? var.function_name : local.default_function_name}"
}

module "mylambda" {
    source = "../base"
    lambda_filename = "mylambda"
    function_name = "${local.final_function_name}"
    env = "${var.env}"
    role = "${aws_iam_role.mylambda_role.arn}"
    script_env_vars = {
      DUMMY = "123"
    }
}


