resource "aws_lb" "front_load_balancer" {
  subnets = ["subnet-9e93d2d6", "subnet-a39526f9"]
  name = "front-load-balancer"
  load_balancer_type = "application"
  // security_groups = ["${aws_security_group.allow_5000.name}"]
}

resource "aws_lb_target_group" "front_target_group" {
  name = "front-target-group"
  vpc_id = "${aws_lb.front_load_balancer.vpc_id}"
  port = 5000
  protocol = "HTTP"
  target_type = "instance"

  health_check {
    port = 5000
    path = "/hello"
  }
}

resource "aws_lb_target_group_attachment" "front_target_group_attachment" {
  target_group_arn = "${aws_lb_target_group.front_target_group.arn}"
  target_id = "${aws_instance.flask_server.id}"
  port = 5000
}

resource "aws_lb_listener" "front_listener" {
  load_balancer_arn = "${aws_lb.front_load_balancer.arn}"
  port = 5000

  default_action {
    type = "forward"
    target_group_arn = "${aws_lb_target_group.front_target_group.arn}"
  }
}