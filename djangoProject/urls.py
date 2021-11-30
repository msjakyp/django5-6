"""djangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from lab3_web import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.fourth, name='1stpage'),
    path('2ndpage/', views.second, name='2ndpage'),
    path('3rdpage/', views.third, name='3rdpage'),
    path('4thpage/', views.fourth, name='4thpage'),
    path('5thpage/', views.fifth, name='5thpage'),
    path('6thpage/', views.sixth, name='6thpage'),
    path('7thpage/', views.seven, name='7thpage'),
    path('create_articles', views.create_prod, name='create_articles'),
    path('<int:pk>', views.ArticlesDetailed.as_view(), name='detail_art'),
    path('<int:pk>/update', views.ArticlesUpdate.as_view(), name='update_art'),
]
