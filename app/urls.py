# from django.urls import path
# from .views import *

# urlpatterns = [
#     path('', FileUploadView.as_view())
# ]

from django.conf.urls import url
from .views import FileView
urlpatterns = [
    url(r'^upload/$', FileView.as_view(), name='file-upload'),
]