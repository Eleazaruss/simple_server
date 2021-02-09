from django.urls import path
from masterchef_backend.views import test_response

urlpatterns = [
    path('test/', test_response)
]
