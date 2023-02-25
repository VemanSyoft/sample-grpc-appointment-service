from django.db import models
import uuid


class Appointment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    service = models.CharField(max_length=1000, blank=True, null=False)
    date = models.CharField(max_length=1000, blank=True, null=True,default="")
    slot = models.CharField(max_length=1000, blank=True, null=False)
    end_user = models.CharField(max_length=1000, blank=True, null=False)
    created_at = models.DateTimeField("Created at", auto_now_add=True)
    updated_at = models.DateTimeField("Updated at", auto_now=True)

    def __str__(self):
        return str(self.id)
