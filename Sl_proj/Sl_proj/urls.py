from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('mytransactions/', include('txn.urls')),
    path('register/', views.UserSignupFormView.as_view(), name='register'),
    path('login/', views.UserLoginFormView.as_view(), name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('', views.home, name='home'),
    path('analysis/', include('graphs.urls')),
    path('mygroups/', include('split.urls'),name='groups')
]


# Handling Bill Images in Development Mode
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)