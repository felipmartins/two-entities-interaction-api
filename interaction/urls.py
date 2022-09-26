from django.urls import path
from .views import check_if_participants_exists

urlpatterns = [
    path('', check_if_participants_exists ,name='check'),
]
