from django.db import models
from apps.portfolio.models import Identifier

# Create your models here.





class Feed(models.Model):
    name = models.CharField(max_length=70, null=True)
    desc = models.CharField(max_length=70)

    def __str__(self):
        return self.name

