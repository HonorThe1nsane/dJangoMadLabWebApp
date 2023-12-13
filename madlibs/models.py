# For now it this is not being used.
from django.db import models

class MadLib(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()

    def __str__(self):
        return self.title