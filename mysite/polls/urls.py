from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('sqltesst/',views.sqltesst,name='sqltesst'),
    path('sqlworking/', views.sqlworking, name='sqlworking'),
]
