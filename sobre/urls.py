from django.urls import path
from . import views

#produtos
urlpatterns = [
    path('teste/', views.teste)
]