from django.urls import path
from .views import check_if_participants_exists, create_participant, check_if_connection_exists, create_connection, send_message

urlpatterns = [
    path('', check_if_participants_exists ,name='check-participant'),
    path('create_participant', create_participant, name='create-participant'),
    path('check_connection', check_if_connection_exists, name='check-connection'),
    path('create_connection', create_connection, name="create-connection" ),
    path('send_message', send_message, name="send-message" )
]
