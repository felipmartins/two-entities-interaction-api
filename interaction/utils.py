import random
from .models import Connection

def create_new_pin_number():
                not_unique = True
                while not_unique:
                    unique_pin = random.randint(10000, 99999)
                    if not Conection.objects.filter(Referrence_Number=unique_pin):
                        not_unique = False
                return str(unique_pin)