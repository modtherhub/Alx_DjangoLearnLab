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
