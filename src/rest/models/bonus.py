import uuid
from django.db import models


class Bonus(models.Model):
    id = models.CharField(max_length=128, default=uuid.uuid4, primary_key=True)
    bonus_code = models.CharField(max_length=128, null=False)
    status = models.IntegerField(default=0, null=False)
    fas_time = models.DateTimeField(null=True)
    type = models.CharField(max_length=128, null=True)
    user_id = models.CharField(max_length=128, null=True)
    active_time = models.DateTimeField(null=True)