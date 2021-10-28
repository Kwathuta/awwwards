from django.contrib.auth.models import User
from rest_framework import serializers
from api.models import *


class RatingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Rating
        fields = ['url', 'id', 'design', 'usability', 'content']


class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Project
        fields = ['url', 'id', 'title', 'image',
                  'description', 'url', 'posted', 'owner']
        owner = serializers.ReadOnlyField(source='owner.username')


class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Profile
        fields = ['url', 'id', 'avatar', 'bio', 'projects', 'email']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    projects = serializers.HyperlinkedRelatedField(
        many=True, view_name='project-detail', read_only=True)

    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'projects']
