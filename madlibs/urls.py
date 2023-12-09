# madlibs/urls.py
from django.urls import path
from .templates.data import views

urlpatterns = [
    path('', views.madlib_list, name='madlib_list'),
    path('<int:madlib_id>/', views.madlib_detail, name='madlib_detail'),
    path('hello/', hello_view, name='hello_view')
    # Add other URLs as needed
]