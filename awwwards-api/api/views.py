from django.contrib.auth.models import User
from rest_framework import status, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets, generics
from rest_framework.reverse import reverse
from drf_yasg.utils import swagger_auto_schema
from api.models import *
from api.serializers import *
from api.permissions import *

# Create your views here.


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    @swagger_auto_schema(responses={200: ProjectSerializer()})
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    @swagger_auto_schema(request_body=ProjectSerializer, responses={200: "Your site was submitted successfully"})
    def post(request):
        file = request.data['file']
        image = Profile.objects.create(image=file)
        return Response(({'message': "Uploaded successfully"}), status=status.HTTP_200_OK)


class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly, IsUserOrReadOnly]

    @swagger_auto_schema(responses={200: ProjectSerializer()})
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @swagger_auto_schema(request_body=ProfileSerializer, responses={200: "Your profile was updated successfully"})
    def post(self, request):
        file = request.data['file']
        image = Profile.objects.create(image=file)
        return Response(({'message': "Uploaded successfully"}), status=status.HTTP_200_OK)


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
