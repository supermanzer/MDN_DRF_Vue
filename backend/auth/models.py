"""Custom User Model

This filec contains the definition we will use for our custom user model.  If we need any customizations
we can perform them here, without breaking the authentication system.
"""
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass
