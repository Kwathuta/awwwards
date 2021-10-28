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
        owner = serializers.ReadOnlyField(source='owner.username')
        fields = ['url', 'id', 'title', 'image',
                  'description', 'url', 'posted', 'owner']


class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Profile
        user = serializers.ReadOnlyField(source='user.username')
        fields = ['url', 'id', 'avatar', 'bio', 'projects', 'email', 'user']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    projects = serializers.HyperlinkedRelatedField(
        many=True, view_name='project-detail', read_only=True)

    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'projects']
