from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^(?P<user_id>[0-9]+)/$', views.detail, name='detail')
]
