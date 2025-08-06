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
