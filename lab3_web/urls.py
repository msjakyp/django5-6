from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main, name='4thpage'),
    path('2ndpage/', views.second, name='2ndpage'),
    path('3rdpage/', views.third, name='3rdpage'),
    path('4thpage/', views.fourth, name='4thpage'),
    path('5thpage/', views.fifth, name='5thpage'),
    path('6thpage/', views.sixth, name='6thpage'),
    path('create_articles', views.create_prod, name='create_articles'),
    path('<int:pk>', views.ArticlesDetailed.as_view(), name='detail_art'),
    path('<int:pk>/update', views.ArticlesUpdate.as_view(), name='update_art'),
]