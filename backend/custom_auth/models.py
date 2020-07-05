from django.contrib.auth.models import AbstractUser, Group


class User(AbstractUser):
    pass


class Group(Group):
    pass
