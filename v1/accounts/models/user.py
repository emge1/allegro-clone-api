import uuid
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from v1.utils.constants import USER_TYPE_CHOICES
from v1.accounts.managers.user_manager import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    objects = UserManager()
    id = models.AutoField(primary_key=True)
    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    type_choice = models.CharField(
        max_length=1,
        choices=USER_TYPE_CHOICES,
        default=4
    )
    date_joined = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'

    class Meta:
        app_label = 'accounts'

    def __str__(self):
        return self.email

    def get_short_name(self):
        return self.email

    def get_full_name(self):
        return self.email

    def save(self, *args, **kwargs):
        if not self.password:
            self.password = str(uuid.uuid4()).replace('-', '')
        super(User, self).save(*args, **kwargs)
