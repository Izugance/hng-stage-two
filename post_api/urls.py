from django.urls import path
from .views import arithmetic_post_view

urlpatterns = [
    path("", arithmetic_post_view)
]