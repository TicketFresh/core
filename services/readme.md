# Services
This set of folders contain all of the configuration for the microservices of TicketFresh

## Application
This is the primary Flask application service. Note this folder does __NOT__ contain the application logic, all of that can be found in the utilities folder in the root directory of TicketFresh.

## Authentication
The authentication service (including an LDAP service?), and SAML/OAuth logic.

## Database
All the configuration for the database, including the volume mountpoint.

## Nginx
All the configuration for NGINX, including SSL.