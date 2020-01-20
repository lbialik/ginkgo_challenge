from django.db import models
from django.utils import timezone

class Sequence(models.Model):
    title = models.TextField()
    protein = models.TextField()
    index = models.CharField(max_length=20)
    timestamp = models.DateTimeField(default=timezone.now)
