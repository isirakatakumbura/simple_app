variable "aws_region" {
  description = "AWS Region"
  type = string
  default = "eu-north-1"
}

variable "cluster_name" {
  description = "EKS Cluster Name"
  type = string
  default = "simple-app-eks"
}

variable "node_instance_type" {
  description = "EC2 type of EKS worker nodes"
  type = string
  default = "t3.micro"
}

variable "desired_capacity" {
  description = "desired number of EKS nodes"
  type = number
  default = 1
}