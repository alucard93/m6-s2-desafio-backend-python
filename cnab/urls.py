from django.urls import path
from .views import index_file

urlpatterns = [
    path("", index_file, name='cnab')
]