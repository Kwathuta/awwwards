from rest_framework import serializers
from api.models import *


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ['design', 'usability', 'content']


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['title', 'image', 'description', 'url', 'posted', 'rating']
