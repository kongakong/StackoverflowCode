variable "env" {}
variable "region" {}
variable "team" {}


module "team_template" {
  source = "../reusable_module"
  env = "${var.env}"
  region = "${var.region}"
  function_name = "${var.team}-essentail-function"
}

# More resources specific to team_template

