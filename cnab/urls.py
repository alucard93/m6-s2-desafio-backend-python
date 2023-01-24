from django.urls import path
from .views import IndexView, UploadView

urlpatterns = [
        # uri  /   nome da view      / nome para linkar
    path('', IndexView.as_view(), name='cnab'),
    path('transactions/', UploadView.as_view(), name='transactions'),

]
