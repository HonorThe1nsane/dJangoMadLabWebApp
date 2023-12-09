# madlibs/urls.py
from django.urls import path
from .views import madlib_list, madlib_detail, hello_view

urlpatterns = [
    path('', madlib_list, name='madlib_list'),
    path('<int:madlib_id>/', madlib_detail, name='madlib_detail'),
    path('hello/', hello_view, name='hello_view'),
    # Add other URLs as needed
]
