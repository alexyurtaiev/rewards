from django.urls import path

from rewards import views


urlpatterns = [
    path('', views.index, name='index')
]
