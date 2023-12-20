from django.db import models

# Create your models here.

# Create your models here.
class user(models.Model):
    username = models.CharField(max_length = 18)
    password = models.CharField(max_length = 10)

    def __str__(self):
        return self.username