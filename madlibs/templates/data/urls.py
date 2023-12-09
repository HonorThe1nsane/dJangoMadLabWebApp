# madlibs/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.madlib_list, name='madlib_list'),
    path('<int:madlib_id>/', views.madlib_detail, name='madlib_detail'),
    # Add other URLs as needed
]