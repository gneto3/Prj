from django.urls import path
from produto import views

#produtos
urlpatterns = [
    path('', views.metodo)
]