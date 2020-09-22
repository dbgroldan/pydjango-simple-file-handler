from django.db import models
from django.contrib.auth.models import AbstractUser

class Client(AbstractUser):
    identification =  models.CharField(max_length=20, null=False)
    username = None
    email = models.EmailField(unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        db_table = 'client'
        ordering = ['identification']

    def __str__(self):
        return self.identification

class File(models.Model):
    title =  models.CharField(max_length=100, null=False)
    file_data = models.FileField(blank=True, null=True)
    description =  models.CharField(max_length=255)
    # client_id = models.ForeignKey(Client, on_delete=models.CASCADE)

    class Meta:
        db_table = 'file'
        ordering = ['title']

    def __str__(self):
        return self.title