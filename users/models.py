from uuid import uuid4

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser


class UsersModel(AbstractUser):
    id = models.UUIDField(default=uuid4, editable=False, unique=True, primary_key=True)
    username = models.CharField(max_length=150, unique=True)
    first_name = models.CharField(max_length=150, blank=True)
    last_name = models.CharField(max_length=150, blank=True)

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    date_joined = models.DateTimeField(default=timezone.now)
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = [
        "first_name",
        'last_name',
        'password'
    ]

    class Meta:
        db_table = "users"
