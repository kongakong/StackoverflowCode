variable "env" {}
variable "region" {}
variable "function_name" {
  description = "To override default function name"
  default = ""
}

module "team_template" {
  source = "../reusable_module"
  env = "${var.env}"
  region = "${var.region}"
  function_name = "${var.function_name}" 
}


# More resources specific to team_template

