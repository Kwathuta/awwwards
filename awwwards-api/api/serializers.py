from rest_framework import serializers
from api.models import *


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ['design', 'usability', 'content']
