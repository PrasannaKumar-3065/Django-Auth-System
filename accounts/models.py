from django.db import models

# Create your models here.

class Users(models.Model):
    username = models.CharField(unique=True, max_length=50)
    password = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'users'