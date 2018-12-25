# MongoDB

## Getting Started

#### Requirements

Because everything is containerized, as long as you are running TicketFresh as a service there are no pre-requisites. It is however recommended to use MongoDB Compass \([https://www.mongodb.com/products/compass](https://www.mongodb.com/products/compass)\) as it is a user friendly DB explorer.

## Accessing the MongoDB service

#### Connecting via MongoShell

Once inside the container and in a bash terminal \(see: [https://ticketfresh.gitbook.io/documentation/\#accessing-bash-inside-a-service](https://ticketfresh.gitbook.io/documentation/#accessing-bash-inside-a-service) for instructions on how to get there\)

```bash
mongo --username <username> --password <password> --authenticationDatabase admin
```

#### Connecting Via MongoDB Compass

Because the compose file is set up to expose the MongoDB default port \(27017\) to the host machine from the container via tcp you configure the connection as if the service was running locally.  
  
For example if I had a service running with an admin DB that I wanted to connect to using an account called admin the setup would look like the image below. ADD IMAGE HERE

