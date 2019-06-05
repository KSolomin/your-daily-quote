resource "aws_instance" "elasticsearch" {
  ami = "ami-0b2a4d260c54e8d3d"
  instance_type = "t2.small"
  key_name = "${var.ssh_key_name}"
  security_groups = ["default", "${aws_security_group.allow_elastic.name}"]

  tags = {
    Name = "elasticsearch"
  }
}

resource "aws_security_group" "allow_elastic" {
  name = "allow-elastic"

  ingress {
    from_port = 9200
    to_port = 9200
    protocol = "TCP"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    from_port = 9300
    to_port = 9300
    protocol = "TCP"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

output "elasticsearch_address" {
  value = "${aws_instance.elasticsearch.public_ip}"
}