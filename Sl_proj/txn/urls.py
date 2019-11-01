from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('transactions/<int:user_id>/', views.detail, name='detail'),
    path('optimize/<int:group_id>/',views.group, name ='group')
]
