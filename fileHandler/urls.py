from django.urls import path, include
from .views import FileView

urlpatterns = [
  url('upload/', FileView.as_view(), name='file-upload'),
]
