from django.urls import path
from api import views

# URL Patterns

urlpatterns = [
    path('projects/', views.projects_list),
    path('projects/<int:pk>', views.project_detail),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view())
]
