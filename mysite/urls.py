from django.contrib import admin
from django.urls import path, include
from myweb import views

urlpatterns = [

    path('', views.welcome),
    path('myweb/', include('myweb.urls')),

    path('home/', views.home),
    path('login/', views.login_user),
    path('logout/', views.logout_user),

    path('admin/', admin.site.urls),
]