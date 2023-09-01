from django.urls import path
from . import views

urlpatterns = [
    path('', views.savingandviewing,name="blog-home"),
]