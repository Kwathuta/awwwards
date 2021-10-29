from django.urls import path, include
from rest_framework.authtoken import views


urlpatterns = [
    path('login/', views.obtain_auth_token),
    path('accounts/', include('rest_registration.api.urls')),
]
