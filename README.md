# django

This is a quick learn repo on creating a todo application with user authentication with Django. This repo covers just the basic stuff.

Table of contents:

1. [Prerequisite](_docs/chapter_1.md)
2. [Project, app, wsgi, asgi, and the files](_docs/chapter_2.md)
3. [Apps, Models, DB](_docs/chapter_3.md)
4. views, templates, actions, forms
5. views, templates, actions, forms (Extended)
6. Statics, styles, assets
7. REST API (basics)
8. REST API (Extended)

## Deployment with Nginx and Let's Encrypt

This project uses Nginx as a reverse proxy with Let's Encrypt for SSL certificates.

### Initial Setup

1. Make sure Docker and Docker Compose are installed on your server
2. Clone this repository to your server
3. Run the initialization script with your domain name:
   ```
   ./init-letsencrypt.sh todo.zaped.xyz
   ```
   This script will:
   - Create temporary certificates
   - Start Nginx
   - Request real Let's Encrypt certificates
   - Reload Nginx with the new certificates

4. Start the entire application stack:
   ```
   docker-compose up -d
   ```

### Certificate Renewal

Certificates will automatically renew thanks to the Certbot container that runs in the background.

### Customizing the Configuration

- Nginx configuration: Edit the `nginx.conf` file
- Let's Encrypt settings: Edit the `init-letsencrypt.sh` script
