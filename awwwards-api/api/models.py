from django.db import models

# Create your models here.


class Rating(models.Model):
    design = models.IntegerField(max_length=2)
    usability = models.IntegerField(max_length=2)
    content = models.IntegerField(max_length=2)


class Project(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='img/')
    description = models.TextField(max_length=300)
    url = models.CharField()
    posted = models.DateTimeField(auto_now_add=True)
    rating = models.ForeignKey(Rating, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-posted']


class Profile(models.Model):
    avatar = models.ImageField(upload_to='img/')
    bio = models.TextField(max_length=200)
    projects = models.ForeignKey(Project, on_delete=models.CASCADE)
    email = models.EmailField(max_length=100)
