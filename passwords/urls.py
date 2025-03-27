from django.urls import path
from .views import check_password, generate_password_view

urlpatterns = [
    path('check/', check_password, name='check_password'),
    path('generate/', generate_password_view, name='generate_password'),
]
