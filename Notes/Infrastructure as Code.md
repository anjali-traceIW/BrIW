# Infrastructure as Code

- Define what we want to build
- The state of the infrastructure at any time. Have things been changed manually in an environment? Why? We can refresh the state of it.
- A way of creating/updating the infrastructure
- Languages used are declarative

## CloudFormation

AWS's IaC tool. Written in YAML. Describe your resources and properties. Stacks created from templates.

Change sets - the difference between the current state and the updated state f the iunfrasructure.

## Terraform

### Commands

- `init` initialise your working directory
- `plan` generate the execution plan - what will happen if I execute this script? What is created/updated/detroyed?
- `apply` execute the plan. Will show you what will actually change and ask for confirmation.
- `destroy` remove the terraform managed infrastructure.

### Structure

Written in HCL/HML (HashiCorps <something> Language). Indentation does not matter. Understands usual datatypes: int, string, list, bool. We can use variables too (?)

- Providers - cloud provider and configs
- Resources - things to provision
- Variables - what we want available while we're executing
- State - manage the state of the things you're about to create
- Plan  - 

#### Providers

Understands the API interactions- usually the cloud provider that will create the resources. Example (not bash - HCL/HML):

```bash
provider "aws" {
	region = "eu-west-1"
	version = "~> 2.0"
}
```

#### Resources

The objects and infra going to be created for our provider. Example (not bash - HCL/HML):

```bash
[...]
# resource defined by "TYPE" and "NAME"
resource "aws_security_group" "app_security_group" {
	name 				= "academy-roulette-sg-tf"
	description = "academy-roulette Security Group"
	vpc_id 			= "vpc-0b5cff80d9bff448f"
	
	ingress {
		from_port 	= 8080
		to_port 		= 8080
		protocol 		= "tcp"
		cidr_blocks = ["0.0.0.0/0"]
	}
	
	ingress {
		from_port 	= 9001
		to_port 		= 9001
		protocol 		= "tcp"
		cidr_blocks = ["0.0.0.0/0"]
	}
	
	egress {
		from_port 	= 0
    to_port 		= 0
    protocol 		= "-1"
    cidr_blocks = ["0.0.0.0/0"]
	}
}
```

#### Variables

Params for the terraform scripts = allowing customisation for environments etc.

```haskell
variable environment {
	description = "Env"
	type = "string"
}

variable app {
	description = "App name"
	type = "string"
}

variable aws region {
	description = "AWS region"
	default = "eu-west-1"
}
```

##### Variable definition file

For setting a group of cares - passed in when run plan/apply. Example of a file called `tfvars.tf`

```bash
env = "test"
app = "academy-roulette"
```

use:

```bash
terraform apply -var-=file=tfvars/test/tfvars.tf
```

##### Parameterised Resource

Looking at our Security Group resource but with some parameterised fields. Use placeholders to be replaced with our declared variable values at run (plan or apply) time.

```bash
[...]
resource "aws_security_group" "app_security_group" {
	name = "${var.app}-sg-tf"
	description = "${var.app} Security Group"	# Human name
	vpc_id = "vpc-gjfksalj"
	
	[...]
}
```

#### State

The provisioned resources - used to understand the actual resources configuresd and metadata for it.

```
terraform {
	backend "s3" {
		bucket = "bucket-name"
		dynamodb_table = "lock-table"
		region = "eu-west-1"
		key = "academy-roulette.tfstate"
	}
	required_version = "ver_num"
}
```

#### Making a Cluster with Terraform

order or declaration doesn't matter with cluster, service, etc. Terraform should figure out what needs to come first. Can assist with less clear dependednies with `depends_on = [list of required resources]`

```bash
locals {
	base_tags = {
		Owner = "Academy"
		environment = "test"	#?
	}
}

resource "aws_security_group" "app_security_group" {
	[...]
}

resource "task_definition" "app_task_definition" {
	family = "${var.app}-tf"
	container_definitions = "${file("task-definitions/container-definition.json")}"
	requires_compatibilityes["FARGATE"]
	network_mode = "awsvpc"
	cpu = 256	#?
	memory = 512	#?
	execution_role_arn = "arn:aws:iam::fdjsaklgh"
}

resource "cluster"... {}

resource "aws_ecs_service" "app_service" {
	depends_on = [aws_security_group.app_security_group]	# Can be a list of more than one resource
	name = "${var.app}-tf"
	cluster = "${aws_ecs_cluster.app_cluster.id}"
	task_definition "${...app_task_definition}"
	launch_type = "FARGATE"
	desired_count = 2
	network_configuration {
		subnets = ["subnet-hgjksahgkj", "subnet-2fhjdsg"]
		security_groups = "${aws_security_group.app_security_group}"
	}
}
```



### Types of variables

`${var.app}` a variable we have declared as such. Here the `app` variable is called. Specified by the `var.` prefix

 Resources. Call with reference of following structure `resource_type.resource_name[.resource_attribute]` . To put in a string or something: `"${aws_ecs_cluster.app_cluster.id}"` else can access without `${}`.

Define variables in `<terraform_init_dir>/variables.tf` to access in other terraform files. Actual values of variables are defined in a file `<terraform_init_dir>/tfvars/test/tfvars.tf` as key value pairs.