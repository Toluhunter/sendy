from uuid import uuid4

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class UserManager(BaseUserManager):

    def create_user(self, username, password, **other_fields):

        account = self.model(username=username, **other_fields)
        account.set_password(password)

        account.save()

        return account
    
    def create_superuser(self, username, password, **other_fields):

        other_fields.setdefault("active", True)

        return self.create_user(username, password, **other_fields)

    
class Account(AbstractBaseUser):

    id = models.UUIDField(default=uuid4, primary_key=True)
    username = models.CharField(max_length=60, null=False, blank=False, unique=True)

    USERNAME_FIELD = "username"

    def __str__(self):

        return self.username