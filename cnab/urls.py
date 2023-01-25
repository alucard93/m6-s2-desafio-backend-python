from django.urls import path
from .views import index_file

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", index_file, name='cnab')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)