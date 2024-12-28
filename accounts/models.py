from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from .managers import UserManager


class User(AbstractUser):
    #username gorunmeyecek yerine nomreden istifade edecek,logini nomreye esasen aparacaq
    username = None
    phone_number = models.CharField(max_length=16, unique=True) # +994 50 404 0414

    USERNAME_FIELD = "phone_number"
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email