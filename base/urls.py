from django.urls import path
from . import views

#2 then here we must have the url for every view
urlpatterns = [
    path('', views.home)
]