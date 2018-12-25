---
description: This page explains the basics of the main TicketFresh app
---

# Getting Started

## Running TicketFresh

There are two distinct ways of running TicketFresh, locally and as a service \(keep in mind some information varies based on which flavour you're using\):

#### Running TicketFresh Locally

To run TicketFresh locally the only pre-requisites are python 3 and flask. To install flask you can navigate to the main directory and use pip to install flask

```bash
pip install -r requirements.txt
```

#### Running TicketFresh as a Service 

TicketFresh is built to run on docker, and to be run using docker compose. before you can use TicketFresh as a service you will need to install docker. 

#### Installing Docker on windows

My recommendation on windows is to install docker desktop \(Does require Hyper-V so you have to have windows 10 pro or enterprise\): [https://www.docker.com/products/docker-desktop](https://www.docker.com/products/docker-desktop)

#### Installing Docker on Linux and Mac

On Mac you can also install docker desktop found here: [https://www.docker.com/products/docker-desktop](https://www.docker.com/products/docker-desktop)

On inux systems you can install docker through the command line via the instructions found here: [https://docs.docker.com/install/linux/docker-ce/ubuntu/\#set-up-the-repository](https://docs.docker.com/install/linux/docker-ce/ubuntu/#set-up-the-repository)

  
**When running TicketFresh as a service you have two options:**

1. Run as a Daemon \(run as a background process on the host machine\)
2. Run in a persistent terminal window

#### Running TicketFresh as a Daemon

1. Navigate to the main app directory
2. Open Terminal/CMD and run:

```bash
docker-compose up --build -d
```

#### Run in a Persistent terminal window

1. Navigate to the main app directory
2. Open Terminal/CMD and run:

```bash
docker-compose up --build
```

#### Accessing Bash Inside a Service

{% hint style="info" %}
 To get to the bash line of the main app container in either version run the command below \(the service\_name  will be main\)
{% endhint %}

```bash
docker-compose exec <service_name> bash 
```



