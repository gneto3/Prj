from django.urls import path
from blog import views

#blog
urlpatterns = [
    path('', views.index)
]