FROM nginx:latest

# Delete Defaul Conf file
RUN rm /etc/nginx/conf.d/default.conf
#Copy custom conf file to directory
COPY default.conf /etc/nginx/conf.d


# Delete Default apt sources.list file
RUN rm /etc/apt/sources.list
#Copy custom apt sources.list to directory
COPY sources.list /etc/apt/
RUN apt-get update

# Install Certbot https://certbot.eff.org/lets-encrypt/ubuntubionic-nginx