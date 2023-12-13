# madlibs/urls.py
from django.urls import path
from .views import madlib_list, madlib_detail, hello_view, home, madlib
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', madlib_list, name='madlib_list'),
    path('<int:madlib_id>/', madlib_detail, name='madlib_detail'),
    path('hello/', hello_view, name='hello_view'),
    path('home/', home, name='home'),
    path('<str:madlib_class>/', madlib, name='madlib'),  # Updated this line
    # Add other URLs as needed
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)