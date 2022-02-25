from django.conf import settings
from django.db import models
from v1.general.created_modified import CreatedModified


class Merchant(CreatedModified):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=255)
    get_details = models.CharField(max_length=255)
    address = models.TextField()

    def __str__(self):
        return self.user.email
