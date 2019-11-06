from django.urls import path
from django.conf.urls import url
from . import views

#app_name = 'txn'
urlpatterns = [
    url(r'^(?P<user_id>[0-9]+)/$', views.index, name='index'),
    url(r'^detail/(?P<pk>[0-9]+)$', views.detail, name='detail'),
    url(r'^transaction/add/$', views.TransactionCreate.as_view(), name='transaction-add'),
    url(r'^transaction/update/(?P<pk>[0-9]+)/$', views.TransactionUpdate.as_view(), name='transaction-update'),
    url(r'^transaction/delete/(?P<pk>[0-9]+)/$', views.TransactionDelete.as_view(), name='transaction-delete'),
    url(r'^register/$', views.UserFormView.as_view(), name='register'),
    #url(r'^login/$', views.UserLoginFormView.as_view(), name='login'),
    path('optimize/<int:group_id>/',views.optimize, name ='optimize'),
    path('analysis/<int:user_id>/',views.analysis, name ='analysis')
]
