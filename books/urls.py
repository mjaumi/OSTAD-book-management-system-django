from django.urls import path
from . import views

# URL patterns for books app declared here
urlpatterns = [
    path('', views.home)
]