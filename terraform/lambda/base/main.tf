# Provide abstraction to define a lambda function
terraform {
  required_version = "0.11.7"
}

variable "env" {}
variable "role" {}
variable "function_name" {
  default = ""
}
variable "lambda_filename" {}
variable "script_env_vars" {
  type = "map"
}

data "archive_file" "package_zip" {
  type = "zip"
  # Terraform does not properly support specifying multiple files to be zip-ed:
  # https://www.terraform.io/docs/providers/archive/d/archive_file.html
  # Thus source_dir is used to have a whole dir with all scripts and then required ones will be used.
  # There is a bug in Terraform which does not allow '..' in source_dir, thus we use path.root:
  # https://github.com/terraform-providers/terraform-provider-archive/issues/5
  source_dir = "${path.root}/scripts/"  # Path from top level module.
  # The output path has to be relative. Otherwise the buildkite will always show a diff.
  output_path = "./.terraform/${var.env}-${var.lambda_filename}.zip"
}

resource "aws_lambda_function" "lambda" {
  function_name = "${var.function_name}"
  description = "Simple function"
  role = "${var.role}"

  runtime = "python3.6"
  timeout = 300  // seconds. Max hard limit is 5 min.

  filename = "${data.archive_file.package_zip.output_path}"
  // The handler is always the file name + function name "handler".
  handler = "${var.lambda_filename}.handler"
  source_code_hash = "${data.archive_file.package_zip.output_base64sha256}"

  // Environemnt variables of the script.
  environment {
    variables = "${var.script_env_vars}"
  }
}
