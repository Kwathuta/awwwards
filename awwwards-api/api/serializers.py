from django.contrib.auth.models import User
from rest_framework import serializers
from api.models import *


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ['id', 'design', 'usability', 'content']


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ['id', 'title', 'image',
                  'description', 'url', 'posted', 'owner']
        owner = serializers.ReadOnlyField(source='owner.username')


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['id', 'avatar', 'bio', 'projects', 'email']


class UserSerializer(serializers.ModelSerializer):
    projects = serializers.PrimaryKeyRelatedField(
        many=True, queryset=Project.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'projects']
