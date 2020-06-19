from django.urls import path , include
from . import views

app_name = 'Switch'
urlpatterns = [
    path('', views.login ),

]
