from django.db import models

# Create your models here.


def fileName(instance, filename):
    return '/'.join(['projects', str(instance.title), filename])


class Rating(models.Model):
    design = models.IntegerField
    usability = models.IntegerField
    content = models.IntegerField


class Project(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to=fileName)
    description = models.TextField(max_length=300)
    url = models.CharField(max_length=300)
    posted = models.DateTimeField(auto_now_add=True)
    rating = models.ForeignKey(Rating, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-posted']


class Profile(models.Model):
    avatar = models.ImageField(upload_to=fileName)
    bio = models.TextField(max_length=200)
    projects = models.ForeignKey(Project, on_delete=models.CASCADE)
    email = models.EmailField(max_length=100)
