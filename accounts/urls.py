from django.urls import path , include
from . import views

app_name = 'accounts'
urlpatterns = [
    path('login/', views.loginform , name='login'),
    path('home/', views.home , name='home'),
]
