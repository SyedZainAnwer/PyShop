from django.urls import path
from . import views

urlpatterns = [
    path('', views.index) # URL endpoint which is the root of our product app
]
