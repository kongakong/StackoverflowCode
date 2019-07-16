variable "env" {}
variable "region" {}
variable "team" {}

module "realdeal" {
  source = "../team_template"
  env = "${var.env}"
  region = "${var.region}"
  team = "${var.team}"
}
