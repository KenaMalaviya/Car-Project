from django.urls import path
from .import views
urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.handlelogin, name='handlelogin'),
    path('logout/', views.handlelogout, name='handlelogout'),
    path('forgot/', views.forgot, name='forgot'),
]
