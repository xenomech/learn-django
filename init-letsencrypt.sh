#!/bin/bash

# Check if domain is provided
if [ -z "$1" ]
then
  echo "Error: Please provide domain name as argument"
  echo "Example: ./init-letsencrypt.sh todo.zaped.xyz"
  exit 1
fi

domain=$1
email="" # Add your email here (optional)
staging=0 # Set to 1 if you're testing your setup to avoid hitting request limits

# Create required directories
mkdir -p certbot/conf/live/$domain
mkdir -p certbot/conf/archive/$domain
mkdir -p certbot/www

# Create dummy certificate
openssl req -x509 -nodes -newkey rsa:4096 -days 1 \
  -keyout certbot/conf/live/$domain/privkey.pem \
  -out certbot/conf/live/$domain/fullchain.pem \
  -subj "/CN=localhost"

echo "### Starting nginx ..."
docker-compose up -d nginx

echo "### Deleting dummy certificate ..."
rm -Rf certbot/conf/live/$domain
rm -Rf certbot/conf/archive/$domain
rm -Rf certbot/conf/renewal/$domain.conf

echo "### Requesting Let's Encrypt certificate for $domain ..."
# Select appropriate email arg
case "$email" in
  "") email_arg="--register-unsafely-without-email" ;;
  *) email_arg="--email $email" ;;
esac

# Enable staging mode if needed
if [ $staging != "0" ]; then staging_arg="--staging"; fi

docker-compose run --rm --entrypoint "\
  certbot certonly --webroot -w /var/www/certbot \
    $staging_arg \
    $email_arg \
    -d $domain \
    --rsa-key-size 4096 \
    --agree-tos \
    --force-renewal" certbot

echo "### Reloading nginx ..."
docker-compose exec nginx nginx -s reload 