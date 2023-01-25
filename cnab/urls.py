from django.urls import path
from .views import index_file, cnab_list

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('cnab/filtro', cnab_list, name='cnab-list'), 
    path("cnab/", index_file, name='cnab')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)