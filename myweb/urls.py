from django.urls import path
from . import views


urlpatterns = [

    path('', views.myhtml, name='myhtml'),

    path('', views.welcome, name='welcome'),
    path('', views.home, name='home'),
    path('', views.topcats, name='topcats'),

    path('', views.login_user, name='login'),
    path('', views.logout_user, name='logout'),
    path('', views.register_user, name='register'),

    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]