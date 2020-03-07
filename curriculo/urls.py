from django.urls import path
from .views import curriculo

urlpatterns = [
    path('', curriculo, name="curriculo_url"),
]