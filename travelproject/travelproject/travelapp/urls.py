from . import views
from django.urls import path

urlpatterns = [

    path('', views.demo,name='demo'),
    # path('expression/',views.expression,name='expression'),
    # path('sub/', views.substraction, name='substraction'),
    # path('mul/', views.multiplication, name='multiplication'),
    # path('div/', views.division, name='division'),
]
