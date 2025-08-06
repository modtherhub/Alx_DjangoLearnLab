# Django Permissions and Groups Setup

This Django application demonstrates how to manage permissions and user groups to restrict access to various features.

## Custom Permissions

Custom permissions were defined in the `Book` model located in `bookshelf/models.py` under the `Meta` class:

```python
class Meta:
    permissions = [
        ("can_view", "Can view book"),
        ("can_create", "Can create book"),
        ("can_edit", "Can edit book"),
        ("can_delete", "Can delete book"),
    ]


# Security Enhancements in LibraryProject

## ✅ Settings Secured:
- DEBUG=False for production
- Enabled:
  - SECURE_BROWSER_XSS_FILTER
  - X_FRAME_OPTIONS
  - SECURE_CONTENT_TYPE_NOSNIFF
  - SESSION_COOKIE_SECURE
  - CSRF_COOKIE_SECURE

## ✅ Templates Secured:
- All forms include {% csrf_token %}

## ✅ Views Secured:
- All data access uses Django ORM
- No raw SQL used
- Inputs validated via BookForm and other forms

## ✅ CSP:
- django-csp middleware is enabled
- Sources restricted to 'self' and trusted domains only


# HTTPS Deployment Configuration

The application is deployed using Nginx with SSL enabled via Let's Encrypt.

Key SSL Configuration:
- SSL certificate and key are placed in `/etc/letsencrypt/live/example.com/fullchain.pem` and `/etc/letsencrypt/live/example.com/privkey.pem`
- HTTP (port 80) is redirected to HTTPS (port 443)
- HSTS headers are enforced via Django and confirmed in browser dev tools

Recommended commands:
sudo certbot --nginx -d example.com -d www.example.com


# HTTPS & Security Configuration for LibraryProject

## Django Settings

- SECURE_SSL_REDIRECT = True
- SECURE_HSTS_SECONDS = 31536000
- SECURE_HSTS_INCLUDE_SUBDOMAINS = True
- SECURE_HSTS_PRELOAD = True
- SESSION_COOKIE_SECURE = True
- CSRF_COOKIE_SECURE = True
- X_FRAME_OPTIONS = 'DENY'
- SECURE_CONTENT_TYPE_NOSNIFF = True
- SECURE_BROWSER_XSS_FILTER = True

## Deployment

- HTTPS enabled with Let's Encrypt and Nginx
- HTTP automatically redirected to HTTPS
- SSL certificate renewed using certbot
