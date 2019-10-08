# Docker

> Monday 7th October 2019 (Week 6)

## What is a container?

Containers allow a developer to package up an application with all of the parts it needs, such as libraries, etc.

Isolate apps and all of their dependencies with none of the overhead of VMs.

All a container contains (haha) is the program and its dependencies. Unlike VMs, they don't emulate a hardware layer or an OS. Runs directly on top of your machine. Therefore more lightweight than a VM but still provides that isolation. Docker makes use of a lot of neat Linux kernel commands that allow it to partition and isolate a program's resources, all of which is abstracted away to us users. It is therefore native to Linux, so if you want to run it on MacOS you will need to virtualise it in a Linux environment.

Containers will create their own memory space, file system, ports, etc so that your own machine's resources are untouched (and also cannot touch your application inside a container).

```bash
# Launch a new container-ish
docker run --rm docker/whalesay cowsay "Hello"

# List running containers
docker ps
```

Can make use of ready-made containers that are globally available.

## Why?

Consistenet, self-contained environment we could deply

To mximise application density e.g. inside a vm, could run two instances of docker containers, then clone that VM many times.

Can tailor make an environment for your application to run in.

## Commands

```bash
docker run [flags] <image> [args]
```

`-d` : detached mode - push to run in background

`-f` : 

`-p` :

`-e` : supply an environment variable to this container e.g. pass in an environment variable called 'mysql_root_password' with value 'password'.

```bash
docker run -d -p 13306:3306 -e MYSQL_ROOT_PASSWORD=password mysql
```

Every image in docker gets assigned its own random id (think of a git commit hash)

```bash
docker stop <container_id OR container_name>
```

Only need to supply enough of an id so that docker knows which one you're talking about.

```bash
docker ps --all
```

Lists every docker container that has ever been run from your machine. Can restart using run command and id.

```bash
docker rm <container_id>
```

Removes a container forever, even from `--all` list.

### Logging into a container

```bash
docker run --rm -it debian bash
```

This will:

- run a debian container
- run bash inside of it
- `-it` login as soon as I activate this container (interactive mode?)
- `--rm` delete container as soon as I stop it

Will automatically be root, as that is the only user

```bash
docker exec -it <container_id> bash
```

Execute bash in a container and log me in as a user.

## Docker Images

Basis of containers.

Constists of the system libraries, system tools, and platform settings. Built in layers which represent the commands of a dockerfile.

When an image is run, it becomes a container.

Structure of a dockerfile

- FROM: what base image are we using e.g. MySQL
- COPY: what we want in the image (i.e. files). Mean we cdont have to use docker cp every time manually.
- RUN: any commands we want to run per image (apt-get, install, update, etc.). e.g. setting command line shortcuts, installing python and pip3 and packages.
- EXPOSE: what ports we want accessible by other containers.
- ENTRYPOINT: configure what gets executed when starting a container. Can be overwritten.
- CMD: used to define the args to ENTRYPOINT

In ascending layer order (which is applied first/how an image is built)

Example - Ubuntu

```dockerfile
# Specify a base image to use. Could just do "FROM ubuntu" to use latest version.
FROM ubuntu:19.04

# Copy contents of api/ to /app in our container
COPY api/ /app

# Install/update all your dependencies for my image 
# python, pip, python-dev, and update pip
RUN apt-get update \
	&& apt-get install -y python3 python3-pip python3-dev \ 
	&& pip3 install --upgrade pip

# install all your requirements for my application
RUN pip3 install -r app/requirements.txt

# Expose port 8080 for other containers to talk to
EXPOSE 8080

# When we start our container, it will run python3 and our app
ENTRYPOINT ["python3", "app/app.py"]
```

To build the file:

```bash
docker build <dir or file name> -t <image name/label>
```

```bash
echo 'alias l=ls -lah' >> /home/.bashrc
```

Could be one of your RUN commands.

### Docker Pull

Pulling an image from a registry (default docker hub).