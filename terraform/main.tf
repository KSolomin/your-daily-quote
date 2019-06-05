terraform {
  backend "s3" {
    bucket = "terraform-state-qkt7ce"
    key = "state/terraform.tfstate"
  }
}

provider "aws" {
  region = "${var.region}"
  access_key = "${var.access_key}"
  secret_key = "${var.secret_key}"
}

resource "aws_security_group" "allow_5000" {
  name = "allow-5000"

  ingress {
    from_port = 5000
    to_port = 5000
    protocol = "TCP"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

resource "aws_security_group" "allow_27017" {
  name = "allow-27017"

  ingress {
    from_port = 27017
    to_port = 27017
    protocol = "TCP"
    cidr_blocks = ["${aws_instance.flask_server.public_ip}/32"]
  }
}

resource "aws_instance" "flask_server" {
  ami = "ami-0b2a4d260c54e8d3d"
  instance_type = "t2.micro"
  key_name = "${var.ssh_key_name}"
  security_groups = ["default", "${aws_security_group.allow_5000.name}"]

  tags = {
    Name = "flask-app"
  }
}

resource "aws_instance" "mongo_server" {
  ami = "ami-0b2a4d260c54e8d3d"
  instance_type = "t2.micro"
  key_name = "${var.ssh_key_name}"
  security_groups = ["default", "${aws_security_group.allow_27017.name}"]

  tags = {
    Name = "mongo-app"
  }
} 

output "mongo_server_address" {
  value = "${aws_instance.mongo_server.public_ip}"
}

output "flask_server_address" {
  value = "${aws_instance.flask_server.public_ip}"
}

output "load_balancer_domain" {
  value = "${aws_lb.front_load_balancer.dns_name}"
}
