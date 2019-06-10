resource "aws_instance" "kibana" {
  ami = "ami-0b2a4d260c54e8d3d"
  instance_type = "t2.micro"
  key_name = "${var.ssh_key_name}"
  security_groups = ["default", "${aws_security_group.allow_elastic.name}"]

  tags = {
    Name = "kibana"
  }
}

output "kibana_address" {
  value = "${aws_instance.kibana.public_ip}"
}