# Automated Provisioning

> Tuesday 1st October 2019 (Week 5)

And Config Management 

## Que?

Setting up the hardware and software required by our application. Can be a manual process for the infrastructure team. Given a spec required for our application (e.g. need python installed, etc.)

## Provisioning vs Configuration Management

(virtual) hardware vs software

## Why automate?

- Consistency
- Scalability
- Repeatibility
- Time-saving: don't have to do the same thing many times
- If something goes wrong, can reset
- Predicitability: same thing in every place.
- Fewer knowledge silos: everyone can see how a thing works and adjust/use it
- DevOps...

IaC: Infrastructure as Code

## How?

- Scripting
- Use a Specific language

Bash/Python/Perl

Ansible, Puppet, Chef, Terraform

### Bash

```bash
#!/usr/bin/env bash
sudo apt-get update
sudo apt-get install nginx -y # -y : yes when asked for confirmation. Also -qq
sudo cp index.html /var/www/html/index.html
sudo service nginx restart	# Restart the service
```

## Ansible

**Node**: a server/machine on which we want our Ansible code to run

**Inventory**: file where the hosts and groups are specified (i.e. which machines on which to run)

**Playbook**: language ansible uses for orchestrating, configuring, deploying onto other systems (this, then this, then this)

**Module**: units of wirk that ansible puts on the remote machine.

Ansible is an automation tool for provisioning, configuration managements, application deployment, infrastructure orchestration. Not too much set up to get running. 

Written in YAML - a playbook is a file written in YAML. Connects to your machines (from you inventory) and pushes out modules. When it has executed the modules, it removes them.

**Declarative not imperative**

Tell it what the state should be, not how to get there.

#### Ansible Inventory

Specifying where we are running the ansible modules

```yaml
[default]
127.0.0.1:2222

[ec2]
3.9.179.141 ansible_user=ubuntu
```

#### Ansible Playbook

Specifying what we want

```yaml
---
- hosts: default	# Run this in default specified in inventory file.
  tasks:
	 - name: ensure nginx is at the latest viersion	# Just a human readable name
	   apt: name=nginx state=latest update_cache=yes	# also apt for places where apt isn't usually used.
	 - name: start nginx
	   service:
	   		name: nginx
	   		state: started
	   become: yes	# use sudo
	 - name: copy the index file to www
	   copy: 
	     src: ~/<path to index>/index.html
	     dest: /var/www/html/index.html
	 - name: restart nginx
	   service: 
	     name=nginx				# Same as passing a key-value pair
	     state=restarted
	   become: yes
```

```
ansible-playbook -i .\hosts .\nginx-install.yaml --ask-pass
```

set an ansible playbook:

- -i spec inventory file path
- the playbook file path 
- --ask-pass ask me for a password when you need to login

## Vagrant

Tool for building and managing virtual machines. 

Allows repeatable local envs for testing, sandboxing etc. Uses VirtualBox locally on which to provision the vm.

To start 

```bash
vagrant up
```

Written in ruby.

