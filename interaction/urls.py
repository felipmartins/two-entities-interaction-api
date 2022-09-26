from django.urls import path
from .views import check_if_participants_exists, create_participant

urlpatterns = [
    path('', check_if_participants_exists ,name='check-participant'),
    path('create_participant', create_participant, name='create-participant')
]
