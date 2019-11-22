from django.urls import path
from django.conf.urls import url
from . import views

#app_name = 'txn'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pk>/detail', views.detail, name='detail'),
    path('add/', views.TransactionCreate.as_view(), name='transaction-add'),
    path('<int:pk>/update/', views.TransactionUpdate.as_view(), name='transaction-update'),
    path('<int:pk>/delete/', views.TransactionDelete.as_view(), name='transaction-delete')
]
