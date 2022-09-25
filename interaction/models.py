from argparse import _MutuallyExclusiveGroup
from django.db import models
from utils import create_new_pin_number
import uuid

class Connection(models.Model):
    status_list = [
        ('Aguardando participantes', 'Aguardando participantes'),
        ('Conexão estabelecidada', 'Conexão estabelecidada'),
        ('Turno da pessoa 1', 'Turno da pessoa 1 '),
        ('Turno da pessoa 2', 'Turno da pessoa 2 '),
        ('Conexão Finalizada', 'Conexão Finalizada')
    ]


    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    pin =  models.Charfield(max_length=5, unique=True, default=create_new_pin_number)
    connection_status = models.CharField(max_length=15, choices=status_list)
    participants = models.JSONField()
    turn = models.ForeignKey(Participant, on_delete=models.CASCADE)


class Participant(models.Model):
    alexa_id = models.CharField(max_lenght=100, primary_key=True, editable=False)
    name = models.CharField(max_length=50)