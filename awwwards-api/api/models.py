from django.db import models
from cloudinary.models import CloudinaryField
# Create your models here.


def projectFileName(instance, filename):
    return '/'.join(['projects', str(instance.title), filename])


def profileFileName(instance, filename):
    return '/'.join(['profiles', str(instance.email), filename])


class Rating(models.Model):
    design = models.IntegerField
    usability = models.IntegerField
    content = models.IntegerField


class Project(models.Model):
    title = models.CharField(max_length=100)
    image = CloudinaryField(blank=True)
    description = models.TextField(max_length=300)
    url = models.CharField(max_length=300)
    posted = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(
        'auth.User', related_name='projects', on_delete=models.CASCADE)

    class Meta:
        ordering = ['-posted']

    def __str__(self):
        return self.title


class Profile(models.Model):
    user = models.OneToOneField(
        'auth.User', related_name='profile', on_delete=models.CASCADE)
    avatar = CloudinaryField(blank=True)
    bio = models.TextField(max_length=200)
    projects = models.ForeignKey(Project, on_delete=models.CASCADE)
    email = models.EmailField(max_length=100)

    def __str__(self):
        return self.email
