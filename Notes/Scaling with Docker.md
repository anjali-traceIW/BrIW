# Scaling with Docker

## Docker-compose

Define and run miltiple container envirnments

- manage the lifecycle of an app through this (yaml) file
- similar commands to docker (run, stop, etc)
- single point for the services of your application
- all services brought up with docker-compse are on the same network and can communicate.

### Example

```yaml
version:x.x
  [specify mysql]
  ...
  briw: 
    image: briw:latest
    depends on:
      - mysql
      - randdrink
      # This briw container will not start until the mysql and randdrink containers have started
    environment:
      - DB_HOST=localhost
      - DB_USER=admin
      - DB_PASSWORD=pass1234
      # set environment variables
    ports:
      - "8080:8081"
      # app locally on 8081. From the host machine, caontact 8080 to get to this app on 8081.
  ...
  [specify randdrink]
```

mysql, briw, randdrink will each be created as their own containers.

When you have a lot of services (each with lots of setup config), a docker compose file is super useful.

```bash
# stop services
docker-compose stop <optional name of service>

# docker logs
docker-compose logs (-f) <optional name of service>

# remove stopped service containers
docker-compose rm <optional name of service>

# stop and remove
docker-compose down
```

### Getting Images from ECR

Log in to ECR:

```bash
$ $(aws ecr get-login --no-include-email --profile iw-sandpit) 
```

Pull the image specified in our docker-compose file

```bash
$ docker-compose pull roulette
```

Build, tag, push image up to ECR:

```bash
# BUILD
docker build -t academy-roulette .

# TAG
docker tag academy-roulette:latest 455073406672.dkr.ecr.eu-west-1.amazonaws.com/academy-roulette:1.2

# PUSH
docker push 455073406672.dkr.ecr.eu-west-1.amazonaws.com/academy-roulette:1.2 
```

### Docker Compose Cheatsheet

```bash
# docker-compose will assume the YML file is called "docker-compose.yml"
$ docker-compose up (-d)                        
# Stop services                        
$ docker-compose stop <optional name of service>

# docker logs
$ docker-compose logs (-f) <optional name of service> 

# remove stopped service containers
$ docker-compose rm <optional name of service>

# stop and remove
$ docker-compose down
```

## Docker Swarm

Made up of nodes 

Nodes - docker engines (some daemons running docker processes) in the swarm: manager nodes and worker nodes

manager node will monitor the workers, stop and start xcontainers, route traffic, etc. You would deploy changes to the manager, which would distribute those changes to the workers.

Services/Tesks - the container you want to run in the cluster. Can be replicated or globally run.

Can distribute some number of services across the worker nodes e.g. seven services accross three workers; might be a copy of each service on each nodes to ensure availability.

Access your services/anything on your nodes via the entrypoint (open port) on your manager node. Could stick a load balancer in front of your worker nodes instead or with(??).

Addition to docker-compose file:

```yaml
image_name:
	image: image_name:ver
	...
  deploy:
    replicas: 3
    restart_policy:
      condition: on-failure
```

deployinh a stack to swarm

```bash
docker stack deploy --compose file docker-compse.yml briw....
```

## ECS

Elastic Container Service

Easily run and scale containerised services on AWS. Less worries about infrastructure. Manages replication of services.

Can be run managed or unmanaged (**Fargate** will manage your infrastructure/EC2 stuff for you or just **EC2**)

Orchestrates the service for you.

### ECS - steps

1. Create a task definition

what is the image/container I want to run. How much memory to allocate etc?

2. Create a cluster

Crete a VPC. Ready to add in services

3. Create a service

​	specify the task definition - will create multiple instances appropriately for your tasks. Every time we make a new instance, use the task def we made.

​	specify the VPC and subnets

​	Configure auto scaling groups - trigger on certain conditions.

## Kubernetes

Container orchestration engine which automates deployment, scalability, etc.

Node: server/vm running K8S or deployed apps

Pod: group of one or more containers (smallest)

replica-set: maintaining a set no of pods

Service: exposes a load-balanced set of pods.

Deployment: managing the lifecycle of an app in the cluster 

Master node - deals with config of and communcation between worker nodes.

Volume - data layer of a application.