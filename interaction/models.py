import uuid
import random
from django.db import models


class Participant(models.Model):
    alexa_id = models.CharField(max_length=100, primary_key=True, editable=False)
    name = models.CharField(max_length=50)


class InteractionConnection(models.Model):

    def create_new_pin_number():
        not_unique = True
        while not_unique:
            unique_pin = random.randint(10000, 99999)
            if not InteractionConnection.objects.filter(pin=unique_pin):
                not_unique = False
        return str(unique_pin)


    status_list = [
        ("Aguardando participantes", "Aguardando participantes"),
        ("Conexão estabelecidada", "Conexão estabelecidada"),
        ("Conexão Finalizada", "Conexão Finalizada"),
    ]


    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    pin = models.CharField(max_length=5, unique=True, default=create_new_pin_number, editable=False)
    connection_status = models.CharField(max_length=30, choices=status_list)
    participants = models.JSONField()
    turn = models.ForeignKey(Participant, on_delete=models.CASCADE)

