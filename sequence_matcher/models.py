from django.db import models

class Sequence(models.Model):
    title = models.TextField()
    protein = models.TextField()
    index = models.CharField(max_length=20)
