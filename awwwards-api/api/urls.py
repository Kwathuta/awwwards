from django.urls import path
from api import views

# URL Patterns

urlpatterns = [
    path('projects/', views.projects_list),
    path('projects/<int:pk>', views.project_detail),
]
