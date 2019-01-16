# TicketFresh
---

Visit https://ticketfresh.gitbook.io/documentation/ for full documentation


# Toolbox
---
it is recommended to take a look at the "toolbox", this is a command line tool that allows for easy provisioning, monitoring, and configuring of TicketFresh: [TicketFresh Toolbox](https://github.com/TicketFresh/toolbox).


# Requirements
---
### Docker & Docker Compose:

#### Windows & Mac
Download docker desktop (includes docker compose): [Docker Desktop](https://www.docker.com/get-started)

#### Linux:
You will need to install docker with whatever package manager your OS uses, also it's likely you will need to download docker-compose seperately. You can also see if you can download docker [directly here](https://docs.docker.com/install/)

### Python 3: 
This is only necessary if you want to run the app without docker: [python Download](https://www.python.org/downloads/)


# Getting Started
---
There are a few ways to run ticketfresh

## TicketFresh as a Daemon:
```
docker-compose up -d
```
This will build the app as it was intended to be used. This will build the authentication service, nginx service, db service, and flask app service. 

## TicketFresh as a flask app
> This assumes you are already running and/or have set up nginx/apache (some sort of reverse proxy), some sort of db (and written a compatability layer if it is not supported), and are running the authentication service.

In the main directory (where routes.py is located) run:
```
python routes.py
```


# Development information
---
All of the information below will help you to get started developing for ticketfresh


## File Structure
---

Folders:

    Services: contains all dockerfiles and configurations for all microservices
    
    Static: All static HTML, CSS, and JS. Along with the ticketfresh instance config file
    
    Utilities: All "core" functionality python files (i.e. test user creation utilities)
    
    Modules: Any aditional optional functionality that is available

