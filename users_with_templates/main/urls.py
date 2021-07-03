from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.home),
    path('new_user', views.new_user),
]
