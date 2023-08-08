from django.urls import path
from . import views

urlpatterns = [
    path('ff/', views.ff_view, name='ff_view'),
    # Add other URL patterns if needed
]