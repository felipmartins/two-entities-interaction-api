import random
from .models import InteractionConnection

def create_new_pin_number():
                not_unique = True
                while not_unique:
                    unique_pin = random.randint(10000, 99999)
                    if not InteractionConnection.objects.filter(Referrence_Number=unique_pin):
                        not_unique = False
                return str(unique_pin)