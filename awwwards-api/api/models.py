from django.db import models

# Create your models here.


class Project(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='img/')
    description = models.TextField
    url = models.CharField()
    posted = models.DateTimeField(auto_now_add=True)
