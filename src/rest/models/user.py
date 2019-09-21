import uuid
from django.db import models


class User(models.Model):
    id = models.CharField(max_length=128, default=uuid.uuid4, primary_key=True)
    email = models.EmailField(null=False)
    password = models.CharField(max_length=128, null=False)
    status = models.IntegerField(default=0, null=False)