variable "env" {}
variable "region" {}

module "realdeal" {
  source = "../team_template"
  env = "${var.env}"
  region = "${var.region}"
  function_name = "${var.env}-team-realdeal-lambda"
}
