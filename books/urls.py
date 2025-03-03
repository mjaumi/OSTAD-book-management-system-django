from django.urls import path
from . import views

# URL patterns for books app declared here
urlpatterns = [
    path('', views.home, name='book_list'),
    path('create/', views.create, name='create_book'),
    path('update/<int:book_id>/', views.update, name='update_book'),
]