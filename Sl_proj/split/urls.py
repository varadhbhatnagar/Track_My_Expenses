from django.urls import path
from . import views

urlpatterns = [
    path('optimize/<int:group_id>/', views.optimize, name='optimize'),
    ]