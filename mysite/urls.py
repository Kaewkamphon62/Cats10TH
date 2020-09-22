from django.contrib import admin
from django.urls import path, include
from myweb import views

urlpatterns = [
    path('', views.catwelcome),
    path('home/', views.cathome),
    path('cats/', views.catcats),


    path('bs.sketchy/', views.bootswatch),
    path('admin/', admin.site.urls),
    #path('polls/', include('polls.urls')),
    path('myweb/', include('myweb.urls')),
]
