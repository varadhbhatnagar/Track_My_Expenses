from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>/optimize/', views.optimize, name='optimize'),
    path('add/', views.GroupCreate.as_view(), name='group-add'),
    path('', views.groups, name='groups'),
    path('<int:pk>/delete/', views.GroupDelete.as_view(), name='group-delete'),
    path('<int:pk>/addtrans/', views.TransCreate.as_view(), name='trans-add'),
    path('<int:pk>/settle/', views.settle, name='settle'),
]
